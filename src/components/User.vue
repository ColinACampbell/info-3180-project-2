<template>
  <div class="row">
    <div class="card shadow p-3 mb-5 bg-body rounded mx-auto">
      <img src="" alt="" class="card-img-top" />
      <div class="card-body">
        <h3 class="card-title">{{ user.name }}</h3>
        <h4 class="card-title text-muted">{{ user.username }}</h4>
        <p class="card-text">
          {{
           user.biography
          }}
        </p>
        <div class="row">
          <div class="col">
            <p class="card-text">Email</p>
          </div>

          <div class="col">
            <p class="card-text">{{user.email }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <p class="card-text">Location</p>
          </div>

          <div class="col">
            <p class="card-text">{{ user.location }}</p>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <p class="card-text">Joined</p>
          </div>

          <div class="col">
            <p class="card-text">{{ "April 8, 2021" }}</p>
          </div>
        </div>
      </div>
    </div>
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
                  <img class="tags" src="" alt="tag" />
                  <p>${{ car.price }}</p>
                </span>
              </span>
              <p class="car-model">{{ car.model }}</p>
            </div>
          </div>
          <button @click="getCar(car.id)" class="btn-details">
            View More Details
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import headerUtils from "./../util/header.util";

export default {
  created() {
    this.getUser();
  },
  data() {
    return {
      currentCars: [],
      car: [],
      user: {},
    };
  },
  computed: {
    carID() {
      return parseInt(this.$route.params.id);
    },
    userID() {
      return parseInt(this.$route.params.id);
    },
  },
  methods: {
    getUser() {
      let self = this;
      fetch(`${import.meta.env.VITE_API_URL}/api/users/${this.userID}`, {
        method: "GET",
        headers: headerUtils.authHeader(),
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          self.user = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    getCar() {
      fetch(`${import.meta.env.VITE_API_URL}/api/cars/${carID()}`, {
        method: "GET",
        headers: authHeader(),
        "Content-Type": "application/json",
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          this.car = data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    created() {
      let self = this;
      fetch(
        `${import.meta.env.VITE_API_URL}/api/users/${userID()}/favourites`,
        {
          headers: authHeader(),
        }
      )
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          console.log(data);
          self.currentCars = data.currentCars;
        });
    },
    authHeader() {
      let accessToken = localStorage.getItem("jwt");

      if (accessToken) {
        return { Authorization: "Bearer " + accessToken };
      } else {
        return {};
      }
    },
  },
};
</script>

<style>
</style>