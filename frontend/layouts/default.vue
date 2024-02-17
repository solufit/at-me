<script setup lang="ts">
	import headervue from '~/components/common/header.vue';
	import calender from '~/components/sidebar/calender.vue';
</script>
<template>
	<div>
		<headervue />
		<div class="lg:flex">
			<div class="drawer lg:drawer-open w-80">
				<input id="my-drawer-3" type="checkbox" class="drawer-toggle" />
				<div class="drawer-side lg:h-fit z-20">
					<label for="my-drawer-3" aria-label="close sidebar" class="drawer-overlay"></label>
					<div class="menu p-4 w-80 min-h-screen lg:min-h-fit bg-base-200 lg:bg-transparent">
						<div class="flex items-center justify-center mb-7">
							<calender />
						</div>
						<ul class="">
							<!-- Sidebar content here -->
							<li><a>Sidebar Item 1</a></li>
							<li><a>Sidebar Item 2</a></li>
						</ul>
					</div>
				</div>
			</div>
			<div class="p-6 w-full">
				<slot />
			</div>
		</div>
	</div>
</template>
