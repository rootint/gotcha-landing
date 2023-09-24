<script>
	import { NAME } from '../constants';
	import { DESCRIPTION } from '../constants';
	import CallToAction from './CallToAction.svelte';
	import Features1 from './Features1.svelte';
	import Hero1 from './Hero1.svelte';
</script>

<svelte:head>
	<title>{NAME}</title>
	<meta name="description" content={DESCRIPTION} />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
	<link
		href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<Hero1
	title="Speak directly to your data."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips."
/>

<Features1
	title="Amazing feature 1. Lorem ipsum dolor sit amet blah blah."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips.Artificial Intelligence-driven data analysis at your fingertips."
	isImageOnRight={false}
	imageUrl="heroimage.png"
/>

<Features1
	title="Amazing feature 2. Lorem ipsum dolor sit amet blah blah."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips. Artificial Intelligence-driven data analysis at your fingertips.Artificial Intelligence-driven data analysis at your fingertips."
	isImageOnRight={true}
	imageUrl="heroimage.png"
/>

<CallToAction
	title="Speak directly to your data."
	subtitle="Artificial Intelligence-driven data analysis at your fingertips."
/>

<style>
</style>
