let addItem = document.getElementById("add_item");

function addLi() {
  let li_element = document.createElement("li");
  li_element.textContent = "Item";
  let ul = document.getElementsByClassName("my_list")[0];
  ul.appendChild(li_element);
}

addItem.addEventListener("click", addLi);
