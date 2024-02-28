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
								<NuxtImg src="/images/logo/google.svg" class="h-8 w-8" />
								<span class="ml-2">Google</span>
							</button>
						</li>
						<li class="my-1">
							<button class="" @click="signInWithGithub()">
								<NuxtImg src="/images/logo/github.svg" class="h-8 w-8" />
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
										<NuxtImg src="/images/logo/google_calendar.svg" class="h-12 w-12" />
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
										<NuxtImg src="/images/logo/github.svg" class="h-12 w-12" />
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
