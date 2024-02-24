<script setup lang="ts">
	definePageMeta({
		layout: false,
	});
</script>
<template>
	<div>
		<div class="navbar bg-base-100">
			<div class="flex-1 text-xl"><NuxtImg src="/images/logo.webp" class="h-8 w-8" alt="logo" /> <span class="ml-1">@me</span></div>
			<div class="flex-none gap-4">
				<NuxtLink to="/" class="text- text-primary">ダッシュボード</NuxtLink>
				<button class="btn btn-square btn-primary w-24">ログイン</button>
			</div>
		</div>
		<div class="hero min-h-96 bg-base-200">
			<div class="hero-content">
				<div>
					<h1 class="text-5xl font-bold">あなたのAIパートナー<span class="mx-3">「@me」</span></h1>
					<p class="py-6 text-lg">AI × タスク管理で始める次世代のタスク管理</p>
					<button class="btn btn-primary">次世代のタスク管理を始めよう</button>
				</div>
			</div>
		</div>
		<div class="flex">
			<div class="p-4"></div>
		</div>
	</div>
</template>
