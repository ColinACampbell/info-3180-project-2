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
    <button class="btn btn-primary" type="submit">Login</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      csrf_token: "",
    };
  },
  methods: {
    register() {
      let registerForm = document.getElementById("registerForm");
      let form_data = new FormData(registerForm);

      fetch(`${import.meta.env.VITE_API_URL}/api/register`, {
        method: "POST",
        body: form_data,
      }).then(async (response) => {
        if (response.status == 201) {
          const data = await response.json();
          const jwt = data.token;
          localStorage.setItem("jwt", jwt);
          this.$router.push("/explore");
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