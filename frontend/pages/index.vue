<script setup lang="ts">
	useHead({
		title: 'Today | @me',
	});
	import Timeline from '~/components/sidebar/timeline.vue';
	import Tasks from '~/components/uiparts/tasks.vue';
	import type { Schdule } from '~/types/schdule';
	import type { Task } from '~/types/task';
	import { useAccessToken } from '../composables/accesstoken';
	const { token } = useAccessToken();
	const { signOut } = useAuth();
	const { setPending } = usePending();
	const config = useRuntimeConfig();
	// defind variable
	const schs = ref<Schdule[] | null>([]);
	const tasks = ref<Task[]>([]);
	// defind today
	const date = new Date();
	const yyyy = String(date.getFullYear());
	const mm = String(date.getMonth() + 1).padStart(2, '0');
	const dd = String(date.getDate()).padStart(2, '0');
	const today = `${yyyy}-${mm}-${dd}`;
	const calendar_pending = ref();
	const tasks_pending = ref();
	// api requests
	const get_schs = async () => {
		const { data, error, pending } = await useFetch(`${config.public.API_ENDPOINT}/v1/calendar`, {
			method: 'get',
			params: {
				token: token,
				date: today,
			},
		});
		console.log(error.value);
		setPending(pending.value);
		if (error.value?.data.detail === 401) {
			signOut();
			window.location.href = '/about';
		} else {
			schs.value = data.value as Schdule[];
		}
	};
	const get_tasks = async () => {
		const { data, error, pending } = await useFetch(`${config.public.API_ENDPOINT}/v1/tasks`, {
			method: 'get',
			params: {
				token: token,
				date: today,
			},
		});
		setPending(pending.value);
		if (error.value?.statusCode === 401) {
			schs.value = null;
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
	const task_rc: Task[] = [
		{
			id: '',
			title: 'Windows Updateをする',
			note: '',
			updated: new Date(),
			selfLink: 'string',
			parent: 'string',
			position: 'string',
			status: 'string',
			due: new Date(),
			duringtime: 30,
			completed: false,
			deleted: false,
			hidden: false,
			provider: 'at-me',
			parent_id: '',
		},
	];
</script>
<template>
	<div>
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
				<div class="md:block md:w-1/2" :class="{ hidden: tabs !== 'calender' }">
					<div v-if="schs !== null">
						<div v-if="schs?.length == 0" class="flex items-center justify-center font-semibold text-2xl mt-10">予定はありません！</div>
						<div v-else><Timeline :schdules="schs" /></div>
					</div>
					<div v-else class="flex items-center justify-center">
						<div>
							<div class="text-3xl text-center text-red-600">連携に失敗しました</div>
							<div class="text-lg text-center my-4">一度、カレンダーとして連携するサービスのアカウント連携を解除し再度認証を行ってください</div>
							<NuxtImg src="/images/error.png" class="h-96 w-96 flex items-center justify-center" />
						</div>
					</div>
				</div>
				<div class="md:block md:w-1/2" :class="{ hidden: tabs !== 'tasks' }">
					<div v-if="tasks !== null">
						<!--
					<div class="shadow-md shadow-lime-200 border-2 border-lime-200 p-3 rounded-md m-2 mb-6 font-semibold">
						<div><span>AI Recommend</span><span class="ml-2">for 30 mins</span></div>
						<div class="mt-4">
							<Tasks :tasks="task_rc" />
						</div>
					</div>
					-->
						<Tasks :tasks="tasks" />
					</div>
					<div v-else class="flex items-center justify-center">
						<div>
							<div class="text-3xl text-center text-red-600">連携に失敗しました</div>
							<div class="text-lg text-center my-4">一度、タスクとして連携するサービスのアカウント連携を解除し再度認証を行ってください</div>
							<NuxtImg src="/images/error.png" class="h-96 w-96 flex items-center justify-center" />
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
