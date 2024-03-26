#!/usr/bin/node

const request = require('request');

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function printMovieCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  fetchData(movieUrl)
    .then((movieData) => {
      const movie = JSON.parse(movieData);
      const characterUrls = movie.characters;
      const characterPromises = characterUrls.map((characterUrl) => fetchData(characterUrl));

      return Promise.all(characterPromises);
    })
    .then((charactersData) => {
      charactersData.forEach((characterData) => {
        const character = JSON.parse(characterData);
        console.log(character.name);
      });
    })
    .catch((err) => {
      console.error('Error:', err);
    });
}

const selectedMovieId = process.argv[2];
printMovieCharacters(selectedMovieId);
