import { ref } from 'vue';
import { defineStore } from 'pinia';
import { type User } from '../types/user';

export const useUserStore = defineStore(
	'user',
	() => {
		const user = ref<User | null>();
		function setUser(newuser: User) {
			user.value = newuser;
		}
		function clearUser() {
			user.value = null;
		}
		return { user, setUser, clearUser };
	},
	{
		persist: {
			storage: persistedState.localStorage,
		},
	}
);
