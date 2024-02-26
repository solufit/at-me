<script setup lang="ts">
	import Timeline from '~/components/sidebar/timeline.vue';
	import Tasks from '~/components/uiparts/tasks.vue';
	import type { Schdule } from '~/types/schdule';
	import type { Task } from '~/types/task';
	const route = useRoute();
	const targetdate = route.params.date as string;
	useHead({
		title: `${targetdate} | @me`,
	});
	const tfdate = new Date(targetdate);
	// defind variable
	const schs = ref<Schdule[]>([]);
	const tasks = ref<Task[]>([]);
	const api_endpoint = process.env.NUXT_API_ENDPOINT;
	const config = useRuntimeConfig();
	const { userLink } = useUserLink();
	const { token } = useAccessToken();
	// api requests
	const get_schs = async () => {
		const { data, error } = await useFetch(`${config.public.API_ENDPOINT}/v1/google/calender?date=${targetdate}&userlink=${userLink}`, {
			method: 'get',
			headers: {
				Authorization: `Bearer ${token}`,
			},
		});
		if (error.value?.data.detail == 'Not authenticated') {
			navigateTo('');
		} else {
			schs.value = data.value as Schdule[];
		}
	};
	const get_tasks = async () => {
		const { data, error } = await useFetch(`${config.public.API_ENDPOINT}/v1/tasks?date=${targetdate}`, {
			method: 'get',
			headers: {
				Authorization: `Bearer ${token}`,
			},
		});
		if (error.value?.data.detail == 'Not authenticated') {
			navigateTo('/');
		} else {
			tasks.value = data.value as Task[];
		}
	};
	get_schs();
	get_tasks();
	const tabs = ref('calender');
	const change_tab = (tab: string) => {
		tabs.value = tab;
	};
</script>
<template>
	<div>
		<div class="flex text-center justify-center items-center h-14">
			<div class="w-4/5 md:w-5/6">
				<span class="text-center justify-center font-semibold mt-5 text-lg md:text-xl"
					>{{ tfdate.getFullYear() }} / {{ tfdate.getMonth() + 1 }} / {{ tfdate.getDate() }} ( {{ ['日', '月', '火', '水', '木', '金', '土'][tfdate.getDay()] }} )</span
				>
			</div>
			<NuxtLink class="w-1/5 md:w-1/6 text-center btn btn-outline btn-md btn-primary" to="/">TODAY</NuxtLink>
		</div>
		<div role="tablist" class="md:hidden tabs tabs-boxed w-32">
			<button role="tab" class="tab" :class="{ 'tab-active': tabs == 'calender' }" @click="change_tab('calender')">
				<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5"
					/>
				</svg>
			</button>
			<button role="tab" class="tab" :class="{ 'tab-active': tabs == 'tasks' }" @click="change_tab('tasks')">
				<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M6.429 9.75 2.25 12l4.179 2.25m0-4.5 5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0 4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0-5.571 3-5.571-3"
					/>
				</svg>
			</button>
		</div>
		<div class="p-5 mt-5 md:mt-0">
			<div class="md:flex w-full">
				<div class="md:block md:w-1/2" :class="{ hidden: tabs != 'calender' }">
					<Timeline :schdules="schs" />
				</div>
				<div class="md:block md:w-1/2" :class="{ hidden: tabs != 'tasks' }">
					<Tasks :tasks="tasks" />
				</div>
			</div>
		</div>
	</div>
</template>
