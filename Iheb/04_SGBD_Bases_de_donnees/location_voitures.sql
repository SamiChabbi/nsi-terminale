-- Données INVENTÉES pour tester les requêtes de l'exercice 7 (le sujet n'en fournit pas).
-- Clients, adresses électroniques et immatriculations fictifs.
DROP TABLE IF EXISTS Location;
DROP TABLE IF EXISTS Véhicule;
DROP TABLE IF EXISTS Modèle;
DROP TABLE IF EXISTS Client;

CREATE TABLE Client (idC INT, nom VARCHAR, prénom VARCHAR, email VARCHAR,
    PRIMARY KEY (idC));
CREATE TABLE Modèle (idM INT, marque VARCHAR, année INT, moteur VARCHAR,
    PRIMARY KEY (idM));
CREATE TABLE Véhicule (idV INT, modele INT, immatr VARCHAR, nbKm INT,
    PRIMARY KEY (idV),
    FOREIGN KEY (modele) REFERENCES Modèle(idM));
CREATE TABLE Location (idL INT, idCli INT, idVehi INT, dateDeb TIMESTAMP, dateFin TIMESTAMP,
    PRIMARY KEY (idL),
    FOREIGN KEY (idCli) REFERENCES Client(idC),
    FOREIGN KEY (idVehi) REFERENCES Véhicule(idV));

INSERT INTO Client VALUES (1345, 'Dupont', 'Marie', 'marie.dupont@exemple.fr');
INSERT INTO Client VALUES (1346, 'Durand', 'Paul', 'paul.durand@exemple.fr');
INSERT INTO Client VALUES (1347, 'Nguyen', 'Linh', 'linh.nguyen@exemple.fr');
INSERT INTO Client VALUES (1348, 'Moreau', 'Hugo', 'hugo.moreau@exemple.fr');

INSERT INTO Modèle VALUES (1, 'Renault', 2022, 'électrique');
INSERT INTO Modèle VALUES (2, 'Peugeot', 2020, 'essence');
INSERT INTO Modèle VALUES (3, 'Tesla', 2023, 'électrique');
INSERT INTO Modèle VALUES (4, 'Citroën', 2019, 'diesel');

INSERT INTO Véhicule VALUES (245, 2, 'AA-123-AA', 62000);
INSERT INTO Véhicule VALUES (246, 1, 'BB-456-BB', 18000);
INSERT INTO Véhicule VALUES (247, 3, 'CC-789-CC', 35000);
INSERT INTO Véhicule VALUES (248, 4, 'DD-012-DD', 125000);
INSERT INTO Véhicule VALUES (249, 1, 'EE-345-EE', 51000);
INSERT INTO Véhicule VALUES (250, 2, 'FF-678-FF', 9000);

INSERT INTO Location VALUES (9101, 1346, 246, '2025-09-03 09:00:00', '2025-09-05 18:00:00');
INSERT INTO Location VALUES (9102, 1347, 247, '2025-09-20 10:00:00', '2025-09-21 10:00:00');
INSERT INTO Location VALUES (9103, 1346, 249, '2025-09-28 08:00:00', '2025-10-02 12:00:00');
INSERT INTO Location VALUES (9104, 1348, 245, '2025-09-10 14:00:00', '2025-09-12 14:00:00');
INSERT INTO Location VALUES (9105, 1348, 246, '2025-10-15 09:00:00', '2025-10-16 09:00:00');
INSERT INTO Location VALUES (9201, 1347, 248, '2025-11-02 07:30:00', null);
INSERT INTO Location VALUES (9202, 1346, 247, '2025-11-04 11:00:00', null);
