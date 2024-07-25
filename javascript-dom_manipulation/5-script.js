let changeHeader = document.getElementById("update_header");
let newHeader = document.getElementsByTagName("header")[0];

function updateHeaderText() {
  newHeader.textContent = "New Header!!!";
}

changeHeader.addEventListener("click", updateHeaderText);
