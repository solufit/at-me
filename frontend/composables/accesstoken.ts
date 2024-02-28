import { ref } from 'vue';
import { defineStore } from 'pinia';
export const useAccessToken = defineStore(
	'token',
	() => {
		const token = ref<string | null>(null);
		function setToken(newuser: string) {
			token.value = newuser;
		}
		function clearToken() {
			token.value = null;
		}
		return { token, setToken, clearToken };
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
