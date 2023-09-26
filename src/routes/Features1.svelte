<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isImageOnRight: boolean;
	// export let imageUrl: string;
	export let isMobile: boolean;
	export let imageSvg: string;
</script>

{#if isMobile}
	<section class="mobile">
		<div class="featurestext">
			<h3>{title}</h3>
			<h4>{subtitle}</h4>
		</div>
		<div style="height: 40px" />
		<img src={imageSvg} alt="Feature screenshot" width="90%"/>
	</section>
{:else}
	<section>
		{#if isImageOnRight}
			<div class="featurestext">
				<h3>{title}</h3>
				<h4>{subtitle}</h4>
			</div>
			<div class="centerpadding" />
			<div class="featuresimage">
				<img src={imageSvg} alt="Feature screenshot" style="max-width: 90%;"/>
			</div>
		{:else}
			<!-- <div class="featuresimage"> -->
			<div class="featuresimage">
				<img src={imageSvg} alt="Feature screenshot" style="max-width: 90%;"/>
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
	.svgcontainer svg {
		width: 150px;
		height: 150px;
		/* width: 100%;
		height: 100%; */
		z-index: 1; /* Place the SVG above other content */
	}

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
