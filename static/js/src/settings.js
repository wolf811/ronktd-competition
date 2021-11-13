//GLOBAL SETTINGS FOR AXIOS AND VUE
import Vue from "vue";
//import AsyncComputed from "vue-async-computed";
const axios = require("axios").default;
import Cookies from "js-cookie";
//import htmx from 'htmx.org';
let CSRF_TOKEN = localStorage.getItem("csrf_token");
//debugger;
//console.log("csrf_token:", CSRF_TOKEN);
var GLOBAL_CSRF_TOKEN = CSRF_TOKEN;

// console.log('HELLO VUE', Vue)
var APP_LOG_LIFECYCLE_EVENTS = true;

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

//let CONFIRM = false;

// use AXIOS instead of default $http of VUE
Vue.prototype.$http = axios;
Vue.options.delimiters = ["[[", "]]"];
if (!Cookies.get("csrftoken")) {
	Cookies.set("csrftoken", GLOBAL_CSRF_TOKEN, { expires: 7 });
}

//fckng async computed settings
//Vue.use(AsyncComputed);

//htmx.org configuration

//htmx logger to console for debugging
// htmx.logAll();

// console.log('HELLO AXIOS', axios)
export const EventBus = new Vue();
