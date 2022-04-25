<template>
  <section id="explore-page">
    <div class="heading">
      <h1>Explore</h1>
    </div>
    <div class="search-cars">
      <div class="inputs">
        <label class="model" for="make">Make</label>
        <input
          type="search"
          name="make"
          v-model="searchTermMake"
          v-on:change="empty"
          id="make"
          class="search-input"
        />
      </div>
      <div class="inputs">
        <label class="model" for="model">Model</label>
        <input
          type="search"
          name="model"
          v-model="searchTermModel"
          v-on:change="empty"
          id="model"
          class="search-input"
        />
      </div>
      <button class="btn-search" @click="searchCars">Search</button>
    </div>

    <div class="car-cards">
      <ul class="cars-lst">
        <li v-for="car in currentCars" :key="car.id">
          <div class="car-card">
            <div class="photo">
              <img :src="API_ENDPOINT + '/uploads/' + car.photo" alt="car" />
            </div>
            <div class="car-info">
              <div>
                <span class="name-and-price">
                  <p class="year-and-make">{{ car.year + " " + car.make }}</p>
                  <span class="car-price">
                    <img class="tags" src="../assets/tag.svg" alt="tag" />
                    <p>${{ car.price }}</p>
                  </span>
                </span>
                <p class="car-model">{{ car.model }}</p>
              </div>
            </div>
            <button @click="cardetail(car.id)" class="btn-details">
              View More Details
            </button>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
    export default {
        data() {
            return {
                cars: [],
                searchCars: ""
            };
        },
        methods: {
            searchCars() {
                let self = this;
                fetch('${import.meta.env.VITE_API_URL}/api/cars'+ self.searchCars + '&language=en', {
                    headers: authHeader()
                }
            ).then(function(response) {
                return response.json();
            }).then(function(data) {
                console.log(data);
                self.cars = data.cars;
            });
            }
        },
        created() {
            let self = this;
            fetch(`${import.meta.env.VITE_API_URL}/api/cars`,
            {
            headers: authHeader()
            }
        ).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log(data);
            self.cars = [JSON.parse(data.cars)[-1], JSON.parse(data.cars)[-2], JSON.parse(data.cars)[-3]];
        });
        },
        authHeader() {
            let accessToken = localStorage.getItem("jwt");

            if (accessToken) {
                return { Authorization: "Bearer " + accessToken };
            } else {
                return {};
            }
        }
    };
</script>

<style>
/* Add any component specific styles here */
</style>