<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isImageOnRight: boolean;
	// export let imageUrl: string;
	export let isMobile: boolean;
	export let imageSvg: string;
	export let titleSpan: string;
</script>

{#if isMobile}
	<section class="mobile">
		<div class="featurestext">
			<h3>{title}</h3>
			<h4>{subtitle}</h4>
		</div>
		<div style="height: 40px" />
		<img src={imageSvg} alt="Feature screenshot" width="90%" />
	</section>
{:else}
	<section>
		{#if isImageOnRight}
			<div class="featurestext">
				<h3>
					{title}
					<span style="color: var(--color-theme-2);">{titleSpan}</span>
				</h3>
				<h4>{subtitle}</h4>
			</div>
			<div class="centerpadding" />
			<div class="featuresimage">
				<img src={imageSvg} alt="Feature screenshot" style="max-width: 90%;" />
			</div>
			<div class="circle-blue" />
		{:else}
			<!-- <div class="featuresimage"> -->
			<div class="circle-red" />
			<div class="featuresimage">
				<img src={imageSvg} alt="Feature screenshot" style="max-width: 90%;" />
			</div>
			<div class="centerpadding" />
			<div class="featurestext">
				<h3>
					{title}
					<span style="color: var(--color-theme-1);">{titleSpan}</span>
				</h3>
				<h4>{subtitle}</h4>
			</div>
		{/if}
	</section>
	<div style="height: 13rem" />
{/if}

<style>
	.circle-red {
		width: 30%;
		aspect-ratio: 1;
		background-color: var(--color-theme-2-50); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
        left: 0;
		/* left: 30%;
		top: 60px; */
		/* transform: translateX(-50%);  */
		filter: blur(50px);
		transform: translate3d(-90%, -10%, 0);
		z-index: -1;
	}
	.circle-blue {
		width: 30%;
		aspect-ratio: 1;
		background-color: var(--color-theme-1-50); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
        right: 0;
		/* left: 30%;
		top: 60px; */
		/* transform: translateX(-50%);  */
		filter: blur(50px);
		transform: translate3d(90%, -10%, 0);
		z-index: 2;
	}
	h4 {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 2.5rem;
		color: var(--color-text);
	}
	h3 {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 4rem;
		color: var(--color-text);
	}

	section {
		display: flex;
		align-items: left;
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
