let change_color = document.getElementById("red_header");

function header_color_change() {
  change_color.style.color = "#FF0000";
}

change_color.addEventListener("click", header_color_change);
