#!/usr/bin/node

const request = require('request');

const filmNumb = process.argv[2] + '/';

const filmsURL = 'https://swapi-api.hbtn.io/api/films/';

request(filmsURL + filmNumb, async function (errr, ress, bodyy) {
  if (errr) return console.error(errr);

  const charURLListts = JSON.parse(bodyy).characters;

  for (const charsURL of charURLListts) {
    await new Promise(function (resolve, reject) {
      request(charsURL, function (errr, ress, bodyy) {
        if (errr) return console.error(errr);

        console.log(JSON.parse(bodyy).name);

        resolve();
      });
    });
  }
});
