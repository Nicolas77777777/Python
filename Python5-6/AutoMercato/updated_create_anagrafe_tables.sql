
-- Creazione della tabella 'utenti'
CREATE TABLE  utenti (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    privilegi INT NOT NULL
);

-- Creazione della tabella 'automobile'
CREATE TABLE  automobile (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modello VARCHAR(50) NOT NULL,
    colore VARCHAR(20) NOT NULL,
    posizione VARCHAR(100),
    filiale_id INT NOT NULL,
    condizione VARCHAR(50) NOT NULL
);

-- Creazione della tabella 'vendite'
CREATE TABLE IF NOT EXISTS vendite (
    id SERIAL PRIMARY KEY,
    id_automobile INT NOT NULL,
    data_vendita DATE NOT NULL,
    FOREIGN KEY (id_automobile) REFERENCES automobile (id)
);

-- Correzione di una query incompleta
-- Query per estrarre il massimo delle vendite di automobili e moto per filiale e data
SELECT 
    filiale, 
    data_vendita, 
    MAX(NumAutomobiliVendute) AS NumAutomobiliVendute,
    MAX(NumMotoVendute) AS NumMotoVendute
FROM (
    SELECT 
        filiale,
        data_vendita,
        COUNT(*) AS NumAutomobiliVendute, 
        0 AS NumMotoVendute
    FROM vendite
    WHERE data_vendita BETWEEN :dataInizio AND :dataFine AND tipo = 'automobile'
    GROUP BY filiale, data_vendita

    UNION

    SELECT 
        filiale,
        data_vendita,
        0 AS NumAutomobiliVendute, 
        COUNT(*) AS NumMotoVendute
    FROM vendite
    WHERE data_vendita BETWEEN :dataInizio AND :dataFine AND tipo = 'motocicletta'
    GROUP BY filiale, data_vendita
) AS tmp
GROUP BY filiale, data_vendita;
