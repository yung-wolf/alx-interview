#!/usr/bin/env node

const request = require('request');
const rp = require('request-promise');

// Check if the user has provided a movie ID as a command line argument.
// If not, print an error message and exit the program.
if (process.argv.length < 3) {
  console.error('Usage:  ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}
// construct the URL for the API call by concatenating the base URL with the
// movie ID provided as a command line argument
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
const url = `${baseUrl}${movieId}/`;

request(url, { json: true }, function (error, response, body) {
  // if there is an error, print an error message and exit the program
  if (error) {
    console.error(error);
    return;
  }

  // if response is not 200, print an error message and exit the program
  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  }

  // store the data in a variable
  const characters = body.characters;

  // function to fetch character names
  async function fetchCharacterNames (characterUrls) {
    for (const characterUrl of characterUrls) {
      try {
        const character = await rp({ uri: characterUrl, json: true });
        console.log(character.name);
      } catch (error) {
        console.error('Error fetching character data:', error);
      }
    }
  }

  fetchCharacterNames(characters);
});
