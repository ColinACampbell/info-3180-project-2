<template>
    <div class="container">
        <h2 class="text-warning">Add a New Car</h2>
        <hr class="solid">
        <AddCar />
    </div>
</template>

<script>
import AddCar from "@/components/AddCar.vue";
export default {
    data() {

    },
    components: { AddCar }
}
</script>

<style>
    hr.solid {
        border-top: 3px solid #bbb;
    }
</style>