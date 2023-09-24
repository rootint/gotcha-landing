<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;

	let email = '';
	let message = '';

	const handleSubmit = async () => {
		try {
			const response = await fetch('https://RNDRandoM.pythonanywhere.com/submit', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ name: 'testing1', email: email }) // Modify the data as needed
			});

			if (response.ok) {
				const data = await response.json();
				console.log(data);
			} else {
				// Handle error cases
				console.error('POST request failed');
			}
		} catch (error) {
			console.error('Error:', error);
		}
	};
</script>

<section>
	<h1 style="text-align: center">{title}</h1>
	<h2 style="text-align: center">
		{subtitle}
	</h2>
	<div style="height: 40px" />
	<input type="text" bind:value={email} placeholder="Email" />
	<div style="width: 30%;">
		<a class="button" on:click={handleSubmit}>Request A Demo</a>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
