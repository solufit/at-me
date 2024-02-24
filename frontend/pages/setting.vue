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
	const signOut = async (): Promise<void> => {
		await useAuth().signOut();
		await navigateTo('/signIn');
	};
	const providers = (user === null || user === undefined ? [] : user.providerData).map((pvd) => {
		return pvd.providerId;
	});
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
		<div class="flex border-2 shadow-sm rounded-lg p-6 items-center justify-center">
			<div class="w-1/4 rounded-full">
				<img alt="User Icon" :src="user?.photoURL" v-if="user?.photoURL !== null" />
			</div>
			<div class="md:w-1/2 p-3">
				<div class="text-2xl">
					<div class="text-2xl m-1">{{ user?.displayName }}</div>
					<div class="text-sm m-1">{{ user?.email }}</div>
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
		<div class="mt-6 p-6">
			<h2 class="font-bold">アカウント連携</h2>
			<p class="m-2 text-sm text-gray-600">アカウントを連携することでほかのサービスの情報を利用することができます。</p>
			<div class="p-6">
				<div class="flex items-center justify-center">
					<div class="w-2/3">Google</div>
					<div class="w-1/3">
						<button class="btn w-24" v-if="providers.indexOf('google.com')">連携する</button>
						<button class="btn w-24 btn-disabled" v-else>連携中</button>
					</div>
				</div>
			</div>
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
