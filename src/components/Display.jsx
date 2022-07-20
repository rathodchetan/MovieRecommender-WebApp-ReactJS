import React from "react";

function Display(props) {
    if (props.movieTitles.length === 0) {
        return <div>Movie not in database</div>
    }
    return (
        <div className="recommend">
            <div className="movieCard">
                <p>{props.movieTitles[0]}</p>
                <img src={props.movieTitles[1]} alt="moviePoster" className="poster" />
            </div>
            <div className="movieCard">
                <p>{props.movieTitles[2]}</p>
                <img src={props.movieTitles[3]} alt="moviePoster" className="poster" />
            </div><div className="movieCard">
                <p>{props.movieTitles[4]}</p>
                <img src={props.movieTitles[5]} alt="moviePoster" className="poster" />
            </div><div className="movieCard">
                <p>{props.movieTitles[6]}</p>
                <img src={props.movieTitles[7]} alt="moviePoster" className="poster" />
            </div><div className="movieCard">
                <p>{props.movieTitles[8]}</p>
                <img src={props.movieTitles[9]} alt="moviePoster" className="poster" />
            </div>
        </div>
    )
}

export default Display;