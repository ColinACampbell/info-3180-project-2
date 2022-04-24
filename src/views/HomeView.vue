<script>
export default {
    created() {
      console.log(import.meta.env.VITE_API_URL)
    },
    data() {
        return {
            
        };
    },
}
</script>

<template>
      <div class="d-flex align-items-center row">
        <div class="col-6">
          <div class="container mx-4 px-5">
            <h1 class="text-warning">Buy and Sell Cars Online</h1>
            <p class="text-muted">United Auto Sales provides the fastest, easiest and most user friendly way to buy or sell cars online. Find a great price on the vehicle you want!</p>
          <div class="row">
            <div class="col-2">
           <RouterLink class="router-link btn btn-primary btn-link text-light px-5" to="/register">Register</RouterLink>
            </div>
            <div class="col-4">
            <RouterLink class="router-link btn btn-warning btn-link text-light ms-5 px-5" to="/login">Login</RouterLink>
            </div>
          </div>
          </div>
        </div>
        <div class="col-6  d-flex justify-content-end">
        <img class="vh-100" src="https://images.unsplash.com/photo-1550355291-bbee04a92027?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1936&q=80" alt="red car">
        </div>
      </div>
</template>

<style>
/* Add any component specific styles here */
.router-link {
text-decoration: none;
}
</style>