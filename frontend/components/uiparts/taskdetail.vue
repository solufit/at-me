<script setup lang="ts">
	import { Calendar, DatePicker } from 'v-calendar';
	import 'v-calendar/style.css';
	import type { Task } from '~/types/task';
	interface Props {
		task: Task;
	}
	const props = withDefaults(defineProps<Props>(), {
		task: {
			id: '',
			title: '',
			deadtime: new Date(),
			description: '',
			project: '',
			projectId: '',
			schduletime: new Date(),
			duringtime: 30,
		},
	});
	const duetime = ref(props.task.schduletime);
	const deadtime = ref(props.task.deadtime);
	const title = ref(props.task.title);
	const description = ref(props.task.description);
	const duringtime = ref(props.task.duringtime);
</script>
<template>
	<div class="h-full">
		<label class="hidden" for="name">タスク名</label>
		<input type="text" name="name" placeholder="タスク名" class="input w-full font-bold" v-model="title" />
		<div class="py-4">
			<div class="flex mb-4">
				<div class="w-1/2">
					<div class="dropdown">
						<div tabindex="0" role="button" class="m-1 btn btn-xs">予定日 {{ $formatDate(duetime) }}</div>
						<div tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box"><DatePicker :min-date="new Date()" v-model="duetime" mode="dateTime" /></div>
					</div>
				</div>
				<div class="w-1/2">
					<div class="dropdown dropdown-end">
						<div tabindex="0" role="button" class="m-1 btn btn-xs text-red-800">締め切り日 {{ $formatDate(deadtime) }}</div>
						<div tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box"></div>
					</div>
				</div>
			</div>
			<div class="flex flex-wrap mb-4">
				<div class="w-full md:w-4/5">
					<label class="hidden" for="duringtime">タスクにかかる時間</label>
					<input type="range" name="duringtime" min="0" max="120" class="range range-primary range-sm" step="15" v-model="duringtime" />
					<div class="w-full flex justify-between text-xs px-2">
						<span>0</span>
						<span>30</span>
						<span>60</span>
						<span>90</span>
						<span>120</span>
					</div>
				</div>
				<div class="w-full md:w-1/5 pt-3 md:pl-6 text-xs">かかる時間: {{ duringtime }}分</div>
			</div>
			<div class="mb-6">
				<label class="hidden" for="memo">タスクの内容</label>
				<textarea class="textarea w-full h-96" name="memo" placeholder="タスクの詳細" v-model="description">{{ task }}</textarea>
			</div>
			<div class="text-end">
				<div class="btn btn-primary btn-md">
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M9 3.75H6.912a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H15M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859M12 3v8.25m0 0-3-3m3 3 3-3"
						/>
					</svg>
					<span>保存</span>
				</div>
			</div>
		</div>
	</div>
</template>
