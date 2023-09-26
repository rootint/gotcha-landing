<script lang="ts">
	import EmailButton from './EmailButton.svelte';
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;

	let email = '';
	let message = '';
	let isEmailValid = false;
	let isPopupVisible = false;
	let buttonText = 'Request A Demo';

	const handleSubmit = async () => {
		try {
			buttonText = 'Loading...';
			const response = await fetch('https://RNDRandoM.pythonanywhere.com/submit', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ name: 'gotcha', email: email }) // Modify the data as needed
			});
			if (response.ok) {
				const data = await response.json();
				console.log(data);
				email = '';
				// isPopupVisible = true;
				isEmailValid = false;
				buttonText = 'Request A Demo';
				alert('Your email was sent successfully!');
			} else {
				// Handle error cases
				console.error('POST request failed');
				buttonText = 'Request A Demo';
				isEmailValid = false;
				alert("Can't send the email, please try again later.");
			}
		} catch (error) {
			console.error('Error:', error);
		}
	};

	// Function to validate the email input
	function validateEmail() {
		const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
		isEmailValid = emailRegex.test(email);
	}

	function closePopup() {
		isPopupVisible = false;
	}

	function doNothing() {}
</script>

{#if isMobile}
	<section class="mobile">
		<h1 class="mobile">{title}</h1>
		<h2 class="mobile">{subtitle}</h2>
		<div style="height: 40px" />
		<!-- <a class="button mobile" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
		<EmailButton {isMobile} />
		<div style="height: 40px" />
		<img src="heroimage.png" alt="heroimage" class="herofgimage mobile" />
	</section>
{:else}
	<section class="desktop">
		<div class="herotext">
			<h1>{title}</h1>
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
	section.desktop {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
		margin: 0;
		width: 100%;
	}
	a.mobile {
		max-width: 50%;
		font-size: 1.2rem;
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
