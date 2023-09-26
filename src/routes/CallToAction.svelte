<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
	export let isMobile: boolean;

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

{#if isMobile}
	<section class="mobile">
		<h1 style="text-align: center" class="mobile">{title}</h1>
		<h2 style="text-align: center" class="mobile">
			{subtitle}
		</h2>
		<div style="height: 40px" />
		<input type="text" bind:value={email} placeholder="Email" />
		<a class="button" on:click={handleSubmit}>Request A Demo</a>
	</section>
{:else}
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
{/if}

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
