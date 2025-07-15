#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    for (let i = 0; i < data.results.length; i++) {
      const item = document.createElement('li');
      item.textContent = data.results[i].title;
      document.querySelector('#list_movies').appendChild(item);
    }
  });
