<script setup lang="ts">
	const route = useRoute();
	const jwt = route.query.jwt;
	const linkcode = route.query.linkcode;
	const provider = route.query.provider;
	const { setToken } = useAccessToken();
	const { setLink } = useUserLink();
	setToken(jwt as string);
	setLink({ linkcode: linkcode as string, provider: provider as string });
	window.location.href = '/';
</script>
