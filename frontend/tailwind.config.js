/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ['./components/**/*.{js,vue,ts}', './layouts/**/*.vue', './pages/**/*.vue', './plugins/**/*.{js,ts}', './app.vue', './error.vue'],
	theme: {
		extend: {},
	},
	plugins: [require('daisyui')],
	daisyui: {
		themes: [
			{
				default: {
					primary: '#82AE46',
					secondary: '#f6d860',
					accent: '#37cdbe',
					neutral: '#f4ffe6',
					gray: '#606f78',
					'base-100': '#ffffff',
					'--rounded-box': '1rem', // border radius rounded-box utility class, used in card and other large boxes
					'--rounded-btn': '0.5rem', // border radius rounded-btn utility class, used in buttons and similar element
					'--rounded-badge': '1.9rem', // border radius rounded-badge utility class, used in badges and similar
					'--animation-btn': '0.25s', // duration of animation when you click on button
					'--animation-input': '0.2s', // duration of animation for inputs like checkbox, toggle, radio, etc
					'--btn-focus-scale': '0.95', // scale transform of button when you focus on it
					'--border-btn': '1px', // border width of buttons
					'--tab-border': '1px', // border width of tabs
					'--tab-radius': '0.5rem', // border radius of tabs
				},
			},
			'light',
			'dark',
			'cupcake',
		],
	},
};
