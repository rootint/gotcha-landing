<script lang="ts">
	import './styles.css';

	// export let emoji: string;
	// export let title: string;
	// export let subtitle: string;
	export let isMobile: boolean;
</script>

{#if isMobile}
	<div style="height: 5rem;" />
	<div class="cards mobile">
		<div class="card-wrapper mobile">
			<div class="card">
				<p class="emoji">✏️</p>
				<div style="height: 1.5rem" />
				<p class="header">Let AI edit your<br />videos</p>
				<div style="height: 1.5rem" />
				<p class="description mobile">
					Add captions, B-rolls, effects and adjust color balance in no time using AI.
				</p>
			</div>
		</div>
        <div style="height: 1rem;" />
		<div class="card-wrapper mobile">
			<div class="card">
				<p class="emoji">🪄</p>
				<div style="height: 1.5rem" />
				<p class="header">Get feedback with GotchaBack</p>
				<div style="height: 1.5rem" />
				<p class="description">
					Get valuable feedback on your video and edit it without rerecording using deepfakes.
				</p>
			</div>
		</div>
        <div style="height: 1rem;" />
		<div class="card-wrapper mobile">
			<div class="card right">
				<p class="emoji">🚀</p>
				<div style="height: 1.5rem" />
				<p class="header">Make your video<br />viral</p>
				<div style="height: 1.5rem" />
				<p class="description">
					Our AI is trained on thousands of viral videos to make your video as viral as possible.
				</p>
			</div>
		</div>
	</div>
	<div style="height: 4rem" />
{:else}
	<div style="height: 5rem;" />
	<div class="cards">
		<div class="card-wrapper">
			<div class="card">
				<p class="emoji">✏️</p>
				<div style="height: 1.5rem" />
				<p class="header">Let AI edit your<br />videos</p>
				<div style="height: 1.5rem" />
				<p class="description">
					Add captions, B-rolls, effects and adjust color balance in no time using AI.
				</p>
			</div>
		</div>
		<div class="card-wrapper center">
			<div class="card">
				<p class="emoji">🪄</p>
				<div style="height: 1.5rem" />
				<p class="header">Get feedback with GotchaBack</p>
				<div style="height: 1.5rem" />
				<p class="description">
					Get valuable feedback on your video and edit it without rerecording using deepfakes.
				</p>
			</div>
		</div>
		<div class="card-wrapper right">
			<div class="card right">
				<p class="emoji">🚀</p>
				<div style="height: 1.5rem" />
				<p class="header">Make your video<br />viral</p>
				<div style="height: 1.5rem" />
				<p class="description">
					Our AI is trained on thousands of viral videos to make your video as viral as possible.
				</p>
			</div>
		</div>
	</div>
	<div style="height: 8rem" />
{/if}

<style>
	.description {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 1.5rem;
		color: var(--color-text);
		z-index: 1;
	}
    .description.mobile {
		font-family: 'Rubik', sans-serif;
		font-weight: 400;
		font-size: 1.25rem;
		color: var(--color-text);
		z-index: 1;
	}
	.header {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 2rem;
		color: var(--color-text);
		z-index: 1;
	}
	.emoji {
		font-size: 2.5rem;
		padding: 0;
		margin: 0;
	}
	.cards {
		display: flex;
		align-items: center;
        justify-content: center;
	}
	.cards.mobile {
		display: flex;
		flex-direction: column;
	}
	.card-wrapper {
		background-color: rgba(222, 69, 74, 0.5);
		/* background-color: linear-gradient(to bottom right, #de454a, #454ade); */
		/* background-color: linear-gradient(to left top, blue, red); */
		width: calc(33% - 0.5rem);
		margin-right: 1.5rem;
		border-radius: 12px;
	}

	.card-wrapper.mobile {
		background-color: rgba(222, 69, 74, 0.5);
		/* background-color: linear-gradient(to bottom right, #de454a, #454ade); */
		/* background-color: linear-gradient(to left top, blue, red); */
		width: 100%;
        margin: 0;
		/* margin-right: 10rem; */
		border-radius: 12px;
	}
	.card {
		/* background-color: linear-gradient(to bottom right, #de454a, #454ade); */
		background-color: #fff;
		background-color: linear-gradient(to left top, blue, red);
		/* background-color: linear-gradient(to bottom right, var(--color-theme-2), var(--color-theme-1)); */
		border-radius: 11px;
		margin: 1px;
		padding: 1.5rem;
	}
	.card-wrapper.right {
		background-color: rgba(74, 222, 69, 0.5);
		margin-right: 0rem;
	}
	.card-wrapper.center {
		background-color: rgba(69, 74, 222, 0.5);
	}
	p {
		margin: 0;
		padding: 0;
	}
</style>
