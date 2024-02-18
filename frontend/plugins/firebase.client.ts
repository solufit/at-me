import { initializeApp } from 'firebase/app';
import { defineNuxtPlugin } from '#app';

export default defineNuxtPlugin(() => {
	const config = useRuntimeConfig();

	const firebaseConfig = {
		apiKey: config.public.FIREBASE_API_KEY,
		authDomain: config.public.FIREBASE_AUTH_DOMAIN,
		projectId: config.public.FIREBASE_PROJECT_ID,
	};

	initializeApp(firebaseConfig);
});
