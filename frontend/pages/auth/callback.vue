<script setup lang="ts">
	const route = useRoute();
	const jwt = route.query.jwt;
	const { setToken } = useAccessToken();
	setToken(jwt as string);
	window.location.href = '/';
</script>
