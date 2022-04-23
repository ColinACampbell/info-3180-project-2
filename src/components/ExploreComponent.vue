<template>
    <form @submit.prevent="searchCars" class="d-flex flex-column justify-content-center">
        <div class="input-group mx-sm-3 mb-2">
            <label class="visually-hidden" for="search">Search</label>
            <input type="search" name="search" v-model="searchCar" id="search" class="form-control mb-2 mr-sm-2" placeholder="Search here" />
            <button class="btn btn-primary mb-2">Search</button>
        </div>
        <p>You are searching for {{ searchCar }}</p>
    </form>
    <ul class="car-list">
        <li v-for="car in cars" class="car-view">
         <img :src="car.urlToImage" :alt="car.model" />
         <p class="car-make">{{ car.make }}</p>
         <p class="car-model">{{ car.model }}</p>
         <p class="car-year">{{ car.year }}</p>
         <p class="car-price">{{ car.price }}</p>
         <p class="car-description">{{ car.description }}</p>
        </li>
    </ul>


</template>

<script>
    export default {
        data() {
            return {
                cars: [],
                searchCars: ''
            };
        },
        methods: {
            searchCars() {
                let self = this;
                fetch(''+ self.searchCars + '&language=en', {
                    headers: {
                        'Authorization': `Bearer ${import.meta.env.VITE_NEWSAPI_TOKEN}`,
                }
            }).then(function(response) {
                return response.json();
            }).then(function(data) {
                console.log(data);
                self.cars = data.cars;
            });
            }
        },
        created() {
            let self = this;
            fetch(`https://newsapi.org/v2/top-headlines?country=us&apiKey=${import.meta.env.VITE_NEWSAPI_TOKEN}`,
            {
            headers: {
                'Authorization': `Bearer ${import.meta.env.VITE_NEWSAPI_TOKEN}`
            }
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log(data);
            self.cars = data.cars;
        });
        }
    };
</script>

<style>
/* Add any component specific styles here */
</style>