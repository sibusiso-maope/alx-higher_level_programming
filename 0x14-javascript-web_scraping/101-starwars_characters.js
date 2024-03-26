#!/usr/bin/node

const req = require('request');

function getDataFrom (url) {
  return new Promise(function (resolve, reject) {
    req(url, function (err, _res, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function errHandler (err) {
  console.log(err);
}

function printMovieCharacters (movieId) {
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  getDataFrom(movieUri)
    .then(JSON.parse, errHandler)
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      for (let k = 0; k < characters.length; ++k) {
        promises.push(getDataFrom(characters[k]));
      }

      Promise.all(promises)
        .then((results) => {
          for (let k = 0; k < results.length; ++k) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

printMovieCharacters(process.argv[2]);
