#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line argument
const movieId = process.argv[2];

// Make the API request to fetch the movie details
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    // Parse the response body as JSON
    const movieData = JSON.parse(body);

    // Extract the character URLs from the movie data
    const characterURLs = movieData.characters;

    // Make separate API requests for each character to fetch their details
    characterURLs.forEach((characterURL) => {
      request(characterURL, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
        } else if (charResponse.statusCode !== 200) {
          console.error('Status:', charResponse.statusCode);
        } else {
          // Parse the character data and print the name
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});
