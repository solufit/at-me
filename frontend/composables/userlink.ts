import { ref } from 'vue';
import { defineStore } from 'pinia';
type UserLink = {
	linkcode: string;
	provider: string;
};
export const useUserLink = defineStore(
	'userlink',
	() => {
		const userLink = ref<UserLink | null>(null);
		function setLink(newuser: UserLink) {
			userLink.value = newuser;
		}
		function clearLink() {
			userLink.value = null;
		}
		return { userLink, setLink, clearLink };
	},
	{
		persist: {
			storage: persistedState.cookiesWithOptions({
				sameSite: 'strict',
				maxAge: 604800,
			}),
		},
	}
);
