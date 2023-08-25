import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
import vuetify from 'vite-plugin-vuetify'

const path = require('path');

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vuetify() // Aggiungi il plugin Vuetify qui
  ],
  resolve: {
    alias: {
      //'@': fileURLToPath(new URL('./src', import.meta.url))
       '@': path.resolve(__dirname, 'src') // Usa path.resolve per creare il percorso assoluto
    }
  },
   vuetify: {
   theme: {
    themes: {
      light: {
        primary: '#1976D2', // Esempio di colore primario
        secondary: '#424242', // Esempio di colore secondario
        accent: '#82B1FF', // Esempio di colore di accento
      },
      dark: {
        primary: '#2196F3',
        secondary: '#616161',
        accent: '#FFC107',
      },
    },
  },
  }
})
