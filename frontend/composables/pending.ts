import { ref } from 'vue';
import { defineStore } from 'pinia';
export const usePending = defineStore('pendingState', () => {
	const pendingState = ref<boolean>(false);
	function setPending(state: boolean) {
		pendingState.value = state;
	}
	return { pendingState, setPending };
});
