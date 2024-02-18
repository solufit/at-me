<script setup lang="ts">
	import type { Task } from '~/types/task';
	import Tasks from '~/components/uiparts/tasks.vue';
	const tasks: Task[] = [
		{
			id: '',
			title: 'test',
			description: 'test',
			schduletime: new Date(),
			deadtime: new Date(),
			project: '',
			projectId: '',
			duringtime: 10,
		},
	];
</script>
<template>
	<div>
		<h1 class="font-bold text-xl">近日中に予定されているタスク</h1>
		<div class="mt-6 p-4">
			<div>
				<div class="font-semibold text-lg">明日</div>
				<div class="p-4">
					<Tasks :tasks="tasks" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">火曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">水曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">木曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">金曜日</div>
				<div class="p-4">
					<Tasks :tasks="tasks" />
				</div>
			</div>
			<div>
				<div class="font-semibold text-lg">土曜日</div>
				<div class="p-4">予定されているタスクはありません</div>
			</div>
		</div>
	</div>
</template>
