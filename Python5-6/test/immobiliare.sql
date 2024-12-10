 --mario pass  è l'utente admin

-- Creazione del tipo ENUM per stato delle case in vendita
CREATE TYPE stato_vendita AS ENUM ('LIBERO', 'OCCUPATO');

-- Creazione del tipo ENUM per tipo di affitto
CREATE TYPE tipo_affitto AS ENUM ('PARZIALE', 'TOTALE');

-- utente admin mario pass 1--

CREATE TABLE utenti (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    stato VARCHAR(20) NOT NULL,
); 

-- Tabella delle filiali
CREATE TABLE filiali (
    partita_iva VARCHAR(16) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    indirizzo_sede VARCHAR(255) NOT NULL,
    civico INTEGER NOT NULL,
    telefono VARCHAR(15) NOT NULL
);

-- Tabella delle case in vendita
CREATE TABLE case_in_vendita (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    numero_civico INTEGER NOT NULL,
    piano INTEGER,
    metri INTEGER NOT NULL,
    vani INTEGER NOT NULL,
    prezzo INTEGER NOT NULL,
    stato stato_vendita  NOT NULL,
    filiale_proponente VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE
);

-- Tabella delle case in affitto
CREATE TABLE case_in_affitto (
    catastale VARCHAR(20) PRIMARY KEY,
    indirizzo VARCHAR(255) NOT NULL,
    civico INTEGER NOT NULL,
    tipo_affitto tipo_affitto NOT NULL,
    bagno_personale BOOLEAN NOT NULL,
    prezzo_mensile INTEGER NOT NULL,
    filiale_proponente VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE
);

-- Tabella delle vendite di case
CREATE TABLE vendite_casa (
    catastale VARCHAR(20) REFERENCES case_in_vendita(catastale) ON DELETE CASCADE,
    data_vendita DATE NOT NULL,
    filiale_proponente VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE,
    filiale_venditrice VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE,
    prezzo_vendita INTEGER NOT NULL,
    PRIMARY KEY (catastale, data_vendita)
);

-- Tabella degli affitti di case
CREATE TABLE affitti_casa (
    catastale VARCHAR(20) REFERENCES case_in_affitto(catastale) ON DELETE CASCADE,
    data_affitto DATE NOT NULL,
    filiale_proponente VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE,
    filiale_venditrice VARCHAR(16) REFERENCES filiali(partita_iva) ON DELETE CASCADE,
    prezzo_affitto INTEGER NOT NULL,
    durata_contratto INTERVAL NOT NULL,
    PRIMARY KEY (catastale, data_affitto)
);





