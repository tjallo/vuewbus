import Vue from 'vue'
import Router from 'vue-router'
import Players from './views/Players'
import Startgame from './views/Startgame'
import Round1 from './views/Round1'
import Round2 from './views/Round2'
import Round3 from './views/Round3'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'players',
            component: Players
        },
        {
            path: '/startgame',
            name: 'startgame',
            component: Startgame
        },
        {
            path: '/round1',
            name: 'round1',
            component: Round1
        },
        {
            path: '/round2',
            name: 'round2',
            component: Round2
        },
        {
            path: '/round3',
            name: 'round3',
            component: Round3
        },
    ]
});