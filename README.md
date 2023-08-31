# Documentazione del Portfolio

Benvenuti alla documentazione del mio Portfolio, un progetto che utilizza Django come backend e Vue.js con Vuetify come frontend. In questa guida, verranno fornite informazioni dettagliate sulle diverse parti del progetto, inclusi gli elementi chiave come tabelle del database, funzionalità e tecnologie utilizzate.

## Tecnologie Principali Utilizzate
- Backend: Django
- Frontend: Vue.js con Vuetify
- Version Control: Git

## Struttura delle Tabelle del Database
1. **Utenti**: Questa tabella memorizza le informazioni sugli utenti registrati nel sistema.
2. **Contatti**: Qui vengono salvati i dettagli dei contatti che gli utenti condividono.
3. **Lavori (Jobs)**: La tabella dei lavori contiene informazioni sulle opportunità di lavoro.
4. **Post**: In questa tabella vengono archiviati i post del blog o le notizie rilevanti.
5. **Categorie**: Le categorie vengono utilizzate per organizzare i post in base agli argomenti.

## Struttura del Progetto
portfolio/
|-- backend/ # Codice sorgente del backend Django
|-- portfolio/ # Codice sorgente del frontend Vue.js
|-- static/ # Risorse statiche
|-- templates/ # Template HTML (semplice integrazione Django)
|-- README.md # Documentazione principale del progetto
|-- requirements.txt # Dipendenze del progetto Django
|-- package.json # Dipendenze del progetto Vue.js
|-- .gitignore # File ignorati da Git


## Backend (Django) 
Il backend del progetto è sviluppato utilizzando il framework Django, noto per la sua scalabilità e facilità d'uso. Le principali funzionalità del backend includono:

- Gestione degli utenti attraverso l'autenticazione e l'autorizzazione.
- API per la gestione dei contatti, dei lavori, dei post e delle categorie.
- Utilizzo di modelli Django per definire la struttura delle tabelle del database.
- Utilizzo di view basate su classe per gestire le richieste API.
- Utilizzo di serializer per la conversione dei dati tra rappresentazione complessa e JSON.

## Frontend (Vue.js con Vuetify)
Il frontend del progetto è costruito utilizzando  Vue.js, un framework progressivo per la creazione di interfacce utente. Vuetify è utilizzato per aggiungere componenti esteticamente piacevoli e reattivi. Le principali caratteristiche del frontend includono:

- Layout responsive e moderno utilizzando componenti Vuetify predefiniti.
- Routing per navigare tra diverse sezioni del portfolio.
- Chiamate API per ottenere e visualizzare i dati dal backend.
- Integrazione di icone di Django e Vue.js per rappresentare le rispettive tecnologie utilizzate.
- Utilizzo di componenti Vue per modularizzare il codice e migliorare la manutenibilità.

## Istruzioni per l'Installazione
1. Clonare il repository Git: `git clone <URL_del_tuo_repository>`
2. Configurare e attivare l'ambiente virtuale (consigliato): 
   - Esegui: `python -m venv venv`
   - Attiva l'ambiente virtuale: Su Windows `venv\Scripts\activate`, su macOS/Linux `source venv/bin/activate`
3. Installare le dipendenze del backend: `pip install -r requirements.txt`
4. Installare le dipendenze del frontend: `npm install` (assicurati di avere Node.js installato)
5. Avviare il backend Django: `python manage.py runserver`
6. Avviare il frontend Vue.js: `npm run dev` utilizza vite
7. Ora puoi accedere al tuo portfolio all'indirizzo `http://localhost:8080`

