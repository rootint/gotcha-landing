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
	title="Get Reels viral now"
	subtitle="Elevate your videos with our AI Video Analyzer. Upload, get feedback, and watch them go viral!"
	{isMobile}
/>

<Features1
	title="Instant Virality Predictions"
	subtitle="With Gotcha, you can unlock instant predictions using the power of AI. Wondering if your video will go viral? Gotcha's AI can instantly check and let you know. Don't wait for success – predict it with Gotcha!"
	isImageOnRight={false}
	imageUrl="heroimage.png"
	{isMobile}
/>

<Features1
	title="Refine Your Content with Actionable Insights"
	subtitle="At Gotcha, we go beyond predicting virality; we're here to help you improve your content. Our cutting-edge GotchaBack feature offers in-depth analysis and actionable recommendations to enhance your videos."
	isImageOnRight={true}
	imageUrl="heroimage.png"
	{isMobile}
/>

<CallToAction
	title="Ready to Skyrocket Your Videos?"
	subtitle="Leave us your email to experience the magic for yourself!"
	{isMobile}
/>

<style>
</style>
