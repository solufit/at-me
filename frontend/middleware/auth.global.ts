import type { RouteLocationNormalized } from 'vue-router';
import { useAccessToken } from '../composables/accesstoken';
import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app';
export default defineNuxtRouteMiddleware(async (to: RouteLocationNormalized) => {
	if (process.server) {
		return;
	}
	if (to.path == '/auth/login') return;
	const { token } = useAccessToken();
	if (!token) {
		return await navigateTo('/auth/login');
	}
});
