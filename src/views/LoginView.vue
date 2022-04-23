<script>
import LoginForm from "@/components/LoginForm.vue";

    export default {
        data() {
            return {};
        },
        components: { LoginForm }
    };
</script>

<template>
    <div class="form-container">
        <h2>LoginForm</h2>
        <LoginForm />
    </div>
</template>

<style>
h2 {
    display: flex;
    justify-content: center;
}
</style>