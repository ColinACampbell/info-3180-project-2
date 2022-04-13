<template>
      <footer class="mt-5">
          <div class="container">
              <p>Copyright &copy {{ year }} Flask Inc.</p>
          </div>
      </footer>
</template>

<script>
export default {
    data() {
      return {
          year: (new Date).getFullYear()
      }        
    }
}
</script>

<style>
/* Add any component specific styles here */
</style>