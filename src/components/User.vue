<template>
    <div class="row">
        <div class="card shadow p-3 mb-5 bg-body rounded mx-auto">
            <img src="" alt="" class="card-img-top">
            <div class="card-body">
                <h3 class="card-title">{{ "User's Name" }}</h3>
                <h4 class="card-title text-muted">{{ "username" }}</h4>
                <p class="card-text">{{ "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget vulputate augue. Maecenas nibh eros, cursus eu fermentum non, dignissim sit amet nisi. Cras nec ipsum sit amet mauris lacinia elementum vel id velit. Nullam facilisis tempus iaculis. Mauris maximus ante leo, quis bibendum enim ullamcorper id." }}</p>
                <div class="row">
                    <div class="col">
                    <p class="card-text">Email</p>
                    </div>
        
                    <div class="col">
                    <p class="card-text">{{ "email@email.com" }}</p>
                    </div>
                </div>
        
                <div class="row">
                    <div class="col">
                    <p class="card-text">Location</p>
                    </div>
        
                    <div class="col">
                    <p class="card-text">{{ "location" }}</p>
                    </div>
                </div>
                
                <div class="row">
                    <div class="col">
                    <p class="card-text">Joined</p>
                    </div>
        
                    <div class="col">
                    <p class="card-text">{{ "April 8, 2021" }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    data() {

    },
    methods: {
        getUser() {
            let self = this;
            fetch(`${import.meta.env.VITE_API_URL}/api/users${self.getUser}&language=en`,{
                
            })
        }
    }
}
</script>

<style>

</style>