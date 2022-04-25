<template>
    <div v-for="error in errors" :key="error.name" class="alert alert-danger">
        {{ error }}
    </div>
</template>

<script>
export default {
    data() {
        return {
            errors: [],
        }
    },
    created() {
        let self = this;
        fetch(`${import.meta.env.VITE_API_URL}/api/`, {
      headers: headerUtils.authHeader(),
    })
      .catch(function (error) {
        console.log(error);
        self.errors.push(error)
      });
  },
}


</script>

<style>

</style>