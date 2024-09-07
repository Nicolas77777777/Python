
-- Definizione dei tipi enumerativi
CREATE TYPE Strutturato AS ENUM ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
CREATE TYPE LavoroProgetto AS ENUM ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');
CREATE TYPE LavoroNonProgettuale AS ENUM ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro');
CREATE TYPE CausaAssenza AS ENUM ('Chiusura Universitaria', 'Maternita', 'Malattia');

-- Definizione dei domini
CREATE DOMAIN PosInteger AS INTEGER CHECK (VALUE >= 0);
CREATE DOMAIN StringaM AS VARCHAR(100);
CREATE DOMAIN NumeroOre AS INTEGER CHECK (VALUE BETWEEN 0 AND 8);
CREATE DOMAIN Denaro AS REAL CHECK (VALUE >= 0);

CREATE TABLE Persona (
    id PosInteger PRIMARY KEY,
    nome StringaM NOT NULL,
    cognome StringaM NOT NULL,
    posizione Strutturato NOT NULL,
    stipendio Denaro NOT NULL
);

CREATE TABLE Progetto (
    id PosInteger PRIMARY KEY,
    nome StringaM UNIQUE, -- Vincolo [VincoloDB.1]
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    budget Denaro NOT NULL,
    CHECK (inizio < fine) -- Vincolo [VincoloDB.2]
);

CREATE TABLE WP (
    progetto PosInteger NOT NULL,
    id PosInteger NOT NULL,
    nome StringaM NOT NULL,
    inizio DATE NOT NULL,
    fine DATE NOT NULL,
    PRIMARY KEY (progetto, nome), -- Vincolo [VincoloDB.4]
    FOREIGN KEY (progetto) REFERENCES Progetto(id), -- Vincolo [VincoloDB.5]
    CHECK (inizio < fine) -- Vincolo [VincoloDB.3]
);

CREATE TABLE AttivitaProgetto (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    progetto PosInteger NOT NULL,
    wp PosInteger NOT NULL,
    giorno DATE NOT NULL,
    tipo LavoroProgetto NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id), -- Vincolo [VincoloDB.6]
    FOREIGN KEY (progetto, wp) REFERENCES WP(progetto, id) -- Vincolo [VincoloDB.7]
);

CREATE TABLE AttivitaNonProgettuale (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo LavoroNonProgettuale NOT NULL,
    giorno DATE NOT NULL,
    oreDurata NumeroOre NOT NULL,
    FOREIGN KEY (persona) REFERENCES Persona(id) -- Vincolo [VincoloDB.8]
);

CREATE TABLE Assenza (
    id PosInteger PRIMARY KEY,
    persona PosInteger NOT NULL,
    tipo CausaAssenza NOT NULL,
    giorno DATE NOT NULL,
    UNIQUE (persona, giorno), -- Vincolo [VincoloDB.9]
    FOREIGN KEY (persona) REFERENCES Persona(id) -- Vincolo [VincoloDB.10]
);
