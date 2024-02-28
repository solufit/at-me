<script setup lang="ts">
	import headervue from '~/components/common/header.vue';
	import Licence from '~/components/licence.vue';
	import taskdetail from '~/components/uiparts/taskdetail.vue';
	import Calendar from '~/components/sidebar/calendar.vue';
	const { $pwa } = useNuxtApp();
	const showInstall = ref(true);
	const dismiss = async () => {
		showInstall.value = false;
	};
	const install = async () => {
		$pwa?.install();
	};
</script>
<template>
	<div class="min-h-screen">
		<headervue />
		<div class="lg:flex">
			<div class="drawer lg:drawer-open w-80">
				<input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
				<div class="drawer-side lg:h-fit z-20">
					<label for="my-drawer-3" aria-label="close sidebar" class="drawer-overlay"></label>
					<div class="menu p-4 w-80 bg-white lg:bg-transparent h-screen md:h-fit">
						<div class="mb-6 lg:hidden">
							<NuxtLink to="/" class="btn btn-ghost text-xl"> <NuxtImg src="/images/logo.webp" class="h-8 w-8" alt="logo" />@me</NuxtLink>
						</div>
						<div class="flex items-center justify-center mb-7">
							<Calendar />
						</div>
						<ul class="">
							<!-- Sidebar content here -->
							<li class="my-3"><NuxtLink to="/">TODAY</NuxtLink></li>
							<li class="my-3"><NuxtLink to="/near">近日予定のタスク</NuxtLink></li>
							<li class="my-3"><NuxtLink to="/deadline">締め切り</NuxtLink></li>
						</ul>
						<hr />
						<ul class="">
							<!-- Sidebar content here -->
							<li class="my-1"><NuxtLink to="/tutorial">チュートリアル</NuxtLink></li>
							<li class="my-1"><a href="https://solufit.net/terms" target="_blank">利用規約</a></li>
							<li class="my-1"><a href="https://solufit.net/privacy" target="_blank">プライバシーポリシー</a></li>
							<li class="my-1"><button onclick="oss_license.showModal()">OSSライセンス</button></li>

							<li class="my-1"><NuxtLink to="/about">このアプリについて</NuxtLink></li>
						</ul>
						<dialog id="oss_license" class="modal">
							<div class="modal-box">
								<Licence />
							</div>
							<form method="dialog" class="modal-backdrop">
								<button>close</button>
							</form>
						</dialog>
					</div>
				</div>
			</div>
			<div class="p-6 w-full" style="height: 90vh">
				<div v-if="$pwa?.isPWAInstalled == false && showInstall == true" class="w-full bg-neutral rounded-xl px-4 py-2 my-4 mb-10 text-sm flex items-center justify-center">
					<div class="flex-1">アプリをダウンロードしてもっと便利に！</div>
					<div class="flex-none flex gap-3">
						<div class="p-1">
							<button class="btn btn-primary btn-sm" @click="install()">インストール</button>
						</div>
						<button class="underline p-1" @click="dismiss()">表示しない</button>
					</div>
				</div>
				<div>
					<slot />
				</div>
			</div>
			<div class="relative">
				<!--
				<div class="dropdown dropdown-top dropdown-end absolute bottom-0 right-0 m-5">
					<div tabindex="0" role="button" class="btn btn-square m-1 bg-primary border-0">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
							<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
						</svg>
					</div>
					<ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
						<li><a>タスクを追加</a></li>
						<li><a>予定を追加</a></li>
					</ul>
				</div>
				-->
				<div class="fixed bottom-0 right-0 m-6">
					<div class="md:tooltip" data-tip="タスクを追加">
						<button tabindex="0" role="button" class="btn btn-square m-1 bg-primary border-0" onclick="add_task.showModal()" aria-label="タスクの追加">
							<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
								<path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
							</svg>
						</button>
					</div>
				</div>
				<dialog id="add_task" class="modal">
					<div class="modal-box">
						<taskdetail />
					</div>
					<form method="dialog" class="modal-backdrop">
						<button>close</button>
					</form>
				</dialog>
			</div>
		</div>
	</div>
</template>
