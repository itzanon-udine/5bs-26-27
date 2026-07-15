# 🎬 Laboratorio Web App Python (Flask + SQLite)

Questo repository contiene gli esercizi di sviluppo web realizzati durante l'anno scolastico utilizzando Python, Flask e SQLite.

---

## 💾 1. Preparazione della Postazione Windows (Locale & Portable)

Per poter programmare e testare le applicazioni in locale senza installare nulla sul sistema operativo (utile in caso di blocchi di sicurezza dei PC scolastici), configuriamo un ambiente Python Portable su disco locale o su chiavetta USB.

### Passo 1: Scaricare e configurare Python Portable

1. **Scarica l'ambiente:** Scarica l'archivio di **WinPython Dot** (versione leggera "Dot").
2. **Crea la cartella principale:** Sul tuo PC (es. sul Desktop) o nella root della tua chiavetta USB, crea una cartella chiamata `Laboratorio Web`.
3. **Estrai e rinomina:** Estrai l'archivio WinPython scaricato dentro la cartella `Laboratorio Web` e rinomina la cartella estratta esattamente in `python_portable`.
4. **Installa le librerie necessarie:**
* Apri la cartella `python_portable` ed esegui il file `WinPython Command Prompt.exe`.
* Nel terminale, digita il seguente comando per installare Flask e Gunicorn:
```bash
pip install flask gunicorn

```


* Chiudi la finestra del terminale. Il tuo motore portatile è pronto e occupa **meno di 100MB**.



### Passo 2: Struttura dei file e percorsi relativi

La cartella `python_portable` e la cartella degli `esercizi` (che sincronizzerai su GitHub) devono essere affiancate dentro `Laboratorio Web`.

Organizza la struttura esattamente così:

```text
📁 Laboratorio Web/ (Cartella sul PC locale o sulla tua Chiavetta USB)
├── 📁 python_portable/        # Il motore Python configurato al Passo 1 (NON va su GitHub)
│   ├── 📄 VS Code.exe         # Launcher rapido di VS Code (se presente nel pacchetto)
│   ├── 📄 WinPython Command Prompt.exe
│   ├── 📁 notebooks/
│   ├── 📁 python/             # Contiene l'eseguibile python.exe
│   ├── 📁 scripts/
│   ├── 📁 settings/
│   └── 📁 wheelhouse/
└── 📁 esercizi/               # La cartella sincronizzata con questo Repo GitHub
    └── 📁 01_elenco_film/
        ├── 📁 templates/      # Contiene il file HTML per l'interfaccia
        ├── 📄 app.py          # Logica dell'applicazione Flask
        ├── 📄 avvia.bat       # Script di avvio rapido con percorso relativo
        ├── 📄 cinema.db       # Database SQLite locale
        ├── 📄 requirements.txt# Dipendenze per il cloud (Render / Codespaces)
        └── 📄 schema.sql      # Struttura del database SQLite

```

### Passo 3: Configurare il file di avvio (`avvia.bat`)

Dentro la cartella del tuo esercizio (es. `esercizi/01_elenco_film/`), crea o modifica il file `avvia.bat` inserendo questo codice. Grazie ai percorsi relativi, risalirà le cartelle fino a raggiungere il motore Python:

```batch
@echo off
echo Avvio del server Flask in corso...
"..\..\python_portable\python\python.exe" app.py
pause

```

*(Nota: Se nel tuo pacchetto l'eseguibile si trova in un'altra sottocartella, modifica il percorso di conseguenza)*

Fai doppio clic su `avvia.bat` e apri il browser sulla pagina indicata ad es. [http://127.0.0.1:5001](https://www.google.com/search?q=http://127.0.0.1:5001) per testare l'app in locale.

---

## 💻 2. Come Scrivere e Modificare il Codice in Locale

Per scrivere il codice all'interno della cartella `esercizi` sul tuo computer (o sulla chiavetta) hai a disposizione diverse opzioni, tutte pronte all'uso e senza bisogno di toccare le variabili di sistema del PC:

* **Opzione A (VS Code Integrato):** Se disponi di una installazione locale di VS Code, la cartella `python_portable` contiene un apposito launcher **`VS Code.exe`**, puoi fare doppio clic direttamente su di esso per lanciare VS Code. Si avvierà istantaneamente e saprà trovare Python nella cartella python_portable senza dover configurare variabili di ambiente.
* **Opzione B (Qualsiasi Editor locale):** Puoi usare qualsiasi editor di testo leggero già installato sul computer (es. Notepad++, Sublime Text o persino il Blocco Note di Windows) per modificare i file `.py`, `.html` e `.sql`.
* **Opzione C (VS Code Web con accesso locale):** Se sul PC non è installato alcun editor, puoi aprire il browser su [vscode.dev](https://vscode.dev), cliccare su **Open Folder** (Apri cartella) e selezionare la cartella locale `esercizi` per modificarla direttamente dal browser (sfruttando le API di accesso ai file locali del browser).

---

## ☁️ 3. Sviluppo e Setup Interamente Online (Cloud)

Se non hai a disposizione il PC della scuola o la tua chiavetta USB con il Python Portable, puoi completare gli esercizi, testarli ed eseguirli interamente nel cloud dal browser.

### Opzione A: Modifiche rapide al codice (VS Code Web su GitHub)

1. Apri questo repository su GitHub nel browser (per creare la tua copia personale, la prima volta fai un Fork).
2. Premi il tasto **punto fermo (`.`)** sulla tastiera per lanciare **VS Code Web**.
3. Modifica i file di codice direttamente dal browser o trascina i file modificati dentro la cartella `esercizi` a sinistra.
4. Salva le modifiche: vai sulla scheda **Controllo Sorgente** (Source Control) a sinistra, inserisci un messaggio di commit (es. *"Aggiunto esercizio film"*) e clicca su **Commit & Push**.

### Opzione B: Esecuzione e Test completo dell'app (GitHub Codespaces)

Se vuoi avviare l'applicazione e provarla nel browser senza installare nulla sul tuo computer personale:

1. Sul tuo repository GitHub, clicca sul pulsante verde **Code** in alto a destra.
2. Seleziona la scheda **Codespaces** e clicca su **Create codespace on main**.
3. Si aprirà un ambiente di sviluppo VS Code completo direttamente nel browser, dotato di un terminale Linux con Python già installato.
4. Nel terminale in basso, spostati nella cartella dell'esercizio:

```bash
cd esercizi/01_elenco_film

```

5. Installa i pacchetti necessari ed esegui l'app:

```bash
pip install -r requirements.txt
python app.py

```

6. VS Code mostrerà una notifica pop-up in basso a destra. Clicca su **Open in Browser** (Apri nel browser) per visualizzare e testare l'app online.

---

## 🌐 4. Condivisione e Messa in Produzione (Rendere l'app pubblica)

Per mostrare il tuo lavoro al docente o ai tuoi compagni, hai due strade. Scegli quella più adatta alle tue esigenze:

### Opzione A: Port Forwarding con VS Code (Veloce, Temporaneo e senza Registrazioni)

Se stai eseguendo l'app sul tuo computer (tramite l'app di VS Code) o all'interno di **GitHub Codespaces**, puoi generare un link pubblico temporaneo direttamente dall'editor di testo, senza dover configurare server esterni.

1. **Avvia l'applicazione:** Assicurati che il tuo server Flask sia attivo nel terminale di VS Code.
2. **Apri il pannello Porte:** Nella parte inferiore di VS Code, accanto alla scheda *Terminale*, seleziona la scheda **Ports** (Porte).
*(Se non la vedi, fai clic destro sulla barra dei pannelli in basso e spunta la voce "Porte")*.
3. **Inoltra la porta:** Se non è già presente, clicca su **Forward a Port** (Inoltra una porta) e digita il numero della porta su cui gira Flask (es. `5001` o `5000`).
4. **Rendi pubblico il link:** Di default, la porta è privata. Clicca con il tasto destro sulla riga della porta inserita, seleziona **Port Visibility** (Visibilità porta) e impostala su **Public** (Pubblica).
5. **Copia e condividi:** Copia l'indirizzo che compare sotto la colonna **Forwarded Address** (Indirizzo inoltrato) e invialo a chi desideri per fargli testare la tua app.

> ⚠️ **Nota importante:** Questo metodo funziona solo se la tua istanza di VS Code (o Codespace) è aperta e l'applicazione Flask è attivamente in esecuzione. Se chiudi il terminale o spegni il PC, il link smetterà di funzionare.

### Opzione B: Deploy su Render (Permanente e sempre Attivo)

Se vuoi pubblicare l'applicazione web online gratuitamente e fare in modo che rimanga raggiungibile da chiunque in qualsiasi momento tramite un link fisso:

1. Crea un nuovo **Web Service** su Render e connetti il tuo repository GitHub.
2. Configura le seguenti impostazioni fondamentali per indicare a Render in quale cartella lavorare:
* **Root Directory:** `esercizi/01_elenco_film` *(indica a Render di entrare precisamente in questa cartella)*
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `gunicorn app:app`


3. Clicca su **Deploy**. Da questo momento, ogni volta che salverai nuove modifiche su GitHub (usando il metodo del punto o Codespaces), Render aggiornerà il tuo sito web in automatico.
