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
	const { token } = useAccessToken();
	const signOut = async (): Promise<void> => {
		await useAuth().signOut();
		await navigateTo('/signIn');
	};
	// defined form model
	const rsc_calendar = ref(user?.calendarProvider);
	const rsc_tasks = ref(user?.taskProvider);
	// defined translate
	let rsc_calendar_default = '未設定';
	switch (user?.calendarProvider as String) {
		case 'atme':
			rsc_calendar_default = '@me';
			break;
		case 'GoogleCalendar':
			rsc_calendar_default = 'Google カレンダー';
			break;
		default:
			rsc_calendar_default = '';
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
		const { data, error } = await useFetch(`${config.public.AUTH_API}/github/login`, {});
		window.location.href = data.value as string;
	};
	const rsc_submit = async () => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/user/set_provider`, {
			params: {
				token: token,
				calendarProvider: rsc_calendar.value,
				taskProvider: rsc_tasks.value,
			},
			method: 'POST',
		});
		await refreshNuxtData();
	};
	const rm_provider = async (provider: string) => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/user/unlink`, {
			params: {
				token: token,
				provider: provider,
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
					<div class="rounded-full" v-if="user?.loginProvider == 'github'">
						<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
					</div>
					<div class="rounded-full" v-if="user?.loginProvider == 'google'">
						<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
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
				<div class="rounded-full" v-if="user?.loginProvider == 'github'">
					<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
				</div>
				<div class="rounded-full" v-if="user?.loginProvider == 'google'">
					<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
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
										<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
										<span class="ml-3 text-lg">Google</span>
									</td>
									<td>Google Calender</td>
									<td>Google Tasks</td>
									<th>
										<button class="btn btn-sm" @click="rm_provider('google')">連携解除</button>
									</th>
								</tr>
								<tr v-else>
									<td><button class="btn m-2 btn-primary" @click="signInWithGoogle()">Googleアカウントでログイン</button></td>
									<td class="flex items-center justify-center">
										<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
										<span class="ml-3 text-lg">Google</span>
									</td>
									<td>Google Calendar</td>
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
												<div class="font-bold text-left">{{ user?.providers.github.displayName }}</div>
												<div class="text-sm opacity-50">{{ user?.providers.github.email }}</div>
											</div>
										</div>
									</td>
									<td class="flex items-center justify-center">
										<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
										<span class="ml-3 text-lg">Github</span>
									</td>
									<td></td>
									<td>Assigned Issue</td>
									<th>
										<button class="btn btn-sm" @click="rm_provider('github')">連携解除</button>
									</th>
								</tr>
								<tr v-else>
									<td><button class="btn m-2 btn-primary" @click="linkWithGithub()">Githubアカウントでログイン</button></td>
									<td class="flex items-center justify-center">
										<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
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
									<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
								</div>
								<div class="w-1/3">Google</div>
								<button class="btn btn-sm w-24 btn-primary" @click="signInWithGoogle()" v-if="user?.providers.google.id == ''">連携する</button>
								<button class="btn btn-sm w-24" v-else @click="rm_provider('google')">連携解除</button>
							</div>
							<div class="my-3 flex items-center gap-3">
								<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
								<div class="w-1/3">Github</div>
								<button class="btn btn-sm w-24 btn-primary" @click="linkWithGithub()" v-if="user?.providers.google.id == ''">連携する</button>
								<button class="btn btn-sm w-24" v-else @click="rm_provider('github')">連携解除</button>
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
						<div class="w-full md:w-1/2 p-2">
							<label class="form-control w-full max-w-xs md:max-w-md">
								<div class="label">
									<span class="label-text">カレンダー</span>
								</div>
								<select class="select select-bordered" v-model="rsc_calendar">
									<option value="atme">@me</option>
									<option value="GoogleCalendar" v-if="user?.providers.google.id != ''">Google カレンダー</option>
								</select>
							</label>
							<div class="my-4">
								<div class="font-semibold">選択できるリソース</div>
								<div class="my-2 flex flex-wrap gap-4">
									<NuxtImg src="/images/logo/google_calendar.svg" class="h-12 w-12" v-if="user?.providers.google.id != ''" />
								</div>
							</div>
						</div>
						<div class="w-full md:w-1/2 p-2">
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
							<div class="my-4">
								<div class="font-semibold">選択できるリソース</div>
								<div class="my-2 flex flex-wrap gap-4">
									<NuxtImg src="/images/logo/github.svg" class="h-12 w-12" v-if="user?.providers.github.id != ''" />
								</div>
							</div>
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
