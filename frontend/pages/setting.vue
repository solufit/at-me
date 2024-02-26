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
	const wt_mon = ref(true);
	const wt_the = ref(true);
	const wt_wed = ref(true);
	const wt_thu = ref(true);
	const wt_fri = ref(true);
	const wt_sat = ref(false);
	const wt_sun = ref(false);
</script>
<template>
	<div class="p-5">
		<h1 class="font-bold text-2xl mb-12">設定</h1>
		<div class="flex border-2 shadow-sm rounded-lg p-6 items-center justify-center h-32">
			<div class="avater">
				<div class="w-24 rounded-full">
					<img alt="User Icon" :src="user?.photoURL" class="rounded-full" />
				</div>
			</div>
			<div class="md:w-1/2 p-3 ml-6">
				<div class="text-2xl">
					<div class="text-2xl m-1">{{ user?.displayName }}</div>
					<div class="text-sm m-1">{{ user?.email }}</div>
				</div>
			</div>
			<div class="items-center justify-center mr-3">
				<div class="w-12 rounded-full" v-if="userLink?.provider == 'github'">
					<svg viewBox="0 0 98 98" xmlns="http://www.w3.org/2000/svg" class="h-8 w-8">
						<path
							fill-rule="evenodd"
							clip-rule="evenodd"
							d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z"
							fill="#24292f"
						/>
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
		<div class="mt-3 p-6">
			<h2 class="font-bold">ワークタイム</h2>
			<p class="m-2 text-sm text-gray-600">ワークタイムを設定するとワークタイム以外の時間にはタスクをレコメンドされなくなります。</p>
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
			<button class="btn btn-primary w-full">保存</button>
		</div>
	</div>
</template>
