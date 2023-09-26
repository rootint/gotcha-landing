<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isImageOnRight: boolean;
	export let imageUrl: string;
	export let isMobile: boolean;
</script>

{#if isMobile}
	<section class="mobile">
		<div class="featurestext">
			<h3>{title}</h3>
			<h4>{subtitle}</h4>
		</div>
		<div style="height: 40px" />
		<img src={imageUrl} alt="featuresimage" class="herofgimage mobile" />
	</section>
{:else}
	<section class="desktop">
		{#if isImageOnRight}
			<div class="featurestext">
				<h3>{title}</h3>
				<h4>{subtitle}</h4>
			</div>
			<div class="centerpadding" />
			<div class="featuresimage">
				<img src={imageUrl} alt="featuresimage" class="herofgimage" />
			</div>
		{:else}
			<div class="featuresimage">
				<img src={imageUrl} alt="featuresimage" class="herofgimage" />
			</div>
			<div class="centerpadding" />
			<div class="featurestext">
				<h3>{title}</h3>
				<h4>{subtitle}</h4>
			</div>
		{/if}
	</section>
{/if}

<style>
	section {
		padding: 10% 0;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 0;
		width: 100%;
	}

	.featurestext {
		flex: 0.5;
		justify-content: left;
		align-items: left;
	}

	.featuresimage {
		position: relative;
		flex: 0.5;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.herofgimage {
		width: 70%;
		border-radius: 16px;
		z-index: 1;
		animation: fade-in 1s ease-out;
	}
</style>
