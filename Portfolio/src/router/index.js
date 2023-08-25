import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import Home from '../views/Home/Home.vue'
import About from '../views/About/About.vue'
import Contact from '../views/Contact/Contact.vue'
import Blog from '../views/Blog/Blog.vue'
import Portfolio from '../views/Portfolio/Portfolio.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      compontent: About
    },
     {
      path: '/contact',
      name: 'contact',
      compontent: Contact
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      compontent: Portfolio
    },
     {
      path: '/blog',
      name: 'blog',
      compontent: Blog
    },
  ]
})

export default router
