import { ref } from 'vue';
import { defineStore } from 'pinia';
export const useRefreshToken = defineStore(
	'refresh',
	() => {
		const refresh = ref<string | null>('');
		function setRefresh(newuser: string) {
			refresh.value = newuser;
		}
		function clearRefresh() {
			refresh.value = null;
		}
		return { refresh, setRefresh, clearRefresh };
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
