<script>
import registerForm from './../components/RegisterForm.vue'

    export default {
        data() {
            return {};
        },
        components: { RegisterForm }
    };
</script>

<template>
    <div class="form-container">
        <h2>User Registration Form</h2>
        <RegisterForm />
    </div>
</template>

<style>
h2 {
    display: flex;
    justify-content: center;
}
</style>