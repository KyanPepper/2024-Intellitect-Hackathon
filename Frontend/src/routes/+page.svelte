<script>
import axios from "axios";
const backendprefix = "http://127.0.0.1:5000/"

let text = "Server Is ";
//Example of a axios request

  axios.get(backendprefix + "test")
  .then((response) => {
    text += response.data.message;
    console.log(response);
  })
  .catch((error) => {
    console.error(error);
    text += "Down";
  });

</script>

<div>
  {text}
</div>

