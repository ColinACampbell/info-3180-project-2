<template>
  <div v-if="errors.length > 0">
    <div v-for="error in errors" :key="error.name" class="alert alert-danger">
      {{ error }}
    </div>
  </div>
</template>

<script>
export default {
  props:['errors']
};
</script>

<style>
</style>