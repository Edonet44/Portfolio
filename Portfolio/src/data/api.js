import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Aggiorna l'URL con l'indirizzo del backend locale
   timeout: 30000, // Tempo massimo di attesa per la risposta dell'API
});

export default api;