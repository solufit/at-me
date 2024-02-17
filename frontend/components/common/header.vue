<script setup lang="ts"></script>
<template>
	<div>
		<div class="navbar bg-base-100">
			<div class="flex-none">
				<div class="flex-none lg:hidden">
					<label for="my-drawer-3" aria-label="open sidebar" class="btn btn-square btn-ghost">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="inline-block w-5 h-5 stroke-current">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
						</svg>
					</label>
				</div>
			</div>
			<div class="flex-1">
				<a class="btn btn-ghost text-xl">@me</a>
			</div>
			<div class="flex-none">
				<div class="dropdown dropdown-end">
					<div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
						<div class="w-10 rounded-full">
							<img alt="Tailwind CSS Navbar component" src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
						</div>
					</div>
					<ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
						<li>
							<a class="justify-between">
								Profile
								<span class="badge">New</span>
							</a>
						</li>
						<li><a>Settings</a></li>
						<li><a>Logout</a></li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>
