<script setup lang="ts">
	useHead({
		title: '締め切り | @me',
	});
	import type { Task } from '~/types/task';
	import Tasks from '~/components/uiparts/tasks.vue';
	// defind variable
	const tasks = ref<[Task[]]>([[]]);
	const api_endpoint = process.env.NUXT_API_ENDPOINT;
	// api requests
	async () => {
		const { data, error } = await useFetch(`https://${api_endpoint}/tasks/deadline`);
		tasks.value = data.value as [Task[]];
	};
</script>
<template>
	<div>
		<h1 class="font-bold text-xl">締め切りの近いタスク</h1>
		<div class="mt-6 p-4">
			<div>
				<div class="font-semibold text-lg">明日</div>
				<div class="p-4">
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">火曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">水曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">木曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">金曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks[0]" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">土曜日</div>
				<div class="p-4">この日が締め切りのタスクはありません</div>
			</div>
		</div>
	</div>
</template>
