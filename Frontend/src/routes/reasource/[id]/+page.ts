import type { PageLoad } from './$types';
const backendprefix = "http://127.0.0.1:5000/";

export const load: PageLoad = async ({ fetch,params }) => {
  try {
    const response = await fetch(`${backendprefix}getreasource/${params.id}`);
    if (!response.ok) {
      console.log('response:', response);
      throw new Error(`Failed to fetch data: ${response.status}`);
    }
    const data = await response.json();
    console.log('good:', data);
    return { project: data };
  } catch (error) {
    console.error('Error fetching random projects during SSR:', error);
    return { project: null };
  }
};