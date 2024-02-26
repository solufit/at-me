<script setup lang="ts">
	definePageMeta({
		layout: false,
	});
	const config = useRuntimeConfig();
	const signInWithGoogle = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/google/login`, {
			params: {
				redirect: config.public.AUTH_REDIRECT,
			},
		});
		window.location.href = data.value as string;
	};
	const signInWithGithub = async (): Promise<void> => {
		const { data, error } = await useFetch(`${config.public.AUTH_API}/github/login`, {
			params: {
				redirect: config.public.AUTH_REDIRECT,
			},
		});
		window.location.href = data.value as string;
	};
</script>
<template>
	<div>
		<div class="navbar bg-base-100">
			<div class="flex-1 text-xl"><NuxtImg src="/images/logo.webp" class="h-8 w-8" alt="logo" /> <span class="ml-1">@me</span></div>
			<div class="flex-none gap-4">
				<div class="dropdown dropdown-end">
					<div tabindex="0" role="button" class="btn btn-square btn-primary w-24">ログイン</div>
					<ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
						<li><button class="btn btn-square btn-primary w-24" @click="signInWithGoogle()">Google</button></li>
						<li><button class="btn btn-square btn-primary w-24" @click="signInWithGithub()">Github</button></li>
					</ul>
				</div>
			</div>
		</div>
		<div class="hero min-h-96 bg-base-200">
			<div class="hero-content">
				<div>
					<h1 class="text-5xl font-bold">あなたのAIパートナー<span class="mx-3">「@me」</span></h1>
					<p class="py-6 text-lg">AI × タスク管理で始める次世代のタスク管理</p>
					<button class="btn btn-primary" @click="signInWithGoogle()">次世代のタスク管理を始めよう</button>
				</div>
			</div>
		</div>
		<div class="flex">
			<div class="p-4"></div>
		</div>
	</div>
</template>
