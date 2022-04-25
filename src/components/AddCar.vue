<template>
  <form
    @submit.prevent="addCar"
    id="addCarForm"
    method="POST"
    enctype="multipart/form-data"
  >
    <div class="row">
      <div class="col">
        <label for="make">Make</label>
        <input type="text" name="make" id="make" class="form-control" />
      </div>
      <div class="col">
        <label for="model">Model</label>
        <input type="text" name="model" id="model" class="form-control" />
      </div>
    </div>

    <div class="row">
      <div class="col">
        <label for="transmissionType">Transmission</label>
        <input
          type="text"
          name="transmissionType"
          id="transmissionType"
          class="form-control"
        />
      </div>
      <div class="col">
        <label for="year">Year</label>
        <input type="text" name="year" id="year" class="form-control" />
      </div>
    </div>

    <div class="row">
      <div class="col">
        <label for="colour">Colour</label>
        <input type="text" name="colour" id="colour" class="form-control" />
      </div>

      <div class="col">
        <label for="carType">Type</label>
        <input type="text" name="carType" id="carType" class="form-control" />
      </div>
    </div>

    <div class="row">
      <div class="col">
        <label for="description">Description</label>
        <br />
        <textarea
          name="description"
          id="description"
          cols="45"
          rows="5"
        ></textarea>
      </div>

      <div class="col">
        <label for="price">Price</label>
        <div class="input-group mb-3">
          <span class="input-group-text">$</span>
          <input type="text" class="form-control" name="price" id="price" />
          <span class="input-group-text">.00</span>
        </div>
        <label for="carPhoto">Upload a Photo</label>
        <input type="file" name="carPhoto" id="carPhoto" class="form-control" />
      </div>
    </div>

    <button class="btn btn-warning text-white mt-3 px-4" type="submit">
      Submit
    </button>
  </form>
</template>

<script>
import headerUtils from "./../util/header.util";

export default {
  data() {
    return {
      csrf_token: "",
    };
  },
  methods: {
    addCar() {
      const self = this;
      let addCarForm = document.getElementById("addCarForm");
      let form_data = new FormData(addCarForm);

      fetch(`${import.meta.env.VITE_API_URL}/api/cars`, {
        method: "POST",
        body: form_data,
        headers:headerUtils.authHeader()
      })
        .then(async function (response) {
            if (response.status == 201)
            {
                alert("Car added successfully")
                self.$router.push('/explore')
            }
        })
    },
  },
};
</script>

<style>
textarea {
  vertical-align: top;
}
</style>