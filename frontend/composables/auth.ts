import { getAuth, GoogleAuthProvider, signInWithPopup, signOut as firebaseSignOut, type UserCredential } from 'firebase/auth';
import { useAccessToken } from '../composables/accesstoken';
import { useRefreshToken } from '../composables/refreshtoken';
import { useUserStore } from '../composables/user';

type Auth = {
	signIn: () => Promise<void>;
	signOut: () => Promise<void>;
	refresh: () => Promise<void>;
};

export const useAuth = (): Auth => {
	const { setUser, clearUser } = useUserStore();
	const { setToken, clearToken } = useAccessToken();
	const { setRefresh, clearRefresh } = useRefreshToken();

	const signIn = async (): Promise<void> => {
		const auth = getAuth();
		const provider = new GoogleAuthProvider();
		await signInWithPopup(auth, provider)
			.then(async (result: UserCredential) => {
				setUser(result.user);
				setToken(await result.user.getIdToken());
				setRefresh(result.user.refreshToken);
			})
			.catch((error) => {
				alert('統合認証システムに接続できません');
			});
	};

	const signOut = async (): Promise<void> => {
		const auth = getAuth();
		await firebaseSignOut(auth)
			.then(() => {
				clearUser();
				clearToken();
				clearRefresh();
				navigateTo('/login');
			})
			.catch((error) => {
				alert(error.message);
			});
	};

	const refresh = async (): Promise<void> => {
		const config = useRuntimeConfig();
		const { user } = useUserStore();
		const { data, error } = await useFetch(`https://securetoken.googleapis.com/v1/token?key=${config.public.FIREBASE_API_KEY}`, {
			params: {
				grant_type: 'refresh_token',
				refresh_token: user?.refreshToken,
			},
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
			},
		});
		if (!data.value) {
			console.log(error.value?.data);
			signOut();
		} else {
			console.log(data.value);
			setToken((data.value as any).access_token);
			setRefresh((data.value as any).refresh_token);
			navigateTo('/');
		}
	};

	return {
		signIn,
		signOut,
		refresh,
	};
};
