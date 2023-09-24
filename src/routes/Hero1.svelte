<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;
</script>

<section>
	<div class="herotext">
		<h1>{title}</h1>
		<h2>{subtitle}</h2>
		<div style="height: 40px" />
		<a class="button" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a>
	</div>
    <div class="centerpadding"/>
	<div class="heroimage">
		<p class="background" />
		<img src="heroimage.png" alt="heroimage" class="herofgimage" />
	</div>
</section>

<style>
	section {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
		margin: 0;
		width: 100%;
		/* background-color: aqua; */
	}

	p {
		margin: 0;
		padding: 0;
	}

	.mainbutton {
		display: inline-block;
		padding: 12px 56px;
		font-size: 26px;
		font-weight: 500;
		font-family: 'InterVariable', sans-serif;
		color: #fff;
		/* background-color: var(--color-theme-1); */
		background: linear-gradient(to bottom right, var(--color-theme-1), var(--color-theme-2));
		border: none;
		border-radius: 16px;
		cursor: pointer;
		text-decoration: none;
		transition: background-color 0.1s ease-in-out;
	}
	.mainbutton:hover {
		filter: brightness(70%);
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
		position: absolute;
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
