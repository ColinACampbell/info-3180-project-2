import{_ as l,h as p,o as d,c as i,w as m,b as u,r as _,d as f,a as n}from"./index.b022a2b4.js";const v={data(){return{csrf_token:""}},methods:{addCar(){const a=this;let e=document.getElementById("addCarForm"),t=new FormData(e);fetch("http://192.168.100.199:8080/api/cars",{method:"POST",body:t,headers:p.authHeader()}).then(async function(o){o.status==201&&(alert("Car added successfully"),a.$router.push("/explore"))})}}},b=u('<div class="row"><div class="col"><label for="make">Make</label><input type="text" name="make" id="make" class="form-control"></div><div class="col"><label for="model">Model</label><input type="text" name="model" id="model" class="form-control"></div></div><div class="row"><div class="col"><label for="transmissionType">Transmission</label><input type="text" name="transmissionType" id="transmissionType" class="form-control"></div><div class="col"><label for="year">Year</label><input type="text" name="year" id="year" class="form-control"></div></div><div class="row"><div class="col"><label for="colour">Colour</label><input type="text" name="colour" id="colour" class="form-control"></div><div class="col"><label for="carType">Type</label><input type="text" name="carType" id="carType" class="form-control"></div></div><div class="row"><div class="col"><label for="description">Description</label><br><textarea name="description" id="description" cols="45" rows="5"></textarea></div><div class="col"><label for="price">Price</label><div class="input-group mb-3"><span class="input-group-text">$</span><input type="text" class="form-control" name="price" id="price"><span class="input-group-text">.00</span></div><label for="carPhoto">Upload a Photo</label><input type="file" name="carPhoto" id="carPhoto" class="form-control"></div></div><button class="btn btn-warning text-white mt-3 px-4" type="submit"> Submit </button>',5),y=[b];function h(a,e,t,o,c,s){return d(),i("form",{onSubmit:e[0]||(e[0]=m((...r)=>s.addCar&&s.addCar(...r),["prevent"])),id:"addCarForm",method:"POST",enctype:"multipart/form-data"},y,32)}var x=l(v,[["render",h]]);const C={data(){},components:{AddCar:x}},w={class:"container"},$=n("h2",{class:"text-warning"},"Add a New Car",-1),T=n("hr",{class:"solid"},null,-1);function g(a,e,t,o,c,s){const r=_("AddCar");return d(),i("div",w,[$,T,f(r)])}var A=l(C,[["render",g]]);export{A as default};