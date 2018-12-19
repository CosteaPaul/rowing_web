// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import Router from 'vue-router';
import iView from 'iview';
//import cv from 'opencv.js';
import 'iview/dist/styles/iview.css';
import Login from './components/Login';
import Boat_avatar from './components/Boat_avatar';
import Erg_analyzer from './components/Erg_analyzer';

Vue.config.productionTip = false
Vue.use(iView);
//Vue.use(cv);
Vue.use(Router);

const routes = [
  { path: '/login', name: "login", component : Login },
  { path: '/home', component: Boat_avatar},
  { path: '/erg', name: "erg", component: Erg_analyzer},
  { path: '/', redirect: {
                name: "erg"
            }}
];

const router = new Router({routes: routes});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})
