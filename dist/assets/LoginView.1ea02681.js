import{E as _}from"./Errors.395958ca.js";import{_ as c,r as l,o as i,c as m,d,w as u,b as f,a as g}from"./index.b022a2b4.js";const h={components:{Errors:_},data(){return{csrf_token:"",errors:[]}},methods:{login(){const n=this;let t=document.getElementById("loginForm"),a=new FormData(t);fetch("http://192.168.100.199:8080/api/auth/login",{method:"POST",body:a}).then(async e=>{const o=await e.json();if(e.status==200){const r=o.token,s=o.user;localStorage.setItem("jwt",r),localStorage.setItem("user",JSON.stringify(s)),this.$router.push("/explore")}else n.errors=o.message}).catch(e=>{console.log(e)})}},created(){}},w=f('<div class="mb-3"><label class="form-label" for="username">Username</label><input type="text" name="username" id="username" class="form-control" placeholder="Enter your Username"></div><div class="mb-3"><label class="form-label" for="password">Password</label><input type="text" name="password" id="password" class="form-control" placeholder="Enter your Password"></div><button class="btn btn-warning text-white w-100">Login</button>',3);function b(n,t,a,e,o,r){const s=l("Errors");return i(),m("form",{onSubmit:t[0]||(t[0]=u((...p)=>r.login&&r.login(...p),["prevent"])),id:"loginForm",method:"POST",enctype:"multipart/form-data"},[w,d(s,{errors:o.errors},null,8,["errors"])],32)}var v=c(h,[["render",b]]);const x={data(){return{}},components:{LoginForm:v}},y={class:"container"},$=g("h2",{class:"text-warning text-center fw-bold"},"Login",-1);function E(n,t,a,e,o,r){const s=l("LoginForm");return i(),m("div",y,[$,d(s)])}var S=c(x,[["render",E]]);export{S as default};