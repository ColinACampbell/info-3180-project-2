<template>
  <section id="explore-page">

    <h1 class="text-warning m-5">Explore</h1>

    <div class="d-flex align-items-center search-cars row">
      <div class="inputs col d-flex align-items-center">
        <label class="model me-2" for="make">Make</label>
        <input
          type="search"
          name="make"
          v-model="searchTermMake"
          v-on:change="empty"
          id="make"
          class="search-input form-control"
        />
      </div>
      <div class="inputs col d-flex align-items-center">
        <label class="model me-2" for="model">Model</label>
        <input
          type="search"
          name="model"
          v-model="searchTermModel"
          v-on:change="empty"
          id="model"
          class="search-input form-control"
        />
      </div>
      <div class="col"><button class="btn btn-warning text-light px-5" @click="searchCars">Search</button></div>
    </div>

    <div class="car-cards card-group">
      <ul class="cars-lst">
        <li v-for="car in currentCars" :key="car.id">
          <div class="card shadow-sm p-3 mb-5 bg-body rounded" style="width:25rem">
            <img :src="API_ENDPOINT + '/uploads/' + car.photo" alt="car" class="card-img-top"/>
            <div class="card-body">
                  <div class="row">
                    <div class="col">
                      <p class="year-and-make card-text fw-bolder">{{ car.year + " " + car.make }}</p>
                    </div>
                    <div class="col">
                      <p class="btn btn-warning"><i class="fa-solid fa-tag"></i> ${{ car.price }}</p>
                    </div>
                  </div>

                <p class="car-model text-muted">{{ car.model }}</p>
            </div>
            <button @click="cardetail(car.id)" class="btn btn-primary w-100">View More Details</button>
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

function authHeader() {
  let accessToken = localStorage.getItem("jwt");

  if (accessToken) {
    return { Authorization: "Bearer " + accessToken };
  } else {
    return {};
  }
}
</script>

<style>
/* Add any component specific styles here */
</style>