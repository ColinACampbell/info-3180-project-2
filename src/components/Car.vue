<template>
  <div class="card shadow p-3 mb-5 bg-body rounded mx-auto" style="width: 55vw">
    <img
      :src="API_ENDPOINT + '/' + car.photo"
      alt="car.make"
      class="card-img-top"
    />
    <div class="card-body">
      <h3 class="card-title">{{ car.make }}</h3>
      <h4 class="card-title text-muted">{{ car.model }}</h4>
      <p class="card-text">{{ car.description }}</p>
      <div class="row">
        <div class="col-md-6">
          <p class="card-text">
            Colour &nbsp; &nbsp; <strong>{{ car.color }}</strong>
          </p>
        </div>

        <div class="col-md-6">
          <p class="card-text">
            Body Type &nbsp; &nbsp; <strong>{{ car.car_type }}</strong>
          </p>
        </div>
      </div>

      <div class="row mb-5">
        <div class="col-md-6">
          <p class="card-text">
            Price &nbsp; &nbsp; <strong>{{ car.price }}</strong>
          </p>
        </div>

        <div class="col-md-6">
          <p class="card-text">
            Transmission &nbsp; &nbsp; <strong>{{ car.transmission }}</strong>
          </p>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <button class="btn btn-warning text-light">Email Owner</button>
        </div>

        <div class="col d-flex justify-content-end">
          <button class="btn-round">
            <i
              :class="[favButtonActive ? 'fa-solid' : 'fa-regular']"
              @click="favCar() isFav()"
              class="fa fa-heart"
            ></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import headerUtils from "./../util/header.util";

export default {
  mounted() {
    const carID = parseInt(this.$route.params.id);
    const self = this;
    fetch(`${import.meta.env.VITE_API_URL}/api/cars/${carID}`, {
      method: "GET",
      headers: headerUtils.authHeader(),
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        self.car = data;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  data() {
    return {
      favButtonActive: false,
      car: [],
      currentCars: [],
      count: 0
    };
  },
  computed: {
    carID() {
      return parseInt(this.$route.params.id);
    },
    API_ENDPOINT: function () {
      return import.meta.env.VITE_API_URL;
    },
  },
  methods: {
    getCar() {},
    isFav() {
        let self = this;
            fetch(`${import.meta.env.VITE_API_URL}/api/users/${userID()}/favourites`,
            {
            headers: authHeader()
            }
        ).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log(data);
            self.currentCars = data.currentCars;
            for (car in currentCars) {
            if (car.id == carID) {
                count = 1
            }
            if (count > 0) {
                favButtonActive: true
            } else {
                favButtonActive: false
            }
        });

    }
  },
  favCar() {
    let self = this;
            fetch(`${import.meta.env.VITE_API_URL}/api/cars/${carID}/favourites`, methods=['POST'],
            {
            headers: authHeader()
            }
        ).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log(data);
        });

    }
  }

};
</script>

<style>
.btn-round {
  border-style: solid;
  border-width: thin;
  border-radius: 50%;
  padding: 5px 10px;
  border-color: #ccc6c5;
  color: #e34f44;
  background-color: white;
}
</style>