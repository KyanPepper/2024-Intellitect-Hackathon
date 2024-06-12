<script>
    import Reasourcecard from "$lib/reasourcecard.svelte";
// @ts-ignore
import("./+page").PageData;
  export let data;
  // @ts-ignore
  let projects = data.project;
</script>
<div>
    {#each projects as project}
    <Reasourcecard
        id={project.id}
        organization={project.name}
        description={project.description}
        address={project.address}
        phoneNumber={project.phoneNumber}
        email={project.email}
        website={project.website}
        category={project.category_id}
        lon={project.lon}
        lat={project.lat}
        img={project.img}
        tags={project.tags}
    />
    {/each}
</div>