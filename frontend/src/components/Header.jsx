import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="bg-blue-600 text-white p-4">
      <nav className="container mx-auto flex justify-between">
        <Link to="/" className="text-2xl font-bold">Movie List App</Link>
        <div>
          <Link to="/movies" className="mr-4">Movies</Link>
          <Link to="/persons">Persons</Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
