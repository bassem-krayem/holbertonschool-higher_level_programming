let toggle_header = document.getElementById("toggle_header");
let element_to_toggle = document.getElementsByTagName("header")[0];

function toggle_Classes() {
  if (element_to_toggle.classList.contains("green")) {
    element_to_toggle.classList.remove("green");
    element_to_toggle.classList.add("red");
  } else {
    element_to_toggle.classList.remove("red");
    element_to_toggle.classList.add("green");
  }
}

toggle_header.addEventListener("click", toggle_Classes);
