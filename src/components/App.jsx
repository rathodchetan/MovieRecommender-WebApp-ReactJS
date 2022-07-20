import React, { useState } from "react";
import Display from "./Display";

function App(props) {

    const [title, setTitle] = useState("");
    // const [moviePosters, setPoster] = useState([]);
    const [movieTitles, setTitles] = useState([]);
    const [display, setDisplay] = useState(true);
    function handleChange(event) {
        const newTitle = event.target.value;
        // console.log(newTitle)
        setTitle(newTitle);
    }
    function handleClick(event) {
        // const { movie_posters, movie_title_recommend } = props.movieRecommend(title);
        // console.log(movie_id_recommend);
        // console.log(movie_title_recommend)
        const movie_title_recommend = props.movieRecommend(title);
        // setPoster(movie_posters);
        setTitles(movie_title_recommend);
        setDisplay(false);
        // console.log(movieIds);
        // console.log(movieTitles);
        // console.log(movieTitles)

    }
    // { props.movieRecommend("The Fast and the Furious") };
    return (<div>
        <input
            name="movieTitle"
            onChange={handleChange}
            placeholder='Title'
            className="input"
        />
        <button onClick={handleClick} className="button">Recommend</button>
        {/* <p>{movieIds}</p>
        <p>{movieTitles}</p> */}
        <div hidden={display}><Display movieTitles={movieTitles} /></div>
        {/* moviePoster={moviePosters} */}
    </div>);
}
export default App;