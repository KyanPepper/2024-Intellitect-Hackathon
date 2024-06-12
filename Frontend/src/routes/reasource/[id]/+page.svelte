<script>
  import Reasourcecard from "$lib/reasourcecard.svelte";
// @ts-ignore
import("./+page").PageData;
  export let data;
  // @ts-ignore
  let project = data.project;
</script>

<div>
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
    />
</div>