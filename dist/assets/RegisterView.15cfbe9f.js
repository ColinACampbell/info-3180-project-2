import{E as f}from"./Errors.5f52a79c.js";import{_ as c,r as m,o as p,c as d,h,v as _,a,d as u,w as b,b as g}from"./index.52027f09.js";const y={components:{Errors:f},data(){return{csrf_token:"",errors:[]}},methods:{register(){let t=document.getElementById("registerForm"),e=new FormData(t);const n=this;fetch("https://info-3180-project-2-prod.herokuapp.com//api/register",{method:"POST",body:e}).then(async l=>{const r=await l.json();if(l.status==201){const o=r.user,s=r.token;localStorage.setItem("jwt",s),localStorage.setItem("user",JSON.stringify(o)),this.$router.push("/explore")}else n.errors=r.message})}},created(){}},w=g('<label class="label" for="username">Username</label><input type="text" name="username" id="username" class="form-control" placeholder="Enter your Username"><label class="label" for="password">Password</label><input type="password" name="password" id="password" class="form-control" placeholder="Enter your Password"><label class="label" for="firstname"> Name</label><input type="text" name="name" id="name" class="form-control" placeholder="Enter your Name"><label class="label" for="email">Email</label><input type="text" name="email" id="email" class="form-control" placeholder="Enter your Email Address"><label class="label" for="location">Location</label><input type="text" name="location" id="location" class="form-control" placeholder="Enter your Location"><label class="label" for="biography">Biography</label>',11),E=a("label",{class:"label",for:"userPhoto"},"Upload Photo",-1),x=a("input",{type:"file",name:"photo",id:"userPhoto",class:"form-control"},null,-1),v=a("button",{class:"btn btn-primary",type:"submit"},"Register",-1);function $(t,e,n,l,r,o){const s=m("Errors");return p(),d("form",{onSubmit:e[1]||(e[1]=b((...i)=>o.register&&o.register(...i),["prevent"])),id:"registerForm",method:"POST",enctype:"multipart/form-data"},[w,h(a("input",{type:"text",name:"bio","onUpdate:modelValue":e[0]||(e[0]=i=>t.biography=i),id:"biography",class:"form-control",placeholder:"Add a Biography"},null,512),[[_,t.biography]]),E,x,v,u(s,{errors:r.errors},null,8,["errors"])],32)}var F=c(y,[["render",$]]);const P={data(){return{}},components:{RegisterForm:F}},R={class:"container"},S=a("h2",{class:"text-warning text-center"},"Register",-1);function B(t,e,n,l,r,o){const s=m("RegisterForm");return p(),d("div",R,[S,u(s)])}var V=c(P,[["render",B]]);export{V as default};