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

  const services = [
    "Financial Stability Center",
    "Health + Wellness",
    "Housing",
    // Add more services here
  ];

  </script>
  
  <div class="bg-white shadow-md rounded-md p-6 mb-4">
    <div class="mb-4">
      <h2 class="text-xl font-semibold">{organization}</h2>
      <p class="text-gray-600">Category: {getCategoryName(category)}</p>
    </div>
    <div class="mb-4">
      <p class="text-gray-800 italic">{description}</p>

      {#each services as service}
      <div class="flex items-center mb-2">
        <div class="flex items-center mb-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 text-green-500" viewBox="0 0 25 25" fill="currentColor">
            <path fill-rule="evenodd" d="M11,16.4l-4.7,-4.7l1.4,-1.4l3.3,3.3l8.4,-8.4c-1.9,-1.9 -4.5,-3.2 -7.4,-3.2c-5.5,0 -10,4.5 -10,10c0,5.5 4.5,10 10,10c5.5,0 10,-4.5 10,-10c0,-1.9 -0.5,-3.6 -1.4,-5.1z"/>
          </svg>
          <p class="text-gray-800">{service}</p>
        </div>
        </div>
    {/each}

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
  