CREATE TYPE condizione  AS ENUM ('Nuova', 'Usata');


CREATE TABLE Automobile (
    num_telaio VARCHAR(50) PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modello VARCHAR(50) NOT NULL,
    colore VARCHAR(30) NOT NULL,
    filiale VARCHAR(255) NOT NULL,
    condizione condizione NOT NULL DEFAULT 'Nuova',
    FOREIGN KEY (filiale) REFERENCES Filiale(nome)
);


CREATE TABLE filiale (
    nome VARCHAR(255) PRIMARY KEY
);

INSERT INTO filiale (nome) VALUES
('Filiale1'),
('Filiale2'),
('Filiale3'),
('Magazzino Centrale');


INSERT INTO Automobile (num_telaio, marca, modello, colore, filiale, condizione) VALUES
('1HGCM82', 'Toyota', 'Corolla', 'Rosso', 'Filiale1', 'Nuova'),
('2HGCM63', 'Ford', 'Fiesta', 'Blu', 'Filiale2', 'Usata'),
('3HGCM78', 'Volkswagen', 'Golf', 'Bianco', 'Filiale3', 'Nuova'),
('4HGCM45', 'Renault', 'Clio', 'Nero', 'Magazzino Centrale', 'Nuova'),
('5HGCM26', 'Fiat', 'Panda', 'Grigio', 'Filiale1', 'Usata');
('11HGCM26', 'Fiat', 'Panda', 'Grigio', 'Filiale1', 'Usata');



CREATE TABLE Vendita_Auto (
    num_telaio VARCHAR(50) PRIMARY KEY,
    data_vendita DATE NOT NULL,
    filiale VARCHAR(255) NOT NULL,
    FOREIGN KEY (num_telaio) REFERENCES Automobile(num_telaio),
    FOREIGN KEY (filiale) REFERENCES Filiale(nome)
);


-- SELECT filiale, data_vendita, COUNT(*) AS numero_vendite
-- FROM Vendita_Auto
-- GROUP BY filiale, data_vendita
-- ORDER BY numero_vendite DESC;


SELECT filiale, COUNT(*) AS numero_vendite 
FROM Vendita_Auto 
where data_vendita = '2024-12-04' 
GROUP BY filiale 
ORDER BY numero_vendite DESC;