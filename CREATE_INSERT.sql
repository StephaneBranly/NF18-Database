CREATE TABLE CLIENT (
ID INTEGER PRIMARY KEY,
Nom VARCHAR NOT NULL,
Prenom VARCHAR NOT NULL,
DateDeNaissance DATE NOT NULL,
Adresse VARCHAR,
NumeroTel VARCHAR
);

CREATE TABLE PERSONNEL (
ID INTEGER PRIMARY KEY,
Nom VARCHAR NOT NULL,
Prenom VARCHAR NOT NULL,
DateDeNaissance DATE,
Adresse VARCHAR,
NumeroTel VARCHAR,
Poste VARCHAR CHECK (Poste IN ('Veto', 'Assistant'))
) ;

CREATE TABLE ESPECE (
Espece VARCHAR PRIMARY KEY
) ;

CREATE TABLE PATIENT (
ID INTEGER PRIMARY KEY,
Nom VARCHAR NOT NULL,
DateDeNaissance DATE NOT NULL,
Taille VARCHAR CHECK (Taille IN ('Petite', 'Moyenne')),
NumeroPuceID VARCHAR,
NumeroPasseport VARCHAR,
Espece VARCHAR,
FOREIGN KEY (Espece) REFERENCES ESPECE(espece)
) ;

CREATE TABLE MEDICAMENT (
NomMolecule VARCHAR PRIMARY KEY,
Description VARCHAR
) ;

CREATE TABLE MESURE (
ID INTEGER PRIMARY KEY,
IDPatient INTEGER NOT NULL,
DateEtHeure DATE,
Taille VARCHAR CHECK (Taille IN ('Petite', 'Moyenne')),
Poids REAL ,
CONSTRAINT CHK_TaillePoids CHECK (Taille IS NOT NULL OR Poids IS NOT NULL),
FOREIGN KEY (IDPatient) REFERENCES PATIENT(ID)
) ;

CREATE TABLE TRAITEMENT (
ID INTEGER PRIMARY KEY,
IDPatient INTEGER NOT NULL,
DateEtHeure DATE ,
DateDebut DATE ,
Duree INTEGER,
 FOREIGN KEY (IDPatient) REFERENCES PATIENT(ID)
) ;

CREATE TABLE RESULTAT_ANALYSE (
ID INTEGER PRIMARY KEY,
IDPatient INTEGER NOT NULL,
DateEtHeure DATE,
Resultat VARCHAR,
FOREIGN KEY (IDPatient) REFERENCES PATIENT(ID)
);

CREATE TABLE OBSERVATION_GENERALE (
ID INTEGER PRIMARY KEY,
IDPatient INTEGER NOT NULL,
IDPersonnel INTEGER NOT NULL,
DateEtHeure DATE,
Observation VARCHAR,
FOREIGN KEY (IDPatient) REFERENCES PATIENT(ID),
FOREIGN KEY (IDPersonnel) REFERENCES PERSONNEL(ID)
) ;

CREATE TABLE PROCEDURE (
ID INTEGER PRIMARY KEY,
IDPatient INTEGER  NOT NULL,
DateEtHeure DATE,
Description VARCHAR,
FOREIGN KEY (IDPatient) REFERENCES PATIENT(ID)
) ;

CREATE TABLE REL_PATIENT_CLIENT (
ID_Client INTEGER NOT NULL,
ID_Patient INTEGER NOT NULL,
DateDebut DATE NOT NULL,
DateFin DATE,
FOREIGN KEY (ID_Client) REFERENCES CLIENT(ID),
FOREIGN KEY (ID_Patient) REFERENCES PATIENT(ID)

);

CREATE TABLE REL_PATIENT_PERSONNEL (
ID_Personnel INTEGER NOT NULL,
ID_Patient INTEGER NOT NULL,
DateDebut DATE NOT NULL,
DateFin DATE,
FOREIGN KEY (ID_Personnel) REFERENCES PERSONNEL(ID),
FOREIGN KEY (ID_Patient) REFERENCES PATIENT(ID)

);

CREATE TABLE REL_PERSONNEL_ESPECE (
ID_Personnel INTEGER NOT NULL,
Espece VARCHAR NOT NULL,
Taille VARCHAR,
FOREIGN KEY (ID_Personnel) REFERENCES PERSONNEL(ID),
FOREIGN KEY (Espece) REFERENCES ESPECE(Espece)
);

CREATE TABLE REL_TRAITEMENT_MEDICAMENT (
NomMolecule VARCHAR NOT NULL,
ID_Traitement INTEGER NOT NULL,
Quantite INTEGER,
FOREIGN KEY (NomMolecule) REFERENCES MEDICAMENT(NomMolecule),
FOREIGN KEY (ID_Traitement) REFERENCES TRAITEMENT(ID)
);

CREATE TABLE REL_MEDICAMENT_ESPECE (
NomMolecule VARCHAR NOT NULL,
Espece VARCHAR NOT NULL,
FOREIGN KEY (NomMolecule) REFERENCES MEDICAMENT(NomMolecule),
FOREIGN KEY (Espece) REFERENCES ESPECE(Espece)
);


INSERT INTO ESPECE (Espece) VALUES ('Félins');
INSERT INTO ESPECE (Espece) VALUES ('Canidés');
INSERT INTO ESPECE (Espece) VALUES ('Reptiles');
INSERT INTO ESPECE (Espece) VALUES ('Rongeurs');
INSERT INTO ESPECE (Espece) VALUES ('Oiseaux');
INSERT INTO ESPECE (Espece) VALUES ('autres');


INSERT INTO PATIENT (ID, Nom, DateDeNaissance, Taille, NumeroPuceID, NumeroPasseport, Espece)
VALUES (1, 'Oscar', '2008-08-21', 'Petite', 1, 26, 'Reptiles') ;

INSERT INTO PATIENT (ID, Nom, DateDeNaissance, Taille, NumeroPuceID, NumeroPasseport, Espece)
VALUES (2, 'Loulou', '2012-07-12', 'Petite', 2, 196, 'Canidés') ;

INSERT INTO PATIENT (ID, Nom, DateDeNaissance, Taille, NumeroPuceID, NumeroPasseport, Espece)
VALUES (3, 'Pilou', '2016-02-07', 'Moyenne', 3, 238, 'Oiseaux') ;



INSERT INTO CLIENT (ID, Nom, Prenom, DateDeNaissance, Adresse, NumeroTel)
VALUES (1, 'Kerjean', 'Loïck', '2000-07-26', '30 rue de paris 60200', '0659046286') ;

INSERT INTO CLIENT (ID, Nom, Prenom, DateDeNaissance, Adresse, NumeroTel)
VALUES (2, 'Trupin', 'Louis', '1999-08-22', '10 rue de la liberté 02600', '0756927645') ;



INSERT INTO PERSONNEL ( ID, Nom, Prenom, DateDeNaissance, Adresse, NumeroTel, Poste)
VALUES (1, 'Machin', 'Jean', '1965-12-12', '15 rue de Paris 60200', '0657834586', 'Veto') ;

INSERT INTO PERSONNEL ( ID, Nom, Prenom, DateDeNaissance, Adresse, NumeroTel, Poste)
VALUES (2, 'Bidule', 'Pierre', '1982-04-14', '1 rue de la corne du Cerf 60200', '0633562312', 'Assistant') ;



INSERT INTO MEDICAMENT (NomMolecule, Description) VALUES ('Paracétamol', 'calme les douleurs') ;
INSERT INTO MEDICAMENT (NomMolecule, Description) VALUES ('Benzopine', 'contre les inflammations') ;
INSERT INTO MEDICAMENT (NomMolecule, Description) VALUES ('Triplenide', 'réduit les saignements') ;

INSERT INTO MESURE (ID, IDPatient, DateEtHeure, Taille, poids) VALUES (1, 1, '2020-10-22', 'Petite', 20 );
INSERT INTO MESURE (ID, IDPatient, DateEtHeure, Taille, poids) VALUES (2, 2, '2019-08-23', 'Moyenne', 37 );

INSERT INTO TRAITEMENT (ID, IDPatient, DateEtHeure, DateDebut, Duree) VALUES (1, 1, '2020-10-22', '2020-11-01', 20);
INSERT INTO TRAITEMENT (ID, IDPatient, DateEtHeure, DateDebut, Duree) VALUES (2, 2, '2019-08-23', '2019-09-01', 30);
INSERT INTO TRAITEMENT (ID, IDPatient, DateEtHeure, DateDebut, Duree) VALUES (3, 2, '2019-08-25', '2019-10-01', 24);

INSERT INTO  RESULTAT_ANALYSE (ID, IDPatient, DateEtHeure, Resultat) VALUES (1, 1, '2020-10-22', 'bons');
INSERT INTO  RESULTAT_ANALYSE (ID, IDPatient, DateEtHeure, Resultat) VALUES (2, 2, '2019-08-23', 'moyens');

INSERT INTO OBSERVATION_GENERALE (ID, IDPatient, IDPersonnel, DateEtHeure, Observation) VALUES (1, 1, 1, '2020-10-22', 'rien à signaler');
INSERT INTO OBSERVATION_GENERALE (ID, IDPatient, IDPersonnel, DateEtHeure, Observation) VALUES (2, 2, 1, '2019-08-23', 'rien à signaler' );

INSERT INTO PROCEDURE (ID, IDPatient, DateEtHeure, Description) VALUES (1, 1, '2020-10-22', 'en cours' );
INSERT INTO PROCEDURE (ID, IDPatient, DateEtHeure, Description) VALUES (2, 2, '2019-08-23', 'en cours' );

INSERT INTO REL_TRAITEMENT_MEDICAMENT (NomMolecule, id_traitement, quantite) VALUES ('Triplenide', 1, 50);
INSERT INTO REL_TRAITEMENT_MEDICAMENT (NomMolecule, id_traitement, quantite)  VALUES ('Benzopine', 2, 10);
INSERT INTO REL_TRAITEMENT_MEDICAMENT (NomMolecule, id_traitement, quantite)  VALUES ('Benzopine', 1, 30);




