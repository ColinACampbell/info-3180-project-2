<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
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
            <li class="nav-item ps-5 pe-3">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
           <!--<li class="nav-item px-3">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>--> 
            <li class="nav-item px-3">
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item px-3">
              <RouterLink class="nav-link" to="/cars/new">Add a Car</RouterLink>
            </li>
            <li class="nav-item px-3">
              <RouterLink class="nav-link" to="/login">Login</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
</script>

<style>
/* Add any component specific styles here */
</style>