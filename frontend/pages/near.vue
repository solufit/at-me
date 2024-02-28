<script setup lang="ts">
	useHead({
		title: '近日予定 | @me',
	});
	import type { Task } from '~/types/task';
	import Tasks from '~/components/uiparts/tasks.vue';
	// defind variable
	const tasks = ref<[Task[]]>([[]]);
	const api_endpoint = process.env.NUXT_API_ENDPOINT;
	// api requests
	async () => {
		const { data, error } = await useFetch(`https://${api_endpoint}/v1/tasks/near`);
		tasks.value = data.value as [Task[]];
	};
</script>
<template>
	<div>
		<h1 class="font-bold text-xl">近日中に予定されているタスク</h1>
		<div class="mt-6 p-4">
			<div>
				<div class="font-semibold text-lg">明日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">火曜日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">水曜日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">木曜日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">金曜日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">土曜日</div>
				<div v-if="tasks[0].length === 0 || tasks[0] === null" class="p-4 font-semibold px-6">予定されているタスクはありません</div>
				<div class="p-4" v-else>
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
		</div>
	</div>
</template>
