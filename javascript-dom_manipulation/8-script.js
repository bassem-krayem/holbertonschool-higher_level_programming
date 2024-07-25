document.addEventListener("DOMContentLoaded", async function () {
  try {
    // Fetch data from the API
    let response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
    // Parse the response as JSON
    let data = await response.json();
    // Display the fetched data
    displayHello(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});

function displayHello(data) {
  // Get the container where the data will be displayed
  let container = document.getElementById("hello");

  // Display the "hello" translation
  container.textContent = data.hello;
}
