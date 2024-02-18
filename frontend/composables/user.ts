import { type User as firebaseUser } from 'firebase/auth';

type User = {
	user: Ref<firebaseUser | null>;
	setUser: (newUser: firebaseUser | null) => void;
};

export const useUser = (): User => {
	const user = useState<firebaseUser | null>('user', () => null);

	const setUser = (newUser: firebaseUser | null) => {
		user.value = newUser;
	};

	return {
		user,
		setUser,
	};
};
