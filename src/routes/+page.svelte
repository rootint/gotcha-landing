<script>
	import { NAME } from '../constants';
	import { DESCRIPTION } from '../constants';
	import CallToAction from './CallToAction.svelte';
	import Features1 from './Features1.svelte';
	import Hero1 from './Hero1.svelte';

	import { onMount } from 'svelte';

	let isMobile = false; // Initialize a variable to store the result

	onMount(async () => {
		if (window.innerWidth <= 768) {
			// Adjust the width threshold as needed
			isMobile = true;
		} else {
			isMobile = false;
		}
		const hasBeenHere = localStorage.getItem('hasBeenHere');
		console.log(hasBeenHere);
		if (!hasBeenHere) {
			try {
				const response = await fetch('https://RNDRandoM.pythonanywhere.com/join', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ name: 'testing1' }) // Modify the data as needed
				});

				if (response.ok) {
					const data = await response.json();
				} else {
					// Handle error cases
					console.error('POST request failed');
				}
			} catch (error) {
				console.error('Error:', error);
			}
			localStorage.setItem('hasBeenHere', 'true');
		}
	});
</script>

<svelte:head>
	<title>{NAME}</title>
	<meta name="description" content={DESCRIPTION} />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<Hero1
	title="Speak directly to your data."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips."
	{isMobile}
/>

<Features1
	title="Amazing feature 1. Lorem ipsum dolor sit amet blah blah."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips.Artificial Intelligence-driven data analysis at your fingertips."
	isImageOnRight={false}
	imageUrl="heroimage.png"
	{isMobile}
/>

<Features1
	title="Amazing feature 2. Lorem ipsum dolor sit amet blah blah."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips.Artificial Intelligence-driven data analysis at your fingertips."
	isImageOnRight={true}
	imageUrl="heroimage.png"
	{isMobile}
/>

<CallToAction
	title="Speak directly to your data."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips."
	{isMobile}
/>

<style>
</style>
