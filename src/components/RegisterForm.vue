<template>

 <form @submit.prevent="register" id="registerForm" method="POST" enctype="multipart/form-data">'

	<label class="label" for="username">Username</label>
    <input type="text" name="username" id="username" class="form-control" placeholder="Enter your Username"/>
	<label class="label" for="password">Password</label>
    <input type="password" name="password" id="password" class="form-control" placeholder="Enter your Password"/>
    <label class="label" for="firstname">First Name</label>
    <input type="text" name="firstname" id="firstname" class="form-control" placeholder="Enter your First Name"/>
	<label class="label" for="lastname">Last Name</label>
    <input type="text" name="lastname" id="lastname" class="form-control" placeholder="Enter your Last Name"/>
    <label class="label" for="email">Email</label>
    <input type="text" name="email" id="email" class="form-control" placeholder="Enter your Email Address"/>
	<label class="label" for="location">Location</label>
    <input type="text" name="location" id="location" class="form-control" placeholder="Enter your Location"/>
    <label class="label" for="biography">Biography</label>
    <input type="text" name="biography" v-model="biography" id="biography" class="form-control" placeholder="Add a Biography"/>
    <label class="label" for="userPhoto">Upload Photo</label>
    <input type="file" name="userPhoto" id="userPhoto" class="form-control"/>
	<button class="btn">Login</button>

</form>

</template>

<script>

export default {
        data() {
            return {
                csrf_token: '',
            }
        },
        methods: {
            methods: {
            register() {

                const self = this;
                let registerForm = document.getElementById('registerForm');
                let form_data = new FormData(registerForm);

                fetch(`${import.meta.env.VITE_API_URL}/api/register`, {method: 'POST', body: form_data
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
}
</script>

<style>
/* Add any component specific styles here */
</style>