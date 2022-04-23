<template>
    <div class="row">
        <div class="card shadow p-3 mb-5 bg-body rounded mx-auto">
            <img src="https://www.tesla.com/sites/default/files/images/roadster/roadster-social.jpg" alt="" class="card-img-top">
            <div class="card-body">
                <h3 class="card-title">{{ "2018 Tesla" }}</h3>
                <h4 class="card-title text-muted">{{ "Model S" }}</h4>
                <p class="card-text">{{ "With the longest range and quickest acceleration of any electric vehicle in production, Model S is the highest performing sedan ever built. Both Long Range and Plaid powertrains, with updated battery architecture, are cpabable of back-to-back, consistent 1/4 mile runs." }}</p>
                <div class="row">
                    <div class="col">
                    <p class="card-text">Colour {{ "Red" }}</p>
                    </div>
        
                    <div class="col">
                    <p class="card-text">Body Type {{ "Sedan" }}</p>
                    </div>
                </div>
        
                <div class="row">
                    <div class="col">
                    <p class="card-text">Price {{ "$62,888" }}</p>
                    </div>
        
                    <div class="col">
                    <p class="card-text">Transmission {{ "Automatic" }}</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col"><button class="btn btn-warning">Email Owner</button></div>
        
                    <div class="col"><button class="btn-round"><i class="fa-regular fa-heart"></i></button></div>
                </div>
        
        
            </div>
        </div>
    </div>
</template>

<script>
export default {
    
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