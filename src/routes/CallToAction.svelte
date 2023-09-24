<script lang="ts">
	import './styles.css';

	export let title: string;
	export let subtitle: string;

    function send_email() {
        
    }
</script>

<section>
	<h1 style="text-align: center">{title}</h1>
	<h2 style="text-align: center">
		{subtitle}
	</h2>
	<div style="height: 40px" />
	<div style="width: 30%;">
		<a class="button" href="https://forms.gle/UBCinUCT8mbeWmwr6">Request A Demo</a>
	</div>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
        align-items: center;
	}
</style>
