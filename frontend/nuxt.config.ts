// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	devtools: { enabled: false },
	css: ['~/assets/css/main.css'],
	ssr: false,
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {},
		},
	},
	alias: {
		'*': 'types/*',
	},
	app: {
		head: {
			htmlAttrs: {
				lang: 'ja',
				prefix: 'og: http://ogp.me/ns#',
			},
			charset: 'utf-8',
			viewport: 'width=device-width, initial-scale=1',
			title: '@me',
			meta: [
				{ name: 'description', content: '予定 × タスクで始める時間管理アプリケーション' },
				{ name: 'theme-color', content: '#82AE46' },
			],
			link: [{ rel: 'manifest', href: '/manifest.webmanifest' }],
		},
	},
	modules: ['@nuxt/image', 'dayjs-nuxt', '@pinia/nuxt', '@pinia-plugin-persistedstate/nuxt', '@vite-pwa/nuxt'],
	image: {
		format: ['webp', 'png'],
		dir: 'public/',
	},
	pinia: {
		storesDirs: ['./composables/**'],
	},
	piniaPersistedstate: {
		cookieOptions: {
			sameSite: 'strict',
		},
		storage: 'localStorage',
	},
	pwa: {
		registerType: 'autoUpdate',
		includeAssets: ['favicon.ico'],
		client: {
			installPrompt: true,
		},
		manifest: {
			name: '@me',
			description: '予定 × タスクで始める時間管理アプリケーション',
			theme_color: '#82AE46',
			lang: 'ja',
			short_name: '@me',
			start_url: '/',
			display: 'standalone',
			background_color: '#ffffff',
			icons: [
				{
					src: 'icons/icon-36x36.png',
					sizes: '36x36',
					type: 'image/png',
				},
				{
					src: 'icons/icon-x48.png',
					sizes: '48x48',
					type: 'image/png',
					purpose: 'maskable',
				},
				{
					src: 'icons/icon-x72.png',
					sizes: '72x72',
					type: 'image/png',
					purpose: 'maskable',
				},
				{
					src: 'icons/icon-x96.png',
					sizes: '96x96',
					type: 'image/png',
					purpose: 'maskable',
				},
				{
					src: 'icons/icon-x128.png',
					sizes: '128x128',
					type: 'image/png',
					purpose: 'maskable',
				},
				{
					src: 'icons/icon-144x144.png',
					sizes: '144x144',
					type: 'image/png',
				},
				{
					src: 'icons/icon-152x152.png',
					sizes: '152x152',
					type: 'image/png',
				},
				{
					src: 'icons/icon-192x192.png',
					sizes: '192x192',
					type: 'image/png',
					purpose: 'maskable',
				},
				{
					src: 'icons/icon-256x256.png',
					sizes: '256x256',
					type: 'image/png',
				},
				{
					src: 'icons/icon-384x384.png',
					sizes: '384x384',
					type: 'image/png',
				},
				{
					src: 'icons/icon-512x512.png',
					sizes: '512x512',
					type: 'image/png',
				},
			],
		},
		workbox: {
			navigateFallback: null,
		},
		devOptions: {
			enabled: true,
			type: 'module',
		},
	},
	runtimeConfig: {
		public: {
			API_ENDPOINT: process.env.NUXT_PUBLIC_API_ENDPOINT || '',
			AUTH_API: process.env.NUXT_PUBLIC_AUTH_API || '',
			AUTH_REDIRECT: process.env.NUXT_PUBLIC_AUTH_REDIRECT || '',
		},
	},
});
