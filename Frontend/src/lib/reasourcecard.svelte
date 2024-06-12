<script>
  
  // @ts-ignore
  import axios, {Axios } from "axios";
    export let id;
    /**
   * @type {any}
   */
     export let organization;
    /**
   * @type {any}
   */
     export let description;
    /**
   * @type {any}
   */
     export let address;
    /**
   * @type {any}
   */
     export let phoneNumber;
    /**
   * @type {any}
   */
     export let email;
    /**
   * @type {any}
   */
     export let website;
    /**
   * @type {any}
   */
     export let category;
    /**
   * @type {any}
   */
     export let lon;
    /**
   * @type {any}
   */
     export let lat;
    /**
   * @type {any}
   */
     export let img;
   
     const categoryNames = {
    1: "Elderly",
    2: "Youth",
    3: "People with Disabilities",
    4: "Homeless",
    5: "Refugees and Asylum Seekers",
    6: "Veterans",
    7: "Recovering Addicts",
  };

  // @ts-ignore
  function getCategoryName(id) {
    // @ts-ignore
    return categoryNames[id] || "Unknown";
  }


  </script>
  
  <div class="bg-white shadow-md rounded-md p-6 mb-4">
    <div class="mb-4">
      <h2 class="text-xl font-semibold">{organization}</h2>
      <p class="text-gray-600">Category: {getCategoryName(category)}</p>
    </div>
    <div class="mb-4">
      <p class="text-gray-800">{description}</p>
      <p class="text-gray-800">Address: {address}</p>
      <p class="text-gray-800">Phone: {phoneNumber}</p>
      <p class="text-gray-800">Email: {email}</p>
      <p class="text-gray-800">Website: {website}</p>
    </div>
    <div>
      {#if lon && lat}
        <p class="text-gray-800">Latitude: {lat}, Longitude: {lon}</p>
      {/if}
      {#if img}
        <img src={img} alt="Image" class="mt-2 rounded-lg" />
      {/if}
    </div>
  </div>
  