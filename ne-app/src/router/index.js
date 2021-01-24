import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
<<<<<<< HEAD
import Now from '../views/Now.vue'
import Factories from '../views/Factories.vue'
=======
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd

Vue.use(VueRouter)

const routes = [
  {
<<<<<<< HEAD
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/now',
    name: 'now',
    component: Now
  },
  {
    path: '/factories',
    name: 'factories',
    component: Factories
=======
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
>>>>>>> a96517be5f9a608192f6efc6fc960457dc596edd
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
