import type { PartsTasks } from '#build/components';
<script setup lang="ts">
	import type { Task } from '~/types/task';
	import { Calendar, DatePicker } from 'v-calendar';
	const props = defineProps<{
		tasks: Task[];
	}>();
	const { token } = useAccessToken();
	const config = useRuntimeConfig();
	const task_click = async (id: string) => {
		const { data, error } = await useFetch(`${config.public.API_ENDPOINT}/v1/tasks/complite`, {
			method: 'get',
			headers: {
				Authorization: `Bearer ${token}`,
			},
			params: {
				taskid: id,
			},
		});
	};
</script>
<template>
	<div>
		<div class="p-2" v-if="tasks.length > 0" v-for="task in tasks">
			<div class="border-2 rounded-md p-3 cursor-pointer w-full">
				<div class="flex w-full" :class="{ 'opacity-25': task.completed }">
					<div class="w-20" v-if="task.provider == 'at-me'">
						<input type="radio" :name="task.id" @change="task_click(task.id)" class="radio radio-primary" :checked="task.completed" />
					</div>
					<div class="w-20 flex items-center justify-center" v-if="task.provider == 'github'">
						<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
							<path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
								fill="#24292f"
							/>
						</svg>
					</div>
					<div class="w-full px-3">
						<div class="font-bold">
							{{ task.title }} <span class="text-sm font-normal ml-4" v-if="task.provider == 'at-me'">{{ task.duringtime }} mins</span>
						</div>
						<div class="p-1">{{ task.note }}</div>
					</div>
					<div class="w-9" v-if="task.provider == 'at-me'">
						<div class="dropdown dropdown-end absolute">
							<button tabindex="0" role="button" class="bg-neutral" aria-label="スケジュールの変更">
								<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-primary">
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5m-9-6h.008v.008H12v-.008ZM12 15h.008v.008H12V15Zm0 2.25h.008v.008H12v-.008ZM9.75 15h.008v.008H9.75V15Zm0 2.25h.008v.008H9.75v-.008ZM7.5 15h.008v.008H7.5V15Zm0 2.25h.008v.008H7.5v-.008Zm6.75-4.5h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V15Zm0 2.25h.008v.008h-.008v-.008Zm2.25-4.5h.008v.008H16.5v-.008Zm0 2.25h.008v.008H16.5V15Z"
									/>
								</svg>
							</button>
							<div class="dropdown-content z-[1] menu p-2 shadow border-2 border-primary bg-base-100 rounded-box">
								<div class="mb-2 flex items-center justify-center text-center font-semibold text-md">リスケジュール</div>
								<DatePicker :min-date="new Date()" :value="task.due" mode="dateTime" color="green" borderless />
							</div>
						</div>
					</div>
				</div>
			</div>
			<dialog :id="task.id" class="modal">
				<div class="modal-box">
					<h3 class="font-bold text-lg">Hello!</h3>
					<p class="py-4">Press ESC key or click outside to close</p>
				</div>
				<form method="dialog" class="modal-backdrop">
					<button>close</button>
				</form>
			</dialog>
		</div>
		<div v-else class="flex items-center justify-center p-12">
			<div>
				<div class="text-2xl font-extrabold text-center mb-6">Zero Task！</div>
				<div><NuxtImg src="/images/stackzero.png" class="h-96 w-96"></NuxtImg></div>
			</div>
		</div>
	</div>
</template>
