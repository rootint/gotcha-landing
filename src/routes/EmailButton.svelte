<script lang="ts">
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

	function doNothing() {}
</script>

{#if isMobile}
	<div class="emailcontainer mobile">
		<input
			type="email"
			bind:value={email}
			on:input={validateEmail}
			class="email-input"
			placeholder="example@mail.com"
		/>
		<button
			class="emailbutton {isEmailValid ? '' : 'inactive'}"
			on:click={isEmailValid ? handleSubmit : doNothing}>{buttonText}</button
		>
	</div>
{:else}
	<div class="emailcontainer">
		<input
			type="email"
			bind:value={email}
			on:input={validateEmail}
			class="email-input"
			placeholder="example@mail.com"
		/>
		<button
			class="emailbutton {isEmailValid ? '' : 'inactive'}"
			on:click={isEmailValid ? handleSubmit : doNothing}>{buttonText}</button
		>
	</div>
{/if}

<style>
	.emailcontainer.mobile {
		display: flex;
		flex-direction: column;
		background-color: black;
		border-radius: 16px;
	}
	.emailcontainer {
		display: inline-block;
		/* flex-direction: row; */
		background-color: black;
		border-radius: 16px;
	}

	.emailbutton {
		padding: 10px 24px;
		background-color: white;
		font-weight: 500;
		font-size: 1.2rem;
		min-width: 13rem;
		font-family: 'Rubik', sans-serif;
		color: black;
		border: none;
		border-radius: 12px;
		margin: 16px;
		/* margin-left: 10px; */
		cursor: pointer;
	}

	.emailbutton.inactive {
		cursor: not-allowed; /* Change cursor to not-allowed */
		opacity: 0.6; /* Reduce opacity to indicate inactivity */
	}

	/* Style for the email input */
	.email-input {
		padding: 24px;
		/* border: 1px solid #ccc; */
		background-color: black;
		border: none;
		color: white;
		border-radius: 12px;
		font-size: 1.2rem;
		font-family: 'Rubik', sans-serif;
	}
</style>
