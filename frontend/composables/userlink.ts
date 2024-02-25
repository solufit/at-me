import { ref } from 'vue';
import { defineStore } from 'pinia';
export const useUserLink = defineStore(
	'userlink',
	() => {
		const userLink = ref<string | null>('');
		function setLink(newuser: string) {
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
