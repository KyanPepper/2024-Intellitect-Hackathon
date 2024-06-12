<script>
    import { onMount } from "svelte";
    import ResourceCard from "$lib/ResourceCard.svelte";
    
    let testResource = getasource(1);
  </script>
  
  <div class="w-full h-full">
    <ResourceCard {}></ResourceCard>
  </div>