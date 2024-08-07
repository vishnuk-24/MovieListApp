import React, { useState } from 'react';
import { searchPersons } from '../config/api';
import PersonCard from '../components/PersonCard';

const PersonSearch = () => {
  const [searchParams, setSearchParams] = useState({ name: '' });
  const [persons, setPersons] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await searchPersons(searchParams);
      setPersons(response.data);
    } catch (error) {
      console.error('Error searching persons:', error);
    }
  };

  return (
    <div className="container mx-auto mt-10 text-center">
      <h2 className="text-2xl font-bold mb-4">Search Persons</h2>
      <form onSubmit={handleSearch} className="mb-6">
        <input
          type="text"
          placeholder="Person Name"
          value={searchParams.name}
          onChange={(e) => setSearchParams({ ...searchParams, name: e.target.value })}
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-green-500 text-white px-4 py-2 rounded">Search</button>
      </form>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {persons.map((person) => (
          <PersonCard key={person.id} person={person} />
        ))}
      </div>
    </div>
  );
};

export default PersonSearch;