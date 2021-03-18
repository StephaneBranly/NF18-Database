-- Sélection des informations des clients
SELECT * FROM CLIENT ORDER BY ID ASC;

-- Sélection des informations de clients à partir d'un nom ou d'un prénom (nomClient et prenomClient ici)
SELECT * FROM CLIENT WHERE strpos(nom,nomClient)>0 OR strpos(prenom,prenomClient)>0 ORDER BY ID ASC;

-- Sélection des informations d'un client à partir de son ID (idclient ici)
SELECT * FROM CLIENT WHERE id=idclient;

-- Sélection des animaux actuels d'un client à partir d'un ID (idclient ici)
SELECT * FROM PROPRIETAIRE_ACTUEL WHERE ID_Client=idclient;

-- Sélection des anciens animaux d'un client à partir d'un ID (idclient ici)
SELECT * FROM PROPRIETAIRE_PASSE WHERE ID_Client=idclient;

-- Sélection des différentes espèces 
SELECT * FROM ESPECE ORDER BY ESPECE ASC;

-- Sélection des informations sur les médicaments 
SELECT * FROM MEDICAMENT ORDER BY NomMolecule ASC;

-- Sélection d'une espèce particulière à partir de son nom ('NomEspece' ici)
SELECT * FROM ESPECE WHERE ESPECE='NomEspece';

-- Sélection des informations sur un médicament spécifique à partir de son nom('NomMolecule' ici)
SELECT * FROM MEDICAMENT WHERE nomMolecule='NomMolecule';

-- Sélection des informations sur les patients
SELECT * FROM PATIENT ORDER BY ID ASC;

-- Sélection des informations d'un patient à partir d'un numéro de puce (puceId) ou de passeport (numPasseport)
SELECT * FROM PATIENT WHERE strpos(numeroPuceID,puceId)>0 OR strpos(numeroPasseport,numPasseport)>0 ORDER BY ID ASC;

-- Sélection des informations d'un patient à partir de son ID (idPatient ici)
SELECT * FROM PATIENT WHERE id=idPatient;

-- Sélection des informations du propriétaire actuel d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM PROPRIETAIRE_ACTUEL WHERE ID_Patient=idPatient;

-- Sélection des informations des anciens propriétaires d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM PROPRIETAIRE_PASSE WHERE ID_Patient=idPatient;

-- Sélection des informations du soignant actuel d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM SOIGNANT_ACTUEL WHERE ID_Patient=idPatient;

-- Sélection des informations du soignant actuel d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM SOIGNANT_PASSE WHERE ID_Patient=idPatient;

-- Sélection des informations des anciens soignants d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM MESURE WHERE IDPatient=idPatient ORDER BY DateEtHeure DESC;

-- Sélection des informations sur les procédures d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM PROCEDURE WHERE IDPatient=idPatient ORDER BY DateEtHeure DESC

-- Sélection des informations sur les observations générales d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM OBSERVATION_GENERALE WHERE IDPatient=idPatient ORDER BY DateEtHeure DESC;


-- Sélection des informations sur les résultats d'analyse d'un patient à partir d'un ID (idPatient ici)
SELECT * FROM RESULTAT_ANALYSE WHERE IDPatient=idPatient ORDER BY DateEtHeure DESC

-- Sélection des informations du personnel
SELECT * FROM PERSONNEL ORDER BY ID ASC;

-- Sélection des informations sur le personnel à partir d'un nom ou d'un prénom (nomPersonnel et prenomPersonnel ici)
SELECT * FROM PERSONNEL WHERE strpos(nom,nomPersonnel)>0 OR strpos(prenom,prenomPersonnel)>0 ORDER BY ID ASC;

-- Sélection des informations d'un membre du personnel à partir de son ID (idPersonnel ici)
SELECT * FROM PERSONNEL WHERE id=%i;

-- Sélection des informations sur les patients actuels d'un membre du personnel à partir d'un ID (idPersonnel ici)
SELECT * FROM SOIGNANT_ACTUEL WHERE ID_Personnel=idPersonnel;

-- Sélection des informations sur les anciens patients d'un membre du personnel à partir d'un ID (idPersonnel ici)
SELECT * FROM SOIGNANT_PASSE WHERE ID_Personnel=idPersonnel;


-- Vues créés pour réaliser des statistiques disponible dans le rapport statistique, on réalisera des SELECT sur ces vues pour récupérer les informations qui nous intéressent

CREATE VIEW STATS_MEDICAMENTS AS
SELECT MEDICAMENT.NomMolecule, SUM(REL_TRAITEMENT_MEDICAMENT.QUANTITE)  AS QUANTITE_UTILISEE
FROM
MEDICAMENT INNER JOIN REL_TRAITEMENT_MEDICAMENT
ON MEDICAMENT.NomMolecule = REL_TRAITEMENT_MEDICAMENT.NomMolecule
GROUP BY MEDICAMENT.NomMolecule;

CREATE VIEW NBR_TRAITEMENT AS
SELECT COUNT(*) AS NBR_TRAITEMENT
FROM TRAITEMENT;

CREATE VIEW NBR_PRODEDURE AS
SELECT COUNT(*) AS NBR_PROCEDURE
FROM PROCEDURE;

CREATE VIEW NBR_TRAITEMENT_PAR_ESPECE AS
SELECT PATIENT.Espece, COUNT(*) AS NBR_TRAITEMENT_ESPECE
FROM TRAITEMENT INNER JOIN PATIENT 
ON PATIENT.ID = TRAITEMENT.IDPATIENT
GROUP BY PATIENT.Espece;
