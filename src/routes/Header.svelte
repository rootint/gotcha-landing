<script lang="ts">
	import { NAME } from '../constants';
	import './styles.css';
</script>

<!-- TODO: Mobile! -->
<div class="circle" />
<header>
	<nav>
		<div class="logo">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 437.88 401.12">
				<defs>
					<style>
						.cls-1 {
							fill: #222;
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
			<div style="width: 8px" />
			<p>{NAME}</p>
		</div>
		<div class="back">
			<h4>Home</h4>
			<div style="width: 3rem" />
			<!-- <h4>Pricing</h4> -->
			<!-- <div style="width: 3rem" /> -->
			<button class="header-button">Join Waitlist</button>
		</div>
		<!-- <a class="button-nav" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
	</nav>
</header>

<style>
	.circle {
		width: 654px;
		height: 654px;
		/* background-color: var(--color-theme-3);  */
		background-color: var(--color-theme-3-50);
		border-radius: 50%;
		position: absolute;
		/* transform: translate3d(0, 0, 0); */
		/* display: flex;
        justify-content: center;
        justify-self: center; */
        left: 50%;
		transform: translate3d(-50%, -85%, 0); 
		/* transform: translate3d(50%, -100%, 0); */
		filter: blur(50px);
		z-index: -1;
	}

	@media (max-width: 768px) {
		.circle {
			width: 150px;
			height: 150px;
			background-color: var(--color-theme-3); /* Set the background color of the circle */
			border-radius: 50%; /* Makes the element a circle */
			position: absolute;
			/* top: -300px;
			left: 50%; */
			/* left: 50%; */
			/* transform: translateX(-50%);  */
			/* transform: translate3d(0, -100%, 0); */
			/* transform: translate3d(50%, 0, 0); */
			/* filter: blur(200px); */
			z-index: -1;
		}
	}

	.header-button {
		padding: 0.75rem 2.5rem;
		background-color: var(--color-theme-2);
		font-weight: 500;
		font-size: 1.25rem;
		font-family: 'Rubik', sans-serif;
		color: #fff;
		border: none;
		border-radius: 12px;
		/* margin-left: 10px; */
		cursor: pointer;
	}
	.back {
		display: flex;
		align-items: center;
	}
	h4 {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 1.25rem;
		color: var(--color-text);
		z-index: 1;
	}
	.logo p {
		font-family: 'Rubik', sans-serif;
		font-weight: 500;
		font-size: 1.25rem;
		color: var(--color-text);
	}
	.logo {
		display: flex;
		align-items: center;
	}
	.logo svg {
		/* Customize logo SVG styles here */
		width: 22px; /* Adjust the size as needed */
		height: 19px;
		/* Add any other SVG styling here */
	}
	nav {
		color: #fff;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin: 0 0;
		padding-top: 12px;
	}
</style>
