<script>
import axios from "axios";
const backendprefix = "/localhost:5000/"

let text = "Server Is ";
//Example of a axios request

  axios.get(backendprefix + "test")
  .then((response) => {
    text += response.data;
  })
  .catch((error) => {
    console.error(error);
    text += "Down";
  });

</script>

<div>
  {text}
</div>

