<script>
    // @ts-nocheck
  
    import { onMount, onDestroy } from "svelte";
    import { browser } from "$app/environment";
  
/**
 * Create a card component to display resource information.
 * @param {Object} resourceData - Object containing resource information.
 * @returns {HTMLElement} - Returns a card element.
 */
  
    onMount(async () => {
      if (browser) {
        // @ts-ignore
        // Create card container
    const card = document.createElement('div');
    card.classList.add('resource-card');

    // Create card content
    const nameElement = document.createElement('h2');
    nameElement.textContent = resourceData.name;

    const descriptionElement = document.createElement('p');
    descriptionElement.textContent = resourceData.description;

    const addressElement = document.createElement('p');
    addressElement.textContent = resourceData.address;

    const phoneNumberElement = document.createElement('p');
    phoneNumberElement.textContent = resourceData.phoneNumber;

    const emailElement = document.createElement('p');
    emailElement.textContent = resourceData.email;

    const websiteElement = document.createElement('a');
    websiteElement.href = resourceData.website;
    websiteElement.textContent = 'Visit Website';

    // Append content to card
    card.appendChild(nameElement);
    card.appendChild(descriptionElement);
    card.appendChild(addressElement);
    card.appendChild(phoneNumberElement);
    card.appendChild(emailElement);
    card.appendChild(websiteElement);

    return card;
      }
    });
  
    onDestroy(async () => {
      if (map) {
        console.log("Unloading Leaflet map.");
        map.remove();
      }
    });
  </script>