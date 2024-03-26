#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles character ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter((film) =>
      film.characters.some((character) => character.endsWith(`/${characterId}/`))
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
