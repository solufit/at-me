<script setup lang="ts">
	import type { Schdule } from '~/types/schdule';
	const pps = defineProps<{
		schdules: Schdule[];
	}>();
</script>
<template>
	<ol class="relative border-s border-gray-200 dark:border-gray-700">
		<li class="mb-10 ms-6" v-for="sch in schdules">
			<div :class="{ 'opacity-25': new Date() > new Date(sch.endtime) }">
				<span class="absolute flex items-center justify-center w-7 h-7 bg-neutral rounded-full -start-3 ring-9 ring-white dark:ring-gray-900 dark:bg-blue-900">
					<svg class="w-2.5 h-2.5 text-primary dark:text-blue-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
						<path
							d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"
						/>
					</svg>
				</span>
				<h3 class="flex items-center mb-1 text-lg font-semibold text-gray-900 dark:text-white">
					{{ sch.title }}
					<span
						class="text-primary text-sm font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300 ms-3"
						v-if="new Date() > new Date(sch.starttime) && new Date() < new Date(sch.endtime)"
						>NOW</span
					>
				</h3>
				<time class="block mb-2 text-sm font-normal leading-none text-gray-400 dark:text-gray-500"
					>{{ sch.starttime.split('T')[1].split(':')[0] }}:{{ sch.starttime.split('T')[1].split(':')[1] }} - {{ sch.endtime?.split('T')[1].split(':')[0] }}:{{
						sch.endtime?.split('T')[1].split(':')[1]
					}}
					( {{ sch.duringtime }} mins )</time
				>
				<p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">
					{{ sch.description }}
				</p>
			</div>
		</li>
	</ol>
</template>
