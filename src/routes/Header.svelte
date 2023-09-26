<script lang="ts">
	import { NAME } from '../constants';
	import './styles.css';
</script>

<header>
	<nav>
		<h4>{NAME}</h4>
        <h4>Home</h4>
		<!-- <a class="button-nav" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a> -->
	</nav>
</header>

<style>
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
