<template>
        <div class="card shadow p-3 mb-5 bg-body rounded mx-auto" style="width: 55vw">
            <img :src="car.photo" alt="car.make" class="card-img-top">
            <div class="card-body">
                <h3 class="card-title">{{ car.make  }}</h3>
                <h4 class="card-title text-muted">{{ car.model }}</h4>
                <p class="card-text">{{ car.description }}</p>
                <div class="row">
                    <div class="col-md-6">
                    <p class="card-text">Colour &nbsp; &nbsp; <strong>{{ colour }}</strong></p>
                    </div>
        
                    <div class="col-md-6">
                    <p class="card-text">Body Type &nbsp; &nbsp; <strong>{{ car.car_type }}</strong></p>
                    </div>
                </div>
        
                <div class="row mb-5">
                    <div class="col-md-6">
                    <p class="card-text">Price &nbsp; &nbsp; <strong>{{ car.price }}</strong></p>
                    </div>
        
                    <div class="col-md-6">
                    <p class="card-text">Transmission &nbsp; &nbsp; <strong>{{ car.transmission }}</strong></p>
                    </div>
                </div>
               
                <div class="row">
                    <div class="col"><button class="btn btn-warning text-light">Email Owner</button></div>
        
                    <div class="col d-flex justify-content-end"><button class="btn-round"><i :class="[favButtonActive ? 'fa-solid' : 'fa-regular']" @click="favButtonActive = !favButtonActive" class="fa fa-heart"></i></button></div>
                </div>       
            </div>
        </div>
</template>

<script>
export default {
    data() {
        return {
            favButtonActive: false,
            car: [],
        }
    },
    computed: {
        carID() {
            return parseInt(this.$route.params.id)
        },
    },
    methods: {
        getCar() {
             fetch(`${import.meta.env.VITE_API_URL}/api/cars/${carID()}`, {method: 'GET', 
                headers: {'Content-Type': 'application/json'}
                }).then(function (response) {
                    return response.json();
                }).then(function (data) {
                    console.log(data);
                    this.car = data
                }).catch(function (error) {
                    console.log(error);
                });
         }
    },
   
}
</script>

<style>
.btn-round {
    border-style: solid;
    border-width: thin;
    border-radius: 50%;
    padding: 5px 10px;
    border-color: #ccc6c5;
    color:#e34f44;
    background-color: white;
    

}

</style>