<template>
  <form
    @submit.prevent="login"
    id="loginForm"
    method="POST"
    enctype="multipart/form-data"
  >
    <div class="mb-3">
      <label class="form-label" for="username">Username</label>
      <input
        type="text"
        name="username"
        id="username"
        class="form-control"
        placeholder="Enter your Username"
      />
    </div>
    <div class="mb-3">
      <label class="form-label" for="password">Password</label>
      <input
        type="text"
        name="password"
        id="password"
        class="form-control"
        placeholder="Enter your Password"
      />
    </div>
    <button class="btn btn-warning text-white w-100">Login</button>
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
    login() {
      const self = this;
      let loginForm = document.getElementById("loginForm");
      let form_data = new FormData(loginForm);

      fetch(`${import.meta.env.VITE_API_URL}/api/auth/login`, {
        method: "POST",
        body: form_data,
      })
        .then(async (response) => {
          const data = await response.json();

          if (response.status == 200) {
            const jwt = data.token;
            localStorage.setItem("jwt", jwt);
            this.$router.push("/explore");
          } else {
            self.errors = data.message;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
  },
};
</script>

<style>
/* Add any component specific styles here */
</style>