<template>
    <form @submit.prevent="" id="addCarForm" method="POST" enctype="multipart/form-data">
        <label for="make">Make</label>
        <input type="text" name="make" id="make" class="form-control">

        <label for="model">Model</label>
        <input type="text" name="model" id="model" class="form-control">
        
        <label for="transmission">Transmission</label>
        <input type="text" name="transmission" id="transmission" class="form-control">
        
        <label for="description">Description</label>
        <textarea name="description" id="description" cols="30" rows="10"></textarea>

        <label for="year">Year</label>
        <input type="text" name="year" id="year" class="form-control">
        
        <label for="colour">Colour</label>
        <input type="text" name="colour" id="colour" class="form-control">
        
        <label for="type">Type</label>
        <input type="text" name="type" id="type" class="form-control">
        
        <label for="price">Price</label>
        <div class="input-group mb-3">
            <span class="input-group-text">$</span>
            <input type="text" class="form-control" name="price" id="price">
            <span class="input-group-text">.00</span>
        </div>

        <label for="uploadPhoto">Upload a Photo</label>
        <input type="file" name="uploadPhoto" id="uploadPhoto" class="form-control">
    </form>
</template>

<script>
export default {
    data() {
        
    },
}
</script>

<style>

</style>