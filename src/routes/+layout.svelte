<script>
	import { NAME } from '../constants';
	import Header from './Header.svelte';
    import "./styles.css";
</script>

<div class="app">
	<Header />
	<main>
		<slot />
	</main>

	<footer>
		<h4>{NAME}, 2023</h4>
	</footer>
</div>

<style>
    footer {
        padding: 20px 0 12px 0;
    }
</style>

