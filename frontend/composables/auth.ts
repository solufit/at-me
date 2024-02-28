import { useAccessToken } from '../composables/accesstoken';
import { useUserStore } from '../composables/user';

type Auth = {
	signIn: () => Promise<string>;
	signOut: () => Promise<void>;
};

export const useAuth = (): Auth => {
	const { setUser, clearUser } = useUserStore();
	const { setToken, clearToken } = useAccessToken();

	const signIn = async (): Promise<string> => {
		const config = useRuntimeConfig();
		const { data, error } = await useFetch(`${config.public.AUTH_API}/oauth2/login`, {
			params: {
				redirect: config.public.AUTH_REDIRECT,
			},
		});
		return data.value as string;
		//setUser(result.user);
		//setToken(await result.user.getIdToken());
		//setRefresh(result.user.refreshToken);
	};

	const signOut = async (): Promise<void> => {
		const { token } = useAccessToken();
		const config = useRuntimeConfig();
		if (token) {
			const { data, error } = useFetch(`${config.public.AUTH_API}/session/invalid`, {
				method: 'get',
				params: {
					token: token,
				},
			});
		}
		clearUser();
		clearToken();
		navigateTo('/about');
	};

	return {
		signIn,
		signOut,
	};
};
