<script setup lang="ts">
	import { Calendar, DatePicker } from 'v-calendar';
	import 'v-calendar/style.css';
	const router = useRouter();
	const { token } = useAccessToken();
	const config = useRuntimeConfig();
	const { data, error } = await useFetch(`${config.public.API_ENDPOINT}/v1/calenders/dot`, {
		method: 'get',
		headers: {
			Authorization: `Bearer ${token}`,
		},
	});
	const attributes = ref([
		{
			// Boolean
			dot: 'green',
			dates: (data.value as any).schedules,
		},
		{
			// String
			dot: 'orange',
			dates: (data.value as any).tasks,
		},
	]);
	const movedate = (value: any) => {
		router.push(`/calender/${value.id}`);
	};
</script>
<template>
	<div>
		<Calendar :initial-page="{ month: 2, year: 2024 }" :attributes="attributes" @dayclick="movedate" />
	</div>
</template>
