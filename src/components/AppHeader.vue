<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container-fluid">
        <a class="navbar-brand fw-bold text-warning" href="/">United Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <div :class="[isLoggedIn ? '' : 'd-none']" class="d-flex flex-row">
              <li class="nav-item ps-5 pe-3">
                <RouterLink to="/" class="nav-link active">Home</RouterLink>
              </li>
              <li class="nav-item px-3">
                <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
              </li>
              <li class="nav-item px-3">
                <RouterLink class="nav-link" :to="USER_ROUTE"
                  >My Account</RouterLink
                >
              </li>
              <li class="nav-item px-3">
                <RouterLink class="nav-link" to="/cars/new"
                  >Add a Car</RouterLink
                >
              </li>
            </div>
            <div :class="[isLoggedIn ? 'd-none' : '']" class="d-flex flex-row">
              <li class="nav-item px-3 d-flex justify-content-end">
                <RouterLink class="nav-link" to="/register">Register</RouterLink>
              </li>
              <li class="nav-item px-3 d-flex justify-content-end">
                <RouterLink class="nav-link" to="/login">Login</RouterLink>
              </li>
            </div>
            <li :class="[isLoggedIn ? '' : 'd-none']" class="nav-item px-3 d-flex justify-content-end">
                <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
              </li>
            
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
import headerUtils from "./../util/header.util"
export default {
  created() {
    try {
      let token = headerUtils.authHeader().Authorization;
      console.log("Runs");
      if (token) {
        this.isLoggedIn = true;
      }
    } catch (error) {
      console.log(error);
    }
  },
  computed:{
    USER_ROUTE : () => {
    const user =JSON.parse(localStorage.getItem('user') ?? '{}')
    console.log(localStorage.getItem('user'))
    return `/users/${user.id}`
    }
  },
  data() {
    return {
      isLoggedIn: false,
    }
  },
  methods:
  {
    authHeader() {
      let accessToken = localStorage.getItem("jwt");

      if (accessToken) {
        return { Authorization: "Bearer " + accessToken };
      } else {
        return {};
      }
  },
    created() {
      try {
        let token = authHeader().Authorization;
  
        if(token) {
          this.isLoggedIn = true;
        }
      } catch (error) {
        console.log(error)
      }
    },
  }
}
</script>

<style>
/* Add any component specific styles here */
</style>