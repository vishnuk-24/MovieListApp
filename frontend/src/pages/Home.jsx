import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="container mx-auto mt-10 text-center">
      <h1 className="text-4xl font-bold mb-6">Welcome to Movie List App</h1>
      <div className="space-x-4">
        <Link to="/movies" className="bg-blue-500 text-white px-4 py-2 rounded">Search Movies</Link>
        <Link to="/persons" className="bg-green-500 text-white px-4 py-2 rounded">Search Persons</Link>
      </div>
    </div>
  );
};

export default Home;
