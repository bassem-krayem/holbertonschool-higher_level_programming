async function fetchMovies() {
  try {
    // Fetch data from the API
    let response = await fetch(
      "https://swapi-api.hbtn.io/api/films/?format=json"
    );
    // Parse the response as JSON
    let data = await response.json();
    // Display the fetched data
    displayMovies(data.results);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

function displayMovies(movies) {
  // Get the container where the data will be displayed
  let container = document.getElementById("list_movies");

  // Iterate over the movies and create list items for each movie
  movies.forEach((movie) => {
    // Create a li element for the movie
    let listItem = document.createElement("li");
    listItem.textContent = movie.title;

    // Append the list item to the container
    container.appendChild(listItem);
  });
}

// Fetch and display the movies when the script loads
fetchMovies();
