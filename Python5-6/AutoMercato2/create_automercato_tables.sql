
-- Creazione della tabella 'utenti'
CREATE TABLE utenti (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    stato VARCHAR(20) NOT NULL,
    ruolo VARCHAR(20) NOT NULL
);

-- INSERT INTO utenti (username, pass, stato, ruolo)
-- VALUES ('nome_utente', 'password_criptata', 'attivo', 'amministratore')