import React from 'react';

const MovieCard = ({ movie }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      {movie.title && <h3 className="text-xl font-semibold">{movie.title}</h3>}
      {movie.year_released && <p>Year: {movie.year_released}</p>}
      {movie.type && <p>Type: {movie.type}</p>}
      {movie.genre && <p>Genre: {movie.genre}</p>}
      {movie.associated_people && <p>Associated People: {movie.associated_people.join(', ')}</p>}
    </div>
  );
};

export default MovieCard;
