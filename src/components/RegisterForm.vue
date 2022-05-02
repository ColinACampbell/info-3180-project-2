<template>
  <form
    @submit.prevent="register"
    id="registerForm"
    method="POST"
    enctype="multipart/form-data"
  >
    <label class="label" for="username">Username</label>
    <input
      type="text"
      name="username"
      id="username"
      class="form-control"
      placeholder="Enter your Username"
    />
    <label class="label" for="password">Password</label>
    <input
      type="password"
      name="password"
      id="password"
      class="form-control"
      placeholder="Enter your Password"
    />
    <label class="label" for="firstname"> Name</label>
    <input
      type="text"
      name="name"
      id="name"
      class="form-control"
      placeholder="Enter your Name"
    />

    <label class="label" for="email">Email</label>
    <input
      type="text"
      name="email"
      id="email"
      class="form-control"
      placeholder="Enter your Email Address"
    />
    <label class="label" for="location">Location</label>
    <input
      type="text"
      name="location"
      id="location"
      class="form-control"
      placeholder="Enter your Location"
    />
    <label class="label" for="biography">Biography</label>
    <input
      type="text"
      name="bio"
      v-model="biography"
      id="biography"
      class="form-control"
      placeholder="Add a Biography"
    />
    <label class="label" for="userPhoto">Upload Photo</label>
    <input type="file" name="photo" id="userPhoto" class="form-control" />
    <button class="btn btn-primary" type="submit">Register</button>
    <Errors :errors="errors" />
  </form>
</template>

<script>
import Errors from "@/components/Errors.vue";

export default {
  components: { Errors },
  data() {
    return {
      csrf_token: "",
      errors: [],
    };
  },
  methods: {
    register() {
      let registerForm = document.getElementById("registerForm");
      let form_data = new FormData(registerForm);

      const self = this;

      fetch(`${import.meta.env.VITE_API_URL}/api/register`, {
        method: "POST",
        body: form_data,
      }).then(async (response) => {
        const data = await response.json();
        if (response.status == 201) {
          const user = data.user;

          const jwt = data.token;
          localStorage.setItem("jwt", jwt);
          localStorage.setItem("user", JSON.stringify(user));

          this.$router.push("/explore");
        } else {
          self.errors = data.message;
        }
      });
    },
  },
  created() {},
};
</script>

<style>
/* Add any component specific styles here */
</style>