import { type User as firebaseUser } from 'firebase/auth';
import { useUserStore } from '@/stores/user';

type User = {
	user: Ref<firebaseUser | null | undefined>;
	setUser: (newUser: firebaseUser) => void;
	clearUser: () => void;
};

export const useUser = (): User => {
	const userStore = useUserStore();
	const { user } = storeToRefs(userStore);
	const { setUser, clearUser } = userStore;

	return {
		user,
		setUser,
		clearUser,
	};
};
