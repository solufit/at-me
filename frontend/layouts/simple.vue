<script setup lang="ts">
	import headervue from '~/components/common/header.vue';
	import Licence from '~/components/licence.vue';
</script>
<template>
	<div>
		<headervue />
		<div class="lg:flex">
			<div class="drawer lg:drawer-open w-80">
				<input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
				<div class="drawer-side lg:h-fit z-20">
					<label for="my-drawer-3" aria-label="close sidebar" class="drawer-overlay"></label>
					<div class="menu p-4 w-80 min-h-screen lg:min-h-fit bg-white lg:bg-transparent">
						<div class="mb-6 lg:hidden">
							<a class="btn btn-ghost text-xl" href="/"> <NuxtImg src="/images/logo.webp" class="h-8 w-8" alt="logo" />@me</a>
						</div>
						<ul class="h-96">
							<!-- Sidebar content here -->
							<li class="my-3"><NuxtLink to="/">TODAY</NuxtLink></li>
							<li class="my-3"><NuxtLink to="/near">近日予定のタスク</NuxtLink></li>
							<li class="my-3"><NuxtLink to="/deadline">締め切り</NuxtLink></li>
						</ul>
						<hr />
						<ul class="">
							<!-- Sidebar content here -->
							<li class="my-1"><NuxtLink to="/">チュートリアル</NuxtLink></li>
							<li class="my-1"><NuxtLink to="/">利用規約</NuxtLink></li>
							<li class="my-1"><button onclick="oss_license.showModal()">OSSライセンス</button></li>

							<li class="my-1"><NuxtLink to="/">このアプリについて</NuxtLink></li>
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
			<div class="p-6 w-full overflow-y-auto" style="height: 93vh">
				<slot />
			</div>
		</div>
	</div>
</template>
