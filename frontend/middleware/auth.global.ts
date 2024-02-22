import type { RouteLocationNormalized } from 'vue-router';
import { useUser } from '../composables/user';
import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app';
export default defineNuxtRouteMiddleware(async (to: RouteLocationNormalized) => {
	if (process.server) {
		return;
	}
	if (to.path == '/auth/login') return;

	const { user } = useUser();

	if (!user.value) {
		console.log('not authenticated');
		return await navigateTo('/auth/login');
	}
});
