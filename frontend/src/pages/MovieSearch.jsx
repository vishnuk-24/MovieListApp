import React, { useState } from 'react';
import { searchMovies } from '../config/api';
import MovieCard from '../components/MovieCard';

const MovieSearch = () => {
  const [searchParams, setSearchParams] = useState({ title: '' });
  const [movies, setMovies] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await searchMovies(searchParams);
      setMovies(response.data);
    } catch (error) {
      console.error('Error searching movies:', error);
    }
  };

  return (
    <div className="container mx-auto mt-10 text-center">
      <h2 className="text-2xl font-bold mb-4">Search Movies</h2>
      <form onSubmit={handleSearch} className="mb-6">
        <input
          type="text"
          placeholder="Movie Title"
          value={searchParams.title}
          onChange={(e) => setSearchParams({ ...searchParams, title: e.target.value })}
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Search</button>
      </form>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {movies.map((movie) => (
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>
    </div>
  );
};

export default MovieSearch;