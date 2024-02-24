import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, type UserCredential } from 'firebase/auth';
import { useAccessToken } from '../composables/accesstoken';
import { useUserStore } from '../composables/user';

type Auth = {
	signIn: () => Promise<string>;
	signOut: () => Promise<void>;
};

export const useAuth = (): Auth => {
	const { setUser, clearUser } = useUserStore();
	const { setToken, clearToken } = useAccessToken();
	const { clearLink } = useUserLink();

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
		const auth = getAuth();
		await firebaseSignOut(auth)
			.then(() => {
				clearUser();
				clearToken();
				clearLink();
				navigateTo('/about');
			})
			.catch((error) => {
				alert(error.message);
			});
	};

	return {
		signIn,
		signOut,
	};
};
