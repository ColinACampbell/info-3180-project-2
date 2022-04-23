<template>

 <form @submit.prevent="login" id="loginForm" method="POST" enctype="multipart/form-data">

	<label class="label" for="username">Username</label>
    <input type="text" name="name" id="name" class="form-control" placeholder="Enter your Username"/>
	<label class="label" for="password">Password</label>
    <input type="password" name="password" id="password" class="form-control" placeholder="Enter your Password"/>
	<button class="btn">Login</button>


</form>

</template>

<script>

export default {
    name: "LoginForm",
        data() {
            return {
                csrf_token: '',
            }
        },
        methods: {
            methods: {
            login() {

                const self = this;
                let loginForm = document.getElementById('loginForm');
                let form_data = new FormData(loginForm);

                fetch("/api/login", {method: 'POST', body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                    }
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    // display a success message
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
}
</script>

<style>
/* Add any component specific styles here */
</style>