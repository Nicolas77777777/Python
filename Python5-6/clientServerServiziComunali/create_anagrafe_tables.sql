
-- Creazione della tabella 'utenti'
CREATE TABLE utenti (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    stato VARCHAR(20) NOT NULL,
    ruolo VARCHAR(20) NOT NULL
);

-- Creazione della tabella 'cittadini'
CREATE TABLE cittadini (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    codice_fiscale CHAR(16) UNIQUE NOT NULL,
    data_nascita DATE NOT NULL,
    comune_residenza VARCHAR(100) NOT NULL
);

-- Creazione della tabella 'documenti'
CREATE TABLE documenti (
    id SERIAL PRIMARY KEY,
    id_cittadino INT NOT NULL,
    tipo_documento VARCHAR(50) NOT NULL,
    data_emissione DATE NOT NULL,
    data_scadenza DATE,
    FOREIGN KEY (id_cittadino) REFERENCES cittadini (id)
);

-- Creazione della tabella 'servizi'
CREATE TABLE servizi (
    id SERIAL PRIMARY KEY,
    nome_servizio VARCHAR(100) NOT NULL,
    descrizione TEXT,
    costo DECIMAL(10, 2) NOT NULL
);

-- Creazione della tabella 'prenotazioni'
CREATE TABLE prenotazioni (
    id SERIAL PRIMARY KEY,
    id_cittadino INT NOT NULL,
    id_servizio INT NOT NULL,
    data_prenotazione DATE NOT NULL,
    stato VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_cittadino) REFERENCES cittadini (id),
    FOREIGN KEY (id_servizio) REFERENCES servizi (id)
);
