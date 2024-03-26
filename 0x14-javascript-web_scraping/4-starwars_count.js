#!/usr/bin/node

const req = require('request');
const starWarsUri = process.argv[2];
let times = 0;

req(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let k = 0; k < body.length; ++k) {
    const characters = body[k].characters;

    for (let l = 0; l < characters.length; ++l) {
      const character = characters[l];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
