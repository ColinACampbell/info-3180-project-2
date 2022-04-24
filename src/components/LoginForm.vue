<template>
 <form @submit.prevent="login" id="loginForm" method="POST" enctype="multipart/form-data">

	<label class="label" for="username">Username</label>
    <input type="text" name="username" id="username" class="form-control" placeholder="Enter your Username"/>
	<label class="label" for="password">Password</label>
    <input type="text" name="password" id="password" class="form-control" placeholder="Enter your Password"/>
	<button class="btn">Login</button>

</form>

</template>

<script>
export default {
        data() {
            return {
                csrf_token: "",
            }
        },
        methods: {
            login() {

                const self = this;
                let loginForm = document.getElementById('loginForm');
                let form_data = new FormData(loginForm);

                fetch(`${import.meta.env.VITE_API_URL}/api/auth/login`, {
                    method: "POST",
                    body: form_data,
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    console.log(data);
                }).catch(function (error) {
                    console.log(error);
                });
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
            })
            }
        },
        created() {
            this.getCsrfToken();
        }
    }
</script>

<style>
/* Add any component specific styles here */
</style>