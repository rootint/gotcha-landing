<script lang="ts">
	import { onDestroy } from 'svelte';
	import EmailButton from './EmailButton.svelte';
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;

	let currentWordIndex = 0;
	const words = ['Shorts', 'Reels', 'Tiktoks']; // List of words to cycle through

	// Function to update the displayed word
	function updateWord() {
		currentWordIndex = (currentWordIndex + 1) % words.length;
	}

	// Call the updateWord function at a regular interval (e.g., every 3 seconds)
	const interval = setInterval(updateWord, 2000);

	// Cleanup the interval when the component is destroyed
	onDestroy(() => {
		clearInterval(interval);
	});
</script>

{#if isMobile}
	<section class="mobile">
		<h1 class="mobile" style="margin-bottom: 0;">
			<div class="herotext">
				<h1>
					Go viral with your <p class="scroll-text">
						{#if currentWordIndex === 0} {words[0]} {/if}
						{#if currentWordIndex === 1} {words[1]} {/if}
						{#if currentWordIndex === 2} {words[2]} {/if}
					</p>
				</h1>
			</div>
		</h1>
		<h2 class="mobile" style="margin-top: 0;">{subtitle}</h2>
		<div style="height: 40px" />
		<!-- <a class="button mobile" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
		<EmailButton {isMobile} />
		<div style="height: 40px" />
		<img src="heroimage.png" alt="heroimage" class="herofgimage mobile" />
	</section>
{:else}
	<section class="desktop">
		<div class="herotext">
			<h1>
				Go viral with your <p class="scroll-text">
					{#if currentWordIndex === 0} {words[0]} {/if}
					{#if currentWordIndex === 1} {words[1]} {/if}
					{#if currentWordIndex === 2} {words[2]} {/if}
				</p>
			</h1>

			<h2>{subtitle}</h2>
			<div style="height: 40px" />
			<EmailButton {isMobile} />
		</div>
		<div class="centerpadding" />
		<div class="heroimage">
			<p class="background" />
			<img src="heroimage.png" alt="heroimage" class="herofgimage" />
		</div>
	</section>

	<!-- Popup container -->
	<!-- <div class="popup-container" style="display: {isPopupVisible ? 'block' : 'none'};">
		<span class="popup-close-button" on:click={closePopup}>X</span>
		<p>Your email has been sent successfully!</p>
	</div> -->
{/if}

<style>
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
