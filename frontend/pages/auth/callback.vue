<script setup lang="ts">
	const route = useRoute();
	const jwt = route.query.jwt;
	const linkcode = route.query.linkcode;
	const { setToken } = useAccessToken();
	const { setLink } = useUserLink();
	setToken(jwt as string);
	setLink(linkcode as string);
	window.location.href = '/';
</script>
