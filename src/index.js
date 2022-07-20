import React from "react";
import ReactDOM from "react-dom"
import App from "./components/App.jsx"

const movies = require('./test.json')
const similarity = require('./similarity.json')


const num_movies = Object.keys(movies.title).length
var movie_title = []

for (let i = 0; i < num_movies; i++) {
  movie_title.push(movies.title[i])
}


function movieRecommender(text) {
  const index = movie_title.indexOf(text)
  // console.log(index)
  let movie_title_recommend = []
  // let movie_id_recommend = []
  // let movie_poster = []
  if (index !== -1) {
    // console.log(movie_title[1])
    // console.log(movie_title[similarity[index][3][0]])
    // console.log(similarity[index][3][0])
    // console.log(movies.movie_id[movieRecommendersimilarity[index][3][0]])
    for (let i = 0; i < 5; i++) {
      movie_title_recommend.push(movie_title[similarity[index][i][0]])
      movie_title_recommend.push(movies.poster[similarity[index][i][0]])
      // movie_poster.push(movies.poster[similarity[index][i][0]]);
      // console.log(String(movies.poster[similarity[index][i][0]]));
      // movie_poster.push("https://image.tmdb.org/t/p/w500" + poster);
      // movie_id_recommend.push(movies.movie_id[similarity[index][i][0]])
    }
    // console.log(movie_title_recommend)
    // console.log(movie_poster)
    // console.log(movie_id_recommend);

  }
  // return { movie_id_recommend, movie_title_recommend };
  return movie_title_recommend;

}

ReactDOM.render(<App movieRecommend={movieRecommender} />, document.getElementById("root"));
