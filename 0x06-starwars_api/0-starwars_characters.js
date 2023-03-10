#!/usr/bin/node

const request = require('request');
const { exit } = require('process');
const filmId = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

if (filmId === undefined) {
  console.log('Usage: node 0-starwars_characters.js <film id>');
  exit();
}

// GET film data
request(api, (error, response, body) => {
  if (error) {
    console.log('error', error);
  } else {
    const data = JSON.parse(body).characters;
    printSorted(data, 0);
  }
});

// GET each character in sorted order
function printSorted (chars, n) {
  if (n === chars.length) { return; }
  request(chars[n], (error, response, actors) => {
    if (error) {
      console.log('error', error);
    } else {
      const actor = JSON.parse(actors);
      console.log(actor.name);
      printSorted(chars, n + 1);
    }
  });
}
