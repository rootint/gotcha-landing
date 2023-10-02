<script lang="ts">
	import { onDestroy } from 'svelte';
	import EmailButton from './EmailButton.svelte';
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;
</script>

{#if isMobile}
	<section class="mobile">
		<h1 class="mobile" style="margin-bottom: 0;">
			<div class="herotext">
				<h1>Edit your talking head videos effortlessly🪄</h1>
			</div>
		</h1>
		<h2 class="mobile" style="margin-top: 0;">{subtitle}</h2>
		<div style="height: 40px" />
		<!-- <a class="button mobile" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
		<EmailButton {isMobile} />
		<div style="height: 40px" />
		<img src="title.png" alt="heroimage" class="herofgimage mobile" />
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
			<iframe
				width="550"
				height="275"
				style="border-radius: 12px;"
				src="https://www.youtube.com/embed/8DPrtJ_e2rk?si=h-uYcRaeRyLA2QAk"
				title="YouTube video player"
				allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
				allowfullscreen
			/>
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
		width: 654px; /* Adjust the size of the circle as needed */
		height: 654px; /* Adjust the size of the circle as needed */
		background-color: var(--color-theme-1); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
		left: 30%;
		top: 60px;
		transform: translateX(-50%); /* Center the circle horizontally */
		filter: blur(200px);
		z-index: -1;
	}
	.circle-red {
		width: 654px; /* Adjust the size of the circle as needed */
		height: 654px; /* Adjust the size of the circle as needed */
		background-color: var(--color-theme-2); /* Set the background color of the circle */
		border-radius: 50%; /* Makes the element a circle */
		position: absolute;
		left: 80%;
		top: 60px;
		transform: translateX(-70%); /* Center the circle horizontally */
		filter: blur(200px);
		z-index: -1;
	}
	.aspect-ratio {
		position: relative;
		width: 100%;
		height: 0;
		padding-bottom: 56%; /* The height of the item will now be 56% of the width. */
	}

	.aspect-ratio iframe {
		position: absolute;
		width: 100%;
		height: 100%;
		left: 0;
		top: 0;
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

	h2.hero {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 2.25rem;
		color: var(--color-text);
		z-index: 1;
		text-align: center;
		margin: 0;
	}

	img.mobile {
		width: 100%;
	}
	.scroll-text {
		animation: changeWord 2s ease-in infinite;
		color: black;
	}

	@keyframes changeWord {
		0% {
			opacity: 0;
		}
		33.33% {
			opacity: 1;
		}
		66.66% {
			opacity: 1;
		}
		100% {
			opacity: 0;
		}
	}
	section.desktop {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		margin: 0;
		width: 100%;
	}

	p {
		margin: 0;
		padding: 0;
	}

	.herotext {
		flex: 0.5;
		justify-content: center;
		align-items: center;
	}

	.heroimage {
		/* position: relative; */
		height: 50vh;
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
