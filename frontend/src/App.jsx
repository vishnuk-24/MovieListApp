import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import MovieSearch from './pages/MovieSearch';
import PersonSearch from './pages/PersonSearch';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/movies" element={<MovieSearch />} />
          <Route path="/persons" element={<PersonSearch />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;