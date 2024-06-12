<script>
const backendprefix = "http://127.0.0.1:5000/"
  // @ts-nocheck

  import { onMount, onDestroy } from "svelte";
  import { browser } from "$app/environment";

  /**
   * @type {string | HTMLElement}
   */
  let mapElement;
  /**
   * @type {import("leaflet").Map | import("leaflet").LayerGroup<any>}
   */
  let mapProjects;
  /**
   * @type {import("leaflet").Map | import("leaflet").LayerGroup<any>}
   */
  let map;

  onMount(async () => {
    if (browser) {
      // @ts-ignore
      try {
        const response = await fetch(backendprefix + "getresources");
        if (!response.ok) {
          throw new Error(`Failed to fetch data: ${response.status}`);
        }
        mapProjects = await response.json();
        console.log(mapProjects);
      } catch (error) {
        console.error("Error fetching map projects:", error);
      }
      const leaflet = await import("leaflet");
      const washingtonBounds = leaflet.latLngBounds(
        leaflet.latLng(47.55, -118), // Southwest corner
        leaflet.latLng(47.8, -117.0)   // Northeast corner


      );
      map = leaflet
        .map(mapElement, {
          maxBounds: washingtonBounds,
          maxBoundsViscosity: 1.0,
          minZoom: 2,
        })
        .setView([47.6851, -117.2401], 5);
      leaflet
        .tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          attribution:
            '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        })
        .addTo(map);
        // @ts-ignore
        for (let i = 0; i < mapProjects.length; i++) {
        // @ts-ignore
        leaflet.marker([mapProjects[i].lat, mapProjects[i].lon]).addTo(map)
          .bindPopup(`<div>
            <a href="reasource/${
// @ts-ignore
            mapProjects[i].id}">
            <h3>${
// @ts-ignore
            mapProjects[i].name}</h3>
            <img src="${
// @ts-ignore
            mapProjects[i].img}" style="width: 100%; height: auto;">
            </a>
          </div>`);
      }
      }
      
  });

  onDestroy(async () => {
    if (map) {
      console.log("Unloading Leaflet map.");
      map.remove();
    }
  });
</script>

<main>
  <div bind:this={mapElement}></div>
</main>

<style>
  @import "leaflet/dist/leaflet.css";
  main div {
    height: 800px;
  }
</style>
