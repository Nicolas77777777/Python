-- Creazione del tipo ENUM condizione
-- Questo tipo specifica lo stato del veicolo: "nuovo" o "usato"
CREATE TYPE condizione AS 
ENUM ('nuovo', 'usato');


-- creazine della tabella utenti 
CREATE TABLE utenti (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    stato VARCHAR(20) NOT NULL,
);

-- Creazione della tabella Filiali
-- Rappresenta le filiali dell'automercato
CREATE TABLE filiali (
    id SERIAL PRIMARY KEY,                     -- ID univoco della filiale
    nome VARCHAR(100) NOT NULL,               -- Nome della filiale
    indirizzo VARCHAR(255) NOT NULL,          -- Indirizzo della filiale
    partita_iva CHAR(11) NOT NULL UNIQUE      -- Partita IVA della filiale, univoca
);

-- Creazione della tabella Magazzini
-- Ogni magazzino è associato a una filiale e conserva veicoli e accessori
CREATE TABLE magazzini (
    id SERIAL PRIMARY KEY,                    -- ID univoco del magazzino
    id_filiale INT UNIQUE NOT NULL,           -- ID della filiale associata
    nome_magazzino VARCHAR(100) NOT NULL,     -- Nome del magazzino
    FOREIGN KEY (id_filiale) REFERENCES filiali (id) -- Collegamento alla tabella filiali
);

-- Creazione della tabella Automobili
-- Contiene i dettagli delle automobili disponibili nei magazzini
CREATE TABLE automobili (
    id SERIAL PRIMARY KEY,                    -- ID univoco dell'automobile
    marca VARCHAR(50) NOT NULL,               -- Marca dell'automobile
    modello VARCHAR(50) NOT NULL,             -- Modello dell'automobile
    colore VARCHAR(20) NOT NULL,              -- Colore dell'automobile
    targa VARCHAR(20) NOT NULL UNIQUE,        -- Targa univoca dell'automobile
    magazzino_id INT NOT NULL,                -- ID del magazzino che conserva l'automobile
    condizione condizione NOT NULL DEFAULT 'nuovo', -- Condizione: nuovo o usato
    disponibilita BOOLEAN DEFAULT TRUE,       -- Se l'automobile è disponibile o venduta
    FOREIGN KEY (magazzino_id) REFERENCES magazzini (id) -- Collegamento alla tabella magazzini
);

-- Creazione della tabella Motociclette
-- Contiene i dettagli delle motociclette disponibili nei magazzini
CREATE TABLE motociclette (
    id SERIAL PRIMARY KEY,                    -- ID univoco della motocicletta
    marca VARCHAR(50) NOT NULL,               -- Marca della motocicletta
    modello VARCHAR(50) NOT NULL,             -- Modello della motocicletta
    colore VARCHAR(20) NOT NULL,              -- Colore della motocicletta
    targa VARCHAR(20) NOT NULL UNIQUE,        -- Targa univoca della motocicletta
    magazzino_id INT NOT NULL,                -- ID del magazzino che conserva la motocicletta
    condizione condizione NOT NULL DEFAULT 'nuovo', -- Condizione: nuovo o usato
    disponibilita BOOLEAN DEFAULT TRUE,       -- Se la motocicletta è disponibile o venduta
    FOREIGN KEY (magazzino_id) REFERENCES magazzini (id) -- Collegamento alla tabella magazzini
);

-- Creazione della tabella Accessori
-- Contiene i dettagli degli accessori disponibili nei magazzini
CREATE TABLE accessori (
    id SERIAL PRIMARY KEY,                    -- ID univoco dell'accessorio
    nome VARCHAR(100) NOT NULL,               -- Nome dell'accessorio
    descrizione TEXT DEFAULT 'Descrizione accessorio momentanea', -- Descrizione con valore predefinito
    magazzino_id INT NOT NULL,                -- ID del magazzino che conserva l'accessorio
    disponibilita BOOLEAN DEFAULT TRUE,       -- Se l'accessorio è disponibile o venduto
    FOREIGN KEY (magazzino_id) REFERENCES magazzini (id) -- Collegamento alla tabella magazzini
);


-- Creazione della tabella Vendite
-- Registra le vendite di automobili, motociclette e accessori
CREATE TABLE vendite (
    id SERIAL PRIMARY KEY,                    -- ID univoco della vendita
    tipo_articolo VARCHAR(20) NOT NULL CHECK (tipo_articolo IN ('automobile', 'motocicletta', 'accessorio')), -- Tipo di articolo venduto
    articolo_id INT NOT NULL,                 -- ID dell'articolo venduto
    data_vendita DATE NOT NULL,               -- Data della vendita
    id_filiale INT NOT NULL,                  -- ID della filiale che ha effettuato la vendita
    FOREIGN KEY (id_filiale) REFERENCES filiali (id) -- Collegamento alla tabella filiali
);
