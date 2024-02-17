import dayjs from 'dayjs';
import { defineNuxtPlugin } from '#app';

export default defineNuxtPlugin((nuxtApp) => {
	nuxtApp.provide('formatDate', (value: any) => {
		const date = dayjs(value);
		return date.format('MM/DD HH:mm');
	});
});
