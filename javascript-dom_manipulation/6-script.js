async function fetchData() {
  try {
    // Fetch data from the API
    let response = await fetch(
      "https://swapi-api.hbtn.io/api/people/5/?format=json"
    );
    // Parse the response as JSON
    let data = await response.json();
    // Display the fetched data
    displayData(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

function displayData(data) {
  // Get the container where the data will be displayed
  let container = document.getElementById("character");

  container.textContent = `Character: ${data.name}`;
}

fetchData();
