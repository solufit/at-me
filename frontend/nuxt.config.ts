// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	devtools: { enabled: true },
	css: ['~/assets/css/main.css'],
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {},
		},
	},
	alias: {
		'*': 'types/*',
	},
	modules: ['@nuxt/image', 'dayjs-nuxt', '@pinia/nuxt', '@pinia-plugin-persistedstate/nuxt'],
	image: {
		format: ['webp'],
		dir: 'assets/images',
	},
	pinia: {
		storesDirs: ['./stores/**'],
	},
	runtimeConfig: {
		public: {
			FIREBASE_API_KEY: process.env.NUXT_PUBLIC_APIKEY || '',
			FIREBASE_AUTH_DOMAIN: process.env.NUXT_PUBLIC_AUTH_DOMAIN || '',
			FIREBASE_PROJECT_ID: process.env.NUXT_PUBLIC_PROJECT_ID || '',
		},
	},
});
