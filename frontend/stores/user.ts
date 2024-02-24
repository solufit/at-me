import { ref, computed } from 'vue';
import { defineStore, storeToRefs } from 'pinia';
import { type User as firebaseUser } from 'firebase/auth';

export const useUserStore = defineStore(
	'user',
	() => {
		const user = ref<firebaseUser | null>();
		function setUser(newuser: firebaseUser) {
			user.value = newuser;
		}
		function clearUser() {
			user.value = null;
		}
		return { user, setUser, clearUser };
	},
	{
		persist: true,
	}
);