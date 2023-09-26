<script lang="ts">
	import EmailButton from './EmailButton.svelte';
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;
</script>

{#if isMobile}
	<section class="mobile">
		<h1 style="text-align: center" class="mobile">{title}</h1>
		<h2 style="text-align: center" class="mobile">
			{subtitle}
		</h2>
		<div style="height: 40px" />
		<EmailButton {isMobile} />
	</section>
{:else}
	<section>
		<h1 style="text-align: center">{title}</h1>
		<h2 style="text-align: center">
			{subtitle}
		</h2>
		<div style="height: 40px" />
		<EmailButton {isMobile} />
	</section>
{/if}

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
