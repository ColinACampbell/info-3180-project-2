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

    <div class="card-group">
      <div v-for="car in cars" :key="car.id">
        <div
          class="card shadow-sm p-3 mb-5 bg-body rounded"
          style="width: 20rem; min-height:500px"
        >
          <img
            :src="API_ENDPOINT + '/' + car.photo"
            alt="car"
            class="card-img-top"
          />
          <div class="card-body">
            <div class="row">
              <div class="col">
                <p class="year-and-make card-text fw-bolder">
                  {{ car.year + " " + car.make }}
                </p>
              </div>
              <div class="col">
                <p class="btn btn-warning text-light">
                  <i class="fa-solid fa-tag"></i> ${{ car.price }}
                </p>
              </div>
            </div>

            <p class="car-model text-muted">{{ car.model }}</p>
          </div>
          <button
            @click="carDetail(car.id)"
            class="btn btn-primary w-100 text-light"
          >
            View More Details
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import headerUtils from "./../util/header.util";

export default {
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
        let count = 0;
        while (carCount > 0) {
          self.cars.push(data[i]);
          i--;
          carCount--;
          count++;
          if (count == 3) break;
        }
        console.log(self.cars);
      });
  },
  data() {
    return {
      cars: [],
      searchCars: "",
    };
  },
  computed: {
    API_ENDPOINT: function () {
      return import.meta.env.VITE_API_URL;
    },
  },
  methods: {
    carDetail(id) {
      this.$router.push({ name: "car-details", params: { id } });
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
};
</script>

<style>
.card-group{
  margin-top:30px
}
</style>