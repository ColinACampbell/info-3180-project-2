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
      <div class="col">
        <button class="btn btn-warning text-light px-5" @click="searchCars">
          Search
        </button>
      </div>
    </div>

    <div class="car-cards">
      <ul class="cars-lst">
        <li v-for="car in cars" :key="car.id">
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
            <button @click="carDetail(car.id)" class="btn-details">
              View More Details
            </button>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
import headerUtils from "./../util/header.util";

export default {
  data() {
    return {
      cars: [],
      searchCars: "",
    };
  },
  methods: {
    carDetail(id) {
      this.$router.push({ name: 'car-details', params: { id } })
    },
    searchCars() {
      let self = this;
      fetch(
        `${import.meta.env.VITE_API_URL}/api/cars` +
          self.searchCars +
          "&language=en",
        {
          headers: authHeader(),
        }
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          self.cars = data.cars;
        });
    },
  },
  created() {
    let self = this;
    fetch(`${import.meta.env.VITE_API_URL}/api/cars`, {
      headers: headerUtils.authHeader(),
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        let carCount = data.length;
        let i = carCount - 1;
        while (carCount > 0) {
          self.cars.push(data[i]);
          i--;
          carCount--;
          if (i == 2) break;
        }
        console.log(self.cars);
      });
  },
};
</script>

<style>
/* Add any component specific styles here */
</style>