#!/usr/bin/node

/**
 * Prints all characters of a Star Wars movie.
 * 
 * The first positional argument passed is the Movie ID.
 * Displays one character name per line in the same order as the “characters” list in the /films/ endpoint.
 * 
 * Usage: ./0-starwars_characters.js <Movie ID>
 * Example: ./0-starwars_characters.js 3
 */

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to get data from API. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to get data from API. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
