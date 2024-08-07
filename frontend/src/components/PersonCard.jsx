import React from 'react';

const PersonCard = ({ person }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      {person.name && <h3 className="text-xl font-semibold">{person.name}</h3>}
      {person.birth_year && <p>Birth Year: {person.birth_year}</p>}
      {person.profession && <p>Profession: {person.profession}</p>}
      {person.known_for_titles && <p>Known for: {person.known_for_titles.join(', ')}</p>}
    </div>
  );
};

export default PersonCard;