<script lang="ts">
	export let isMobile: boolean;

	let email = '';

	let message = '';
	let isEmailValid = false;
	let buttonText = 'Join Waitlist';

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
				buttonText = 'Join Waitlist';
				alert('Your email was sent successfully!');
			} else {
				// Handle error cases
				console.error('POST request failed');
				buttonText = 'Join Waitlist';
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

	function doNothing() {}
</script>

{#if isMobile}
	<div class="emailcontainer mobile">
		<input
			type="email"
			bind:value={email}
			on:input={validateEmail}
			class="email-input mobile"
			placeholder="Email address..."
		/>
		<div style="height: 16px" />
		<button class="email-button mobile" on:click={isEmailValid ? handleSubmit : doNothing}
			>{buttonText}</button
		>
	</div>
{:else}
	<div class="emailcontainer">
		<input
			type="email"
			bind:value={email}
			on:input={validateEmail}
			class="email-input"
			placeholder="Email address..."
		/>
		<button class="email-button" on:click={isEmailValid ? handleSubmit : doNothing}
			>{buttonText}</button
		>
	</div>
{/if}

<style>
	.emailcontainer.mobile {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	.email-input {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-style: normal;
		font-size: 1.5rem;
		background-color: #fff;
		color: #222;
		padding: 16px;
		margin-right: 24px;
		border-radius: 12px;
		border: 1px solid rgba(0, 0, 0, 0.25);
		width: 30rem;
	}

	.email-input.mobile {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-style: normal;
		font-size: 1rem;
		background-color: #fff;
		color: #222;
		padding: 16px;
		margin-right: 0px;
		border-radius: 12px;
		border: 1px solid rgba(0, 0, 0, 0.25);
		width: 100%;
	}

	.email-input::placeholder {
		font-family: 'Rubik', sans-serif;
		font-weight: 300;
		color: rgba(0, 0, 0, 0.35); /* Optionally change the color of the placeholder text */
	}

	.email-button {
		padding: 1rem 3.5rem;
		background-color: var(--color-theme-2);
		font-weight: 500;
		font-size: 1.5rem;
		font-family: 'Rubik', sans-serif;
		color: #fff;
		border: none;
		border-radius: 12px;
		/* margin-left: 10px; */
		cursor: pointer;
	}
    .email-button.mobile {
		/* padding: 1rem 3.5rem; */
		background-color: var(--color-theme-2);
		font-weight: 500;
		font-size: 1.2rem;
		font-family: 'Rubik', sans-serif;
		color: #fff;
		border: none;
		border-radius: 12px;
        width: 100%;
		cursor: pointer;
	}
</style>
