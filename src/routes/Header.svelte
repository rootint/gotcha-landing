<script lang="ts">
	import { NAME } from '../constants';
	import './styles.css';
</script>

<header>
	<nav>
		<div class="logo">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 437.88 401.12">
				<defs>
					<style>
						.cls-1 {
							fill: #fff;
						}
					</style>
				</defs>
				<g id="Слой_2" data-name="Слой 2">
					<g id="Слой_1-2" data-name="Слой 1">
						<path
							class="cls-1"
							d="M430.26,94.92,322.18,160.45a15.82,15.82,0,0,1-24-13.52V15.85a15.82,15.82,0,0,1,24-13.53L430.27,67.87A15.82,15.82,0,0,1,430.26,94.92ZM237.47,0H204.65a18.52,18.52,0,0,0-18.52,18.52v254.6H186a58,58,0,1,1-61.59-57.88c1.21-.08,2.42-.11,3.61-.11a18.44,18.44,0,0,0,18.29-18.52V163.46a18.26,18.26,0,0,0-18.11-18.33H128a128,128,0,1,0,3.38,256C201,399.29,256,341.38,256,271.78V18.53A18.52,18.52,0,0,0,237.47,0Z"
						/>
					</g>
				</g>
			</svg>
			<div style="width: 12px" />
			<p>{NAME}</p>
		</div>
		<h4>Home</h4>
		<!-- <a class="button-nav" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
	</nav>
</header>

<style>
	.logo p {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 1rem;
		color: var(--color-text);
	}
	.logo {
		display: flex;
		align-items: center;
	}
	.logo svg {
		/* Customize logo SVG styles here */
		width: 24px; /* Adjust the size as needed */
		height: 24px;
		/* Add any other SVG styling here */
	}
	.button-nav {
		display: inline-block;
		padding: 8px 32px;
		font-size: 1rem;
		font-weight: 500;
		font-family: 'Rubik', sans-serif;
		color: #fff;
		background-color: black;
		border: none;
		border-radius: 12px;
		cursor: pointer;
		text-decoration: none;
		transition: background-color 0.1s ease-in-out;
	}
	nav {
		color: #fff;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 0;
	}
	/* nav {
		color: #fff;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 auto 0;
		padding: 0 15%;
		max-width: 70rem;
	} */
</style>
