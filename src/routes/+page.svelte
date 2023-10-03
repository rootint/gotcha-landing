<script>
	import { NAME } from '../constants';
	import { DESCRIPTION } from '../constants';
	import CallToAction from './CallToAction.svelte';
	import Cards from './Cards.svelte';
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
					body: JSON.stringify({ name: 'gotcha' }) // Modify the data as needed
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
	title="Edit your talking head videos effortlessly🪄"
	subtitle="AI-generated captions, effects, and even deepfakes!"
	{isMobile}
/>

<Cards {isMobile} />

<Features1
	title="Edit your videos in "
	subtitle="Just upload your video to Gotcha, and we'll handle all the heavy lifting, including adding captions and effects, ensuring sound and color balance, and more!"
	titleSpan="one click"
	isImageOnRight={false}
	imageSvg="title.png"
	{isMobile}
/>

<Features1
	title="See your most frequent "
	subtitle="With Gotcha, you have access to AI-powered feedback that points out how to make your videos even better."
	titleSpan="mistakes"
	isImageOnRight={true}
	imageSvg="insights.png"
	{isMobile}
/>

<CallToAction
	title="Ready to Skyrocket Your Videos?"
	subtitle="Sign up now and edit 3 free videos with Gotcha!"
	{isMobile}
/>

<style>
</style>
