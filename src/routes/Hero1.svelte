<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;
</script>

{#if isMobile}
	<section class="mobile">
		<h1 class="mobile">{title}</h1>
		<h2 class="mobile">{subtitle}</h2>
		<div style="height: 40px" />
		<a class="button mobile" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a>
		<div style="height: 40px" />
		<img src="heroimage.png" alt="heroimage" class="herofgimage mobile" />
	</section>
{:else}
	<section class="desktop">
		<div class="herotext">
			<h1>{title}</h1>
			<h2>{subtitle}</h2>
			<div style="height: 40px" />
			<a class="button" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a>
		</div>
		<div class="centerpadding" />
		<div class="heroimage">
			<p class="background" />
			<img src="heroimage.png" alt="heroimage" class="herofgimage" />
		</div>
	</section>
{/if}

<style>
	section.mobile {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		margin: 0;
		padding-top: 80px;
		width: 100%;
	}

	section.desktop {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
		margin: 0;
		width: 100%;
	}

	p {
		margin: 0;
		padding: 0;
	}

	.herotext {
		flex: 0.5;
		justify-content: left;
		align-items: left;
	}

	.heroimage {
		position: relative;
		height: 50vh;
		flex: 0.5;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.herofgimage {
		width: 100%;
		border-radius: 16px;
		z-index: 1;
		animation: fade-in 1s ease-out;
	}

	@keyframes fade-in {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}

	@keyframes fade-in {
		from {
			opacity: 0;
		}
		to {
			opacity: 1;
		}
	}

	.background {
		width: 70%;
		aspect-ratio: 1/1;
		border-radius: 16px;
		background: linear-gradient(to bottom right, var(--color-theme-2), var(--color-theme-1));
		filter: blur(120px);
	}
</style>
