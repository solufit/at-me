import type { RouteLocationNormalized } from 'vue-router';
import { useAccessToken } from '../composables/accesstoken';
import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app';
import { type User } from '../types/user';
export default defineNuxtRouteMiddleware(async (to: RouteLocationNormalized) => {
	if (process.server) {
		return;
	}
	if (to.path == '/auth/callback') return;
	if (to.path == '/about') return;
	const { token } = useAccessToken();
	if (!token) {
		return await navigateTo('/about');
	} else {
		const { user, setUser } = useUserStore();
		const { signOut } = useAuth();
		const config = useRuntimeConfig();
		const { setPending } = usePending();
		const { data, error, pending } = await useFetch(`${config.public.AUTH_API}/user/profile`, {
			method: 'get',
			params: {
				token: token,
			},
		});
		setPending(pending.value);
		if (error.value) {
			await signOut();
			return await navigateTo('/about');
		}
		setUser(data.value as User);
	}
});
