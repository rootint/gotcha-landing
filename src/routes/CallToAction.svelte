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
			Sign up now and edit <span style="color: var(--color-theme-1); font-weight: 500;">
				3 free
			</span>videos with Gotcha!
		</h2>
		<div style="height: 40px" />
		<EmailButton {isMobile} />
	</section>
{:else}
	<section>
		<h1 style="text-align: center; margin-bottom: 20px;">{title}</h1>
		<h2 style="text-align: center">
			Sign up now and edit <span style="color: var(--color-theme-1); font-weight: 500;">
				3 free
			</span>videos with Gotcha!
		</h2>
		<div style="height: 40px" />
		<EmailButton {isMobile} />
	</section>
	<div style="height: 12rem" />
{/if}

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
