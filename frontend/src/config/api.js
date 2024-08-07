import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
});

export const searchMovies = (params) => api.post('/search_movie', params);
export const searchPersons = (params) => api.post('/search_person', params);

export default api;
