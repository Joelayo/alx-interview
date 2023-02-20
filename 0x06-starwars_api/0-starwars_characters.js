#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log('Invalid Status Code Returned:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach(function (characterUrl) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.log('Error:', error);
        } else if (response.statusCode !== 200) {
          console.log('Invalid Status Code Returned:', response.statusCode);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
