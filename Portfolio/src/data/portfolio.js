import api from './api';

//creo un oggetto per il recupero dei dati dal backend
const PortfolioService = {
    
  //funzione per il recupero dati
  async getUtenteData() {
    try {
      //recupero dal database Mongodb in locale
      const response = await api.get('/api/v1/utenti/');
      if (response.status === 200) {
        return response.data;
      } else if (response.status === 403) {
        // ... Gestione altri codici di stato
      } else {
        console.error('Errore durante la chiamata API:', response.data);
        throw new Error('Errore durante la chiamata API');
      }
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        console.error('Timeout durante la chiamata API:', error);
        throw new Error('Timeout durante la chiamata API');
      } else {
        console.error('Errore durante la chiamata API:', error);
        throw error;
      }
    }
  },
  
  async getJobData() {
    try {
      //recupero dal database Mongodb in locale
      const response = await api.get('/api/v1/jobs/');
      if (response.status === 200) {
        return response.data;
      } else if (response.status === 403) {
        // ... Gestione altri codici di stato
      } else {
        console.error('Errore durante la chiamata API:', response.data);
        throw new Error('Errore durante la chiamata API');
      }
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        console.error('Timeout durante la chiamata API:', error);
        throw new Error('Timeout durante la chiamata API');
      } else {
        console.error('Errore durante la chiamata API:', error);
        throw error;
      }
    }
  },


  async getContactData() {
    try {
      //recupero dal database Mongodb in locale
      const response = await api.get('/api/v1/contact/');
      if (response.status === 200) {
        return response.data;
      } else if (response.status === 403) {
        // ... Gestione altri codici di stato
      } else {
        console.error('Errore durante la chiamata API:', response.data);
        throw new Error('Errore durante la chiamata API');
      }
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        console.error('Timeout durante la chiamata API:', error);
        throw new Error('Timeout durante la chiamata API');
      } else {
        console.error('Errore durante la chiamata API:', error);
        throw error;
      }
    }
  },

  async getBlogData() {
    try {
      //recupero dal database Mongodb in locale
      const response = await api.get('/api/v1/blog/');
      if (response.status === 200) {
        return response.data;
      } else if (response.status === 403) {
        // ... Gestione altri codici di stato
      } else {
        console.error('Errore durante la chiamata API:', response.data);
        throw new Error('Errore durante la chiamata API');
      }
    } catch (error) {
      if (error.code === 'ECONNABORTED') {
        console.error('Timeout durante la chiamata API:', error);
        throw new Error('Timeout durante la chiamata API');
      } else {
        console.error('Errore durante la chiamata API:', error);
        throw error;
      }
    }
  }
};

export default PortfolioService;

