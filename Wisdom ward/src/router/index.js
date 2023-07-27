import {createRouter, createWebHashHistory} from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/dashboard'
    }, {
        path: "/",
        component: Home,
        children: [
            {
                path: "/dashboard",
                meta: {
                    title: '系统首页'
                },
                component: () => import ( /* webpackChunkName: "dashboard" */ "../views/Dashboard.vue")
            },
            {
                path: "/information",
                meta: {
                    title: '信息管理'
                },
                component: () => import ( /* webpackChunkName: "table" */ "../views/BaseTable.vue")
            },
            {
                path: "/control",
                meta: {
                    title: '病房控制'
                },
                component: () => import ( /* webpackChunkName: "charts" */ "../views/Control.vue")
            },
            {
                path: "/warning",
                meta: {
                    title: '系统提示'
                },
                component: () => import ( /* webpackChunkName: "tabs" */ "../views/Tabs.vue")
            },
            {
                path: '/user',
                meta: {
                    title: '关于我们'
                },
                component: () => import (/* webpackChunkName: "user" */ '../views/User.vue')
            },
            {
                path: 'test',
                component: () => import (/* webpackChunkName: "user" */ '../views/test.vue')
            },
            {
                path: 'video',
                component:()=> import( /* webpackChunkName: "video" */ '../views/video.vue')
            }
        ]
    }, {
        path: "/login",
        name: "Login",
        meta: {
            title: '登录'
        },
        component: () => import ( /* webpackChunkName: "login" */ "../views/Login.vue")
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | Wisdom ward`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permission) {
        // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
        role === 'admin'
            ? next()
            : next('/dashboard');
    } else {
        next();
    }
});

export default router;