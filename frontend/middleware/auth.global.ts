import type { RouteLocationNormalized } from 'vue-router';
import { useAccessToken } from '../composables/accesstoken';
import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app';
import { type User } from '../types/user';
export default defineNuxtRouteMiddleware(async (to: RouteLocationNormalized) => {
	if (process.server) {
		return;
	}
	if (to.path == '/auth/callback') return;
	if (to.path == '/auth/login') return;
	const { token } = useAccessToken();
	if (!token) {
		return await navigateTo('/auth/login');
	} else {
		const { user, setUser } = useUserStore();
		const config = useRuntimeConfig();
		const { data, error } = await useFetch(`${config.public.API_ENDPOINT}/v1/auth/info`, {
			method: 'get',
			headers: {
				Authorization: `Bearer ${token}`,
			},
		});
		setUser(data.value as User);
	}
});
