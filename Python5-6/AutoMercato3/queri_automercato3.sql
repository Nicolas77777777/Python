-- Creazione tabella vendite
SELECT 
    f.nome AS filiale,                              -- Nome della filiale
    v.data_vendita,                                 -- Data della vendita
    COUNT(CASE WHEN v.tipo_articolo = 'automobile' THEN 1 END) AS vendite_automobili, -- Vendite di automobili
    COUNT(CASE WHEN v.tipo_articolo = 'motocicletta' THEN 1 END) AS vendite_motociclette -- Vendite di motociclette
FROM vendite v
JOIN filiali f ON v.id_filiale = f.id              -- Collegamento della vendita alla filiale
WHERE v.data_vendita BETWEEN '2024-01-01' AND '2024-01-31' -- Intervallo di date (può essere parametrizzato)
GROUP BY f.nome, v.data_vendita                   -- Raggruppamento per filiale e data
ORDER BY v.data_vendita, f.nome;   


-- ricerca per colore 

SELECT f.*, a.*
FROM filiali f
JOIN automobili a ON f.id = a.magazzino_id
WHERE LOWER(a.colore) = 'bianco';