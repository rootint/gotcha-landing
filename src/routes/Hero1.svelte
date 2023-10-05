<script lang="ts">
	import { onDestroy } from 'svelte';
	import EmailButton from './EmailButton.svelte';
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;
	import Youtube from 'svelte-youtube-embed';
</script>

{#if isMobile}
	<section class="mobile">
		<div style="height: 6rem" />
		<h1 class="hero mobile">
			Edit
			<!-- <div id="svg-container">
				<img src="strike.svg" alt="" />
			</div> -->
			your talking head videos
			<span style="color: var(--color-theme-1);">effortlessly</span>🪄
		</h1>

		<div style="height: 2rem" />
		<h2 class="hero mobile">{subtitle}</h2>
		<div style="height: 2rem" />
		<EmailButton {isMobile} />
		<div style="height: 2rem" />
		<div class="aspect-ratio">
			<!-- <div class="circle-blue" />
			<div class="circle-red" /> -->
			<Youtube id="8DPrtJ_e2rk" />
		</div>
		<div style="height: 1rem" />
	</section>
{:else}
	<section class="desktop">
		<div style="height: 14rem" />
		<h1 class="hero">
			Edit <div id="svg-container">
				<img src="strike.svg" alt="" />
			</div>
			your talking head<br />videos
			<span style="color: var(--color-theme-1);">effortlessly</span>🪄
		</h1>

		<div style="height: 2rem" />
		<h2 class="hero">{subtitle}</h2>
		<div style="height: 4rem" />
		<EmailButton {isMobile} />
		<!-- <div class="heroimage"> -->
		<div style="height: 6rem" />
		<div class="aspect-ratio">
			<div class="circle-blue" />
			<div class="circle-red" />
			<!-- <iframe
				width="550"
				height="275"
				style="border-radius: 12px;"
				src="https://www.youtube.com/embed/8DPrtJ_e2rk?si=h-uYcRaeRyLA2QAk"
				title="YouTube video player"
				allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
				allowfullscreen
			/> -->
			<Youtube id="8DPrtJ_e2rk" />
		</div>
		<div style="height: 4rem" />
		<!-- <p class="background" />
			<img src="title.png" alt="heroimage" class="herofgimage" /> -->
		<!-- </div> -->
	</section>

	<!-- Popup container -->
	<!-- <div class="popup-container" style="display: {isPopupVisible ? 'block' : 'none'};">
		<span class="popup-close-button" on:click={closePopup}>X</span>
		<p>Your email has been sent successfully!</p>
	</div> -->
{/if}

<style>
	.circle-blue {
		width: 650px;
		height: 650px;
		background-color: var(--color-theme-1-50); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
		left: 50%;
		/* left: 30%;
		top: 60px; */
		/* transform: translateX(-50%);  */
		filter: blur(50px);
		transform: translate3d(-85%, -10%, 0);
		z-index: -1;
	}
	.circle-red {
		width: 650px; /* Adjust the size of the circle as needed */
		height: 650px; /* Adjust the size of the circle as needed */
		background-color: var(--color-theme-2-50); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
		left: 50%;
		/* transform: translateX(-70%);  */
		filter: blur(50px);
		/* transform: translate3d(0, 0, 0); */
		transform: translate3d(-15%, -10%, 0);
		z-index: -1;
	}
	.aspect-ratio {
		position: relative;
		width: 100%;
		height: 0;
		padding-bottom: 56%; /* The height of the item will now be 56% of the width. */
	}
	#svg-container {
		position: absolute;
		top: 7rem;
		/* left: 13rem; */
		transform: translateX(-42%);
		z-index: 2; /* SVG should be above the content */
	}
	/* Styles for screens up to 600px wide (small screens) */
	@media (max-width: 900px) {
		#svg-container {
			position: absolute;
			top: 7rem;
			/* transform: translateX(-42%); */
			z-index: 2; /* SVG should be above the content */
		}
	}
	h1.hero {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 5.5rem;
		color: var(--color-text);
		z-index: 1;
		text-align: center;
		margin: 0;
	}
	h1.hero.mobile {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 2.5rem;
		color: var(--color-text);
		z-index: 1;
		text-align: center;
		margin: 0;
	}
	h2.hero {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 2.25rem;
		color: var(--color-text);
		z-index: 1;
		text-align: center;
		margin: 0;
	}
	h2.hero.mobile {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 1.5rem;
		color: var(--color-text);
		z-index: 1;
		text-align: center;
		margin: 0;
	}
	section.desktop {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin: 0;
		width: 100%;
	}
	section.mobile {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin: 0;
		width: 100%;
	}
</style>
