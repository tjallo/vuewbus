import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './views/Dashboard'
import Render from './views/Render'
import Upload from './views/Upload'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: Dashboard
        },
        {
            path: '/render',
            name: 'render',
            component: Render
        },
        {
            path: '/upload',
            name: 'dashboard',
            component: Upload
        },
    ]
});