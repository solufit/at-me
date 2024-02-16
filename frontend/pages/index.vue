<script setup lang="ts">
	import Timeline from '~/components/timeline/timeline.vue';
	import type { Schdule } from '~/types/schdule';
	const schs: Schdule[] = [
		{
			starttime: '2024-02-20 11:44',
			endtime: '2024-02-20 11:54',
			duringtime: 10,
			title: 'test',
			description: 'test',
		},
		{
			starttime: '2024-02-20 11:44',
			endtime: '2024-02-20 11:54',
			duringtime: 10,
			title: 'test',
			description: 'test',
		},
		{
			starttime: '2024-02-20 11:44',
			endtime: '2024-02-20 11:54',
			duringtime: 10,
			title: 'test',
			description: 'test',
		},
		{
			starttime: '2024-02-20 11:44',
			endtime: '2024-02-20 11:54',
			duringtime: 10,
			title: 'test',
			description: 'test',
		},
	];
</script>
<template>
	<div>
		<Timeline :schdules="schs" />
	</div>
</template>
