import type { PartsTasks } from '#build/components';
<script setup lang="ts">
	import type { Task } from '~/types/task';
	import { Calendar, DatePicker } from 'v-calendar';
	import MarkdownIt from 'markdown-it';
	const mdit: MarkdownIt = new MarkdownIt({
		html: true,
	});
	const props = defineProps<{
		tasks: Task[];
	}>();
	const { token } = useAccessToken();
	const config = useRuntimeConfig();
	const task_click = async (id: string) => {
		const { data, error, pending } = await useFetch(`${config.public.API_ENDPOINT}/v1/tasks/complite`, {
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
					<div class="w-20" v-if="task.provider == 'atme'">
						<input type="radio" :name="task.id" @change="task_click(task.id)" class="radio radio-primary" :checked="task.completed" />
					</div>
					<div class="w-20 flex items-center justify-center" v-if="task.provider == 'GithubIssues'">
						<NuxtImg src="/images/logo/github.svg" class="h-10 w-10" />
					</div>
					<div class="w-full max-w-xl px-3">
						<details tabindex="0" class="collapse">
							<summary class="collapse-title p-0">
								<div class="font-bold ml-2">
									{{ task.title }}
								</div>
								<div class="flex gap-4 my-1 text-sm font-normal ml-3">
									<div v-if="task.provider == 'atme'">{{ task.duringtime }} mins</div>
									<div>{{ task.parent }}</div>
								</div>
							</summary>
							<div class="collapse-content">
								<div class="p-1 mt-2 max-w-md"><div v-html="mdit.render(task.note)"></div></div>
							</div>
						</details>
					</div>
					<div class="w-9 flex items-center justify-center">
						<div v-if="task.provider == 'at-me'">
							<div class="dropdown dropdown-end">
								<button tabindex="0" role="button" class="" aria-label="スケジュールの変更">
									<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-primary">
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
						<div v-else>
							<a target="_blank" :href="task.selfLink">
								<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5 text-primary">
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"
									/>
								</svg>
							</a>
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
