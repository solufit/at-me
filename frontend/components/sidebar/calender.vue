<script setup lang="ts">
	import { Calendar, DatePicker } from 'v-calendar';
	import 'v-calendar/style.css';
	const attributes = ref([
		{
			// Boolean
			dot: true,
			dates: [new Date(2024, 1, 1), new Date(2024, 1, 10), new Date(2024, 1, 22)],
		},
		{
			// String
			dot: 'red',
			dates: [new Date(2024, 1, 1), new Date(2024, 1, 10), new Date(2024, 1, 22)],
		},
		{
			// Object
			dot: {
				style: {
					backgroundColor: 'brown',
				},
			},
			dates: [new Date(2024, 1, 1), new Date(2024, 1, 10), new Date(2024, 1, 22)],
		},
	]);
</script>
<template>
	<div>
		<Calendar :initial-page="{ month: 2, year: 2024 }" :attributes="attributes" />
	</div>
</template>
