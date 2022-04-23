<script>
export default {
    created() {
      console.log(import.meta.env.VITE_API_URL)
    },
    data() {
        return {
            message: "Find A Car"
        };
    },
}
</script>

<template>
    <div id="home" class="container">
      <div class="text-center align-middle">
        <h1 class="text-warning">{{ message }}</h1>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
#home { 
  width: 100%;
  height: 100%;
  
  background-image: url(https://images.pexels.com/photos/7230049/pexels-photo-7230049.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1);

  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>