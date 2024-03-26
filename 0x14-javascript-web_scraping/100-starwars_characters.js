#!/usr/bin/node

const req = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

req(starWarsUri, function (_err, _res, body) {
  const characters = JSON.parse(body).characters;

  for (let k = 0; k < characters.length; ++k) {
    req(characters[k], function (_cErr, _cRes, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
