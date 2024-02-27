<script setup lang="ts">
	import type { Task } from '~/types/task';
	import Tasks from '~/components/uiparts/tasks.vue';
	definePageMeta({
		layout: false,
	});
	const config = useRuntimeConfig();
	const signInWithGoogle = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/google/login`);
		window.location.href = data.value as string;
	};
	const signInWithGithub = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/github/login`);
		window.location.href = data.value as string;
	};
	const task_rc: Task[] = [
		{
			id: '',
			title: 'Windows Updateをする',
			note: '',
			updated: new Date(),
			selfLink: 'string',
			parent: 'string',
			position: 'string',
			status: 'string',
			due: new Date(),
			duringtime: 30,
			completed: false,
			deleted: false,
			hidden: false,
			parent_id: '',
			provider: '',
		},
	];
</script>
<template>
	<div>
		<div class="navbar bg-base-100">
			<div class="flex-1 text-xl"><NuxtImg src="/images/logo.webp" class="h-8 w-8" alt="logo" /> <span class="ml-1">@me</span></div>
			<div class="flex-none gap-4">
				<NuxtLink to="/" class="btn-primary btn btn-outline">ダッシュボード</NuxtLink>
				<div class="dropdown dropdown-end">
					<div tabindex="0" role="button" class="btn btn-square btn-primary w-24">ログイン</div>
					<ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
						<li class="my-1">
							<button class="" @click="signInWithGoogle()">
								<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-8 w-8">
									<path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4" />
									<path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853" />
									<path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05" />
									<path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335" />
									<path d="M1 1h22v22H1z" fill="none" />
								</svg>
								<span class="ml-2">Google</span>
							</button>
						</li>
						<li class="my-1">
							<button class="" @click="signInWithGithub()">
								<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
									<path
										fill-rule="evenodd"
										clip-rule="evenodd"
										d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
										fill="#24292f"
									/>
								</svg>
								<span class="ml-2">Github</span>
							</button>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<div class="hero min-h-96 bg-base-200">
			<div class="hero-content">
				<div>
					<h1 class="text-2xl sm:text-5xl font-bold">あなたのAIパートナー<span class="mx-3">「@me」</span></h1>
					<p class="py-6 text-lg">AI × タスク管理で始める次世代のタスク管理</p>
					<button class="btn btn-primary" @click="signInWithGoogle()">次世代のタスク管理を始めよう</button>
				</div>
			</div>
		</div>
		<div class="flex flex-wrap border-2 p-2 m-2 my-6 rounded-lg">
			<div class="w-full md:w-1/2">
				<div class="flex justify-center bg-white">
					<NuxtImg src="/images/demo-toppage.webp" alt="logo" />
				</div>
			</div>
			<div class="w-full md:w-1/2 p-4 flex items-center justify-center">
				<div>
					<strong class="text-3xl text-primary"
						><div class="text-sm font-bold mr-5 navigate-topic">@meの推しPoint No.１</div>
						<div>カレンダー × タスク</div></strong
					>
					<div class="h-28 py-3 font-semibold">
						<div>生産性を高めるために必要不可欠な２要素を１つの画面に！</div>
					</div>
				</div>
			</div>
		</div>
		<div class="flex flex-wrap border-2 p-2 m-2 my-6 rounded-lg">
			<div class="w-full md:w-1/2 p-6">
				<div class="mockup-browser border bg-base-300">
					<div class="mockup-browser-toolbar h-3">
						<div class="input">https://at-me.solufit.net</div>
					</div>
					<div class="p-4 bg-white">
						<div class="h-72">
							<label class="hidden" for="name">タスク名</label>
							<input type="text" name="name" placeholder="タスク名" class="input w-full font-bold" value="部屋を片付ける" />
							<div class="py-4">
								<div class="flex mb-4">
									<div class="w-1/2">
										<div class="dropdown">
											<div tabindex="0" role="button" class="m-1 btn btn-xs">予定日 2024/2/26</div>
											<div tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box">
												<DatePicker :min-date="new Date()" mode="dateTime" color="green" />
											</div>
										</div>
									</div>
									<div class="w-1/2">
										<div class="dropdown dropdown-end">
											<div tabindex="0" role="button" class="m-1 btn btn-xs text-red-800">締め切り日 2024/3/26</div>
											<div tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box"></div>
										</div>
									</div>
								</div>
								<div class="flex flex-wrap mb-4">
									<div class="w-full md:w-4/5">
										<label class="hidden" for="duringtime">タスクにかかる時間</label>
										<input type="range" name="duringtime" min="0" max="120" class="range range-primary range-sm" step="15" />
										<div class="w-full flex justify-between text-xs px-2">
											<span>0</span>
											<span>30</span>
											<span>60</span>
											<span>90</span>
											<span>120</span>
										</div>
									</div>
									<div class="w-full md:w-1/5 pt-3 md:pl-6 text-xs">かかる時間: 30分</div>
								</div>
								<div class="text-end">
									<div class="btn btn-primary btn-md">
										<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
											<path
												stroke-linecap="round"
												stroke-linejoin="round"
												d="M9 3.75H6.912a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H15M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859M12 3v8.25m0 0-3-3m3 3 3-3"
											/>
										</svg>
										<span>保存</span>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="w-full md:w-1/2 p-4 flex items-center justify-center">
				<div>
					<strong class="text-3xl text-primary"
						><div class="text-sm font-bold mr-5 navigate-topic">@meの推しPoint No.２</div>
						<div>予定日だけじゃない！</div></strong
					>
					<div class="h-28 py-3 font-semibold">
						<div class="my-1">予定日と締め切り日をタスクに設定してタスクの見落としを防ごう</div>
						<div class="my-1"></div>
					</div>
				</div>
			</div>
		</div>
		<div class="flex flex-wrap border-2 p-2 m-2 my-6 rounded-lg">
			<div class="w-full md:w-1/2 p-6">
				<div class="mockup-browser border bg-base-300">
					<div class="mockup-browser-toolbar h-3">
						<div class="input">https://at-me.solufit.net</div>
					</div>
					<div class="p-4 bg-white">
						<div class="h-48">
							<div class="shadow-md shadow-lime-200 border-2 border-lime-200 p-3 rounded-md m-2 mb-6 font-semibold">
								<div><span>AI Recommend</span><span class="ml-2">for 30 mins</span></div>
								<div class="mt-4">
									<Tasks :tasks="task_rc" />
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="w-full md:w-1/2 flex p-4 items-center justify-center">
				<div>
					<strong class="text-3xl text-primary"
						><div class="text-sm font-bold mr-5 navigate-topic">@meの推しPoint No.３</div>
						<div>AIリコメンド機能搭載</div></strong
					>
					<div class="h-28 py-3 font-semibold">
						<div class="my-1">あなたのスケジュールに合わせてAIが最適なタスクをお勧めします</div>
					</div>
				</div>
			</div>
		</div>
		<div class="hero">
			<div class="hero-content my-6 flex-wrap items-center justify-center">
				<div class="w-full">
					<h1 class="text-lg md:text-xl font-bold text-center">普段使っているカレンダーやタスク管理ツールを連携して自分だけのアプリを作ろう！</h1>
				</div>
				<div class="w-full flex my-6">
					<div class="w-1/2 p-4">
						<div class="border p-4 h-48 rounded-xl">
							<div class="text-center">連携できるカレンダー</div>
							<div class="p-4 font-semibold">
								<div class="flex items-center justify-center gap-4">
									<div class="h-12 w-12">
										<svg
											xmlns="http://www.w3.org/2000/svg"
											xmlns:xlink="http://www.w3.org/1999/xlink"
											version="1.1"
											id="Livello_1"
											x="0px"
											y="0px"
											viewBox="0 0 200 200"
											enable-background="new 0 0 200 200"
											xml:space="preserve"
										>
											<g>
												<g transform="translate(3.75 3.75)">
													<path
														fill="#FFFFFF"
														d="M148.882,43.618l-47.368-5.263l-57.895,5.263L38.355,96.25l5.263,52.632l52.632,6.579l52.632-6.579    l5.263-53.947L148.882,43.618z"
													/>
													<path
														fill="#1A73E8"
														d="M65.211,125.276c-3.934-2.658-6.658-6.539-8.145-11.671l9.132-3.763c0.829,3.158,2.276,5.605,4.342,7.342    c2.053,1.737,4.553,2.592,7.474,2.592c2.987,0,5.553-0.908,7.697-2.724s3.224-4.132,3.224-6.934c0-2.868-1.132-5.211-3.395-7.026    s-5.105-2.724-8.5-2.724h-5.276v-9.039H76.5c2.921,0,5.382-0.789,7.382-2.368c2-1.579,3-3.737,3-6.487    c0-2.447-0.895-4.395-2.684-5.855s-4.053-2.197-6.803-2.197c-2.684,0-4.816,0.711-6.395,2.145s-2.724,3.197-3.447,5.276    l-9.039-3.763c1.197-3.395,3.395-6.395,6.618-8.987c3.224-2.592,7.342-3.895,12.342-3.895c3.697,0,7.026,0.711,9.974,2.145    c2.947,1.434,5.263,3.421,6.934,5.947c1.671,2.539,2.5,5.382,2.5,8.539c0,3.224-0.776,5.947-2.329,8.184    c-1.553,2.237-3.461,3.947-5.724,5.145v0.539c2.987,1.25,5.421,3.158,7.342,5.724c1.908,2.566,2.868,5.632,2.868,9.211    s-0.908,6.776-2.724,9.579c-1.816,2.803-4.329,5.013-7.513,6.618c-3.197,1.605-6.789,2.421-10.776,2.421    C73.408,129.263,69.145,127.934,65.211,125.276z"
													/>
													<path fill="#1A73E8" d="M121.25,79.961l-9.974,7.25l-5.013-7.605l17.987-12.974h6.895v61.197h-9.895L121.25,79.961z" />
													<path fill="#EA4335" d="M148.882,196.25l47.368-47.368l-23.684-10.526l-23.684,10.526l-10.526,23.684L148.882,196.25z" />
													<path fill="#34A853" d="M33.092,172.566l10.526,23.684h105.263v-47.368H43.618L33.092,172.566z" />
													<path
														fill="#4285F4"
														d="M12.039-3.75C3.316-3.75-3.75,3.316-3.75,12.039v136.842l23.684,10.526l23.684-10.526V43.618h105.263    l10.526-23.684L148.882-3.75H12.039z"
													/>
													<path fill="#188038" d="M-3.75,148.882v31.579c0,8.724,7.066,15.789,15.789,15.789h31.579v-47.368H-3.75z" />
													<path fill="#FBBC04" d="M148.882,43.618v105.263h47.368V43.618l-23.684-10.526L148.882,43.618z" />
													<path fill="#1967D2" d="M196.25,43.618V12.039c0-8.724-7.066-15.789-15.789-15.789h-31.579v47.368H196.25z" />
												</g>
											</g>
										</svg>
									</div>
									<div class="hidden md:block">Google カレンダー</div>
								</div>
							</div>
						</div>
					</div>
					<div class="w-1/2 p-4">
						<div class="border p-4 h-48 rounded-xl">
							<div class="text-center">連携できるタスク管理ツール</div>
							<div class="p-4 font-semibold">
								<div class="flex items-center justify-center gap-4">
									<div class="h-12 w-12">
										<svg viewBox="0 0 98 96" xmlns="http://www.w3.org/2000/svg">
											<path
												fill-rule="evenodd"
												clip-rule="evenodd"
												d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
												fill="#24292f"
											/>
										</svg>
									</div>
									<div class="hidden md:block">Github Issues</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="divider w-full"></div>
				<div class="text-xs text-gray-700 text-left p-1">
					<div>α版のみで提供している連携機能も含みます</div>
				</div>
			</div>
		</div>
		<footer class="footer p-10 text-white" style="--tw-bg-opacity: 1; background-color: #606f78; --tw-text-opacity: 1">
			<aside>
				<img src="https://r2.solufit.net/solufit_common_icon.png" alt="Solufit共通アイコン" class="h-12" />
				<p>Build future yourself</p>
				<p class="text-left">Copylight © 2023-2024 Solufit</p>
			</aside>
			<nav>
				<header class="footer-title">Link</header>
				<div class="grid grid-flow-col gap-4">
					<a href="https://solufit.net">Solufit</a>
					<a href="https://solufit.net/terms">利用規約</a>
					<a href="https://solufit.net/privacy">プライバシーポリシー</a>
				</div>
			</nav>
		</footer>
	</div>
</template>
<style>
	.navigate-topic {
		letter-spacing: 0.08rem;
		margin-bottom: 10px;
	}
</style>
