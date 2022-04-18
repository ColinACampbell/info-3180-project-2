<template>

 <form @submit.prevent="uploadPhoto" id="loginForm" method="POST" enctype="multipart/form-data">'

	<label class="label" for="username">Username</label>
    <input type="text" name="name" id="name" class="form-control" placeholder="Enter your Username"/>
	<label class="label" for="password">Password</label>
    <input type="text" name="password" id="password" class="form-control" placeholder="Enter your Password"/>
	<button class="btn">Login</button>

</form>

</template>

<script>

</script>

<style>
/* Add any component specific styles here */
</style>