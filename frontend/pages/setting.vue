<script setup lang="ts">
	useHead({
		title: '設定 | @me',
	});
	definePageMeta({
		layout: 'simple',
	});
	import { useUserStore } from '../composables/user';
	import { useAuth } from '../composables/auth';
	const { user } = useUserStore();
	const { userLink } = useUserLink();
	const signOut = async (): Promise<void> => {
		await useAuth().signOut();
		await navigateTo('/signIn');
	};
	// defined form model
	const rsc_calendar = ref(user?.calenderProvider);
	const rsc_tasks = ref(user?.taskProvider);
	// defined translate
	let rsc_calender_default = '未設定';
	switch (user?.calenderProvider as String) {
		case 'atme':
			rsc_calender_default = '@me';
			break;
		case 'GoogleCalender':
			rsc_calender_default = 'Google カレンダー';
			break;
		default:
			rsc_calender_default = '';
			break;
	}
	let rsc_tasks_default = '未設定';
	switch (user?.taskProvider as String) {
		case 'atme':
			rsc_tasks_default = '@me';
			break;
		case 'GoogleTasks':
			rsc_tasks_default = 'Google タスク';
			break;
		case 'GithubIssues':
			rsc_tasks_default = 'Github Issues';
			break;
		default:
			rsc_tasks_default = '';
	}
	// defined variable
	const wt_mon = ref(true);
	const wt_the = ref(true);
	const wt_wed = ref(true);
	const wt_thu = ref(true);
	const wt_fri = ref(true);
	const wt_sat = ref(false);
	const wt_sun = ref(false);
	// defined function
	const config = useRuntimeConfig();
	const signInWithGoogle = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/google/login`, {});
		window.location.href = data.value as string;
	};
	const linkWithGithub = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/github/install`, {});
		window.location.href = data.value as string;
	};
	const rsc_submit = async () => {
		console.log('test');
		const { data, error } = await useFetch(`${config.public.AUTH_API}/user/set_provider`, {
			params: {
				userId: user?.userId,
				calenderProvider: rsc_calendar.value,
				taskProvider: rsc_tasks.value,
			},
			method: 'POST',
		});
		await refreshNuxtData();
	};
</script>
<template>
	<div class="p-5">
		<h1 class="font-bold text-2xl mb-12">設定</h1>
		<div class="flex border-2 shadow-sm rounded-lg p-6 items-center justify-center h-32">
			<div class="avater">
				<div class="w-12 md:w-24 rounded-full">
					<img alt="User Icon" :src="user?.photoURL" class="rounded-full" />
				</div>
				<div class="block md:hidden items-center justify-center ml-11">
					<div class="rounded-full" v-if="userLink?.provider == 'github'">
						<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4">
							<path
								fill-rule="evenodd"
								clip-rule="evenodd"
								d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
								fill="#24292f"
							/>
						</svg>
					</div>
					<div class="rounded-full" v-if="userLink?.provider == 'google'">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-4 w-4">
							<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
							<path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
							<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
							<path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
							<path d="M1 1h22v22H1z" fill="none" />
						</svg>
					</div>
				</div>
			</div>
			<div class="md:w-1/2 p-3 ml-6">
				<div class="text-2xl">
					<div class="text-2xl m-1">{{ user?.displayName }}</div>
					<div class="text-sm m-1">{{ user?.email }}</div>
				</div>
			</div>
			<div class="hidden md:block items-center justify-center mr-6">
				<div class="rounded-full" v-if="userLink?.provider == 'github'">
					<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
						<path
							fill-rule="evenodd"
							clip-rule="evenodd"
							d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
							fill="#24292f"
						/>
					</svg>
				</div>
				<div class="rounded-full" v-if="userLink?.provider == 'google'">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-8 w-8">
						<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
						<path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
						<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
						<path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
						<path d="M1 1h22v22H1z" fill="none" />
					</svg>
				</div>
			</div>
			<button class="hidden md:flex items-center justify-center btn btn-outline btn-primary w-36" @click="signOut">
				<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M15.75 9V5.25A2.25 2.25 0 0 0 13.5 3h-6a2.25 2.25 0 0 0-2.25 2.25v13.5A2.25 2.25 0 0 0 7.5 21h6a2.25 2.25 0 0 0 2.25-2.25V15m3 0 3-3m0 0-3-3m3 3H9"
					/>
				</svg>
				<span class="ml-3">ログアウト</span>
			</button>
		</div>
		<div class="mt-3">
			<div class="border rounded-lg p-2 my-6">
				<h2 class="font-bold m-2">連携アカウント</h2>
				<p class="m-4 text-sm text-gray-600">ほかのサービスからタスクやカレンダーを読み込むことができます</p>
				<div class="p-3">
					<div class="overflow-x-auto">
						<table class="hidden md:table fixed text-center items-center justify-center">
							<thead>
								<tr>
									<th>アカウント</th>
									<th></th>
									<th>カレンダーリソース</th>
									<th>タスクリソース</th>
									<th></th>
								</tr>
							</thead>
							<tbody>
								<tr v-if="user?.providers.google.id != ''">
									<td>
										<div class="flex items-center gap-3">
											<div class="avatar">
												<div class="mask mask-squircle w-12 h-12">
													<img :src="user?.photoURL" alt="Avatar Tailwind CSS Component" />
												</div>
											</div>
											<div>
												<div class="font-bold text-left">{{ user?.providers.google.displayName }}</div>
												<div class="text-sm opacity-50">{{ user?.providers.google.email }}</div>
											</div>
										</div>
									</td>
									<td class="flex items-center justify-center">
										<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-8 w-8">
											<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
											<path
												d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
												fill="#34A853"
											/>
											<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
											<path
												d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
												fill="#EA4335"
											/>
											<path d="M1 1h22v22H1z" fill="none" />
										</svg>
										<span class="ml-3 text-lg">Google</span>
									</td>
									<td>Google Calender</td>
									<td>Google Tasks</td>
									<th>
										<button class="btn btn-sm">連携解除</button>
									</th>
								</tr>
								<tr v-else>
									<td><button class="btn m-2 btn-primary" @click="signInWithGoogle()">Googleアカウントでログイン</button></td>
									<td class="flex items-center justify-center">
										<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-8 w-8">
											<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
											<path
												d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
												fill="#34A853"
											/>
											<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
											<path
												d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
												fill="#EA4335"
											/>
											<path d="M1 1h22v22H1z" fill="none" />
										</svg>
										<span class="ml-3 text-lg">Google</span>
									</td>
									<td>Google Calender</td>
									<td>Google Tasks</td>
									<td></td>
								</tr>
								<tr v-if="user?.providers.github.id != ''">
									<td>
										<div class="flex items-center gap-3">
											<div class="avatar">
												<div class="mask mask-squircle w-12 h-12">
													<img :src="user?.photoURL" alt="Avatar Tailwind CSS Component" />
												</div>
											</div>
											<div>
												<div class="font-bold text-left">{{ user?.displayName }}</div>
												<div class="text-sm opacity-50">{{ user?.email }}</div>
											</div>
										</div>
									</td>
									<td class="flex items-center justify-center">
										<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
											<path
												fill-rule="evenodd"
												clip-rule="evenodd"
												d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
												fill="#24292f"
											/>
										</svg>
										<span class="ml-3 text-lg">Github</span>
									</td>
									<td></td>
									<td>Assigned Issue</td>
									<th>
										<button class="btn btn-sm">連携解除</button>
									</th>
								</tr>
								<tr v-else>
									<td><button class="btn m-2 btn-primary" @click="linkWithGithub()">Githubアカウントでログイン</button></td>
									<td class="flex items-center justify-center">
										<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
											<path
												fill-rule="evenodd"
												clip-rule="evenodd"
												d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
												fill="#24292f"
											/>
										</svg>
										<span class="ml-3 text-lg">Github</span>
									</td>
									<td></td>
									<td>Assigned Issue</td>
									<td></td>
								</tr>
							</tbody>
						</table>
						<div class="bloxk md:hidden">
							<div class="my-3 flex items-center gap-3">
								<div class="rounded-full">
									<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-4 w-4">
										<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
										<path
											d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
											fill="#34A853"
										/>
										<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
										<path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
										<path d="M1 1h22v22H1z" fill="none" />
									</svg>
								</div>
								<div class="w-1/3">Google</div>
								<button class="btn btn-sm w-24 btn-primary" @click="signInWithGoogle()" v-if="user?.providers.google.id == ''">連携する</button>
								<button class="btn btn-sm w-24" v-else>連携中</button>
							</div>
							<div class="my-3 flex items-center gap-3">
								<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4">
									<path
										fill-rule="evenodd"
										clip-rule="evenodd"
										d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
										fill="#24292f"
									/>
								</svg>
								<div class="w-1/3">Github</div>
								<button class="btn btn-sm w-24 btn-primary" @click="linkWithGithub()" v-if="user?.providers.google.id == ''">連携する</button>
								<button class="btn btn-sm w-24" v-else>連携中</button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="border rounded-lg p-2 my-6">
				<h2 class="font-bold m-2">リソース設定</h2>
				<p class="m-4 text-sm text-gray-600">カレンダーやタスクとして表示するリソースを設定します</p>
				<div class="p-3">
					<div class="flex items-center justify-center flex-wrap">
						<div class="w-full md:w-1/2">
							<label class="form-control w-full max-w-xs md:max-w-md">
								<div class="label">
									<span class="label-text">カレンダー</span>
								</div>
								<select class="select select-bordered" v-model="rsc_calendar">
									<option value="atme">@me</option>
									<option value="GoogleCalender" v-if="user?.providers.google.id != ''">Google カレンダー</option>
								</select>
							</label>
						</div>
						<div class="w-full md:w-1/2">
							<label class="form-control w-full max-w-xs md:max-w-md">
								<div class="label">
									<span class="label-text">タスク</span>
								</div>
								<select class="select select-bordered" v-model="rsc_tasks">
									<option value="atme">@me</option>
									<option value="GoogleTasks" v-if="user?.providers.google.id != ''">Google タスク</option>
									<option value="GithubIssues" v-if="user?.providers.github.id != ''">Github Issues</option>
								</select>
							</label>
						</div>
					</div>
					<div class="p-4 my-6">
						<div class="text-end">
							<button class="btn btn-primary w-40" @click="rsc_submit()">保存</button>
						</div>
					</div>
				</div>
			</div>
			<div class="border rounded-lg p-2 my-6">
				<h2 class="font-bold m-2">機能設定</h2>
				<p class="m-4 text-sm text-gray-600"></p>
				<div class="p-3">
					<div class="flex flex-wrap my-2">
						<div class="w-full md:w-1/3 my-1">AI Recommend</div>
						<div class="w-full md:w-1/3 my-1">あなたのスケジュールとタスクをもとにタスクをリコメンドします<span class="text-xs ml-1">*1</span></div>
						<div class="w-full md:w-1/3 my-1 text-end"><input type="checkbox" class="toggle toggle-primary" checked /></div>
					</div>
					<hr />
					<div class="text-gray-400 text-xs">
						<div class="flex my-1">
							<div class="w-5">1</div>
							<div>
								この機能を使用した場合、あなたのスケジュールの時間とタスクの所要時間のみをAI機能を提供する第三者へ共有します<br />
								スケジュールの場所や名前、タスクのタイトルやノート、あなたのアカウント情報などは提供されません。<br />
								すべての情報はSolufit共通プライバシーポリシーに準拠し適切に扱われます。
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="border rounded-lg p-2 my-6 md:p-6">
				<h2 class="font-bold m-2">ワークタイム</h2>
				<p class="m-4 text-sm text-gray-600">ワークタイムを設定するとワークタイム以外の時間にはタスクをレコメンドされなくなります。</p>
				<div class="p-3">
					<div class="md:flex flex-wrap items-center justify-center gap-3 my-4 mb-12">
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">月曜日</span>
								<input type="checkbox" v-model="wt_mon" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">火曜日</span>
								<input type="checkbox" v-model="wt_the" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">水曜日</span>
								<input type="checkbox" v-model="wt_wed" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">木曜日</span>
								<input type="checkbox" v-model="wt_thu" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">金曜日</span>
								<input type="checkbox" v-model="wt_fri" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">土曜日</span>
								<input type="checkbox" v-model="wt_sat" class="checkbox checkbox-primary" />
							</label>
						</div>
						<div class="form-control">
							<label class="cursor-pointer label">
								<span class="label-text mr-2">日曜日</span>
								<input type="checkbox" v-model="wt_sun" class="checkbox checkbox-primary" />
							</label>
						</div>
					</div>
					<div class="p-3 md:flex">
						<div class="w-full md:w-1/2 p-2 md:p-4 fonm-control">
							<label for="wt_start">開始時刻</label>
							<input class="input w-full my-1" name="wt_start" type="time" />
						</div>
						<div class="w-full md:w-1/2 p-2 md:p-4 fonm-control">
							<label for="wt_end">終了時刻</label>
							<input class="input w-full my-1" name="wt_end" type="time" />
						</div>
					</div>
				</div>
				<div class="p-4 my-6">
					<div class="text-end">
						<button class="btn btn-primary w-40">保存</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
