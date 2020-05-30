/* eslint-disable */

import "../assets/img/rigo-baby.jpg";
import "../assets/img/4geeks.ico";
//import 'breathecode-dom'; //DOM override to make JS easier to use
import "../style/index.scss";

window.onload = async function() {
  const response = await fetch(
    "https://3000-a1ac14a2-1bbc-4ae5-85a4-8773533b8876.ws-us02.gitpod.io/api/excuse"
  );
  let response_object = await response.json();
  document.querySelector(".alert").innerHTML = response_object;
};
