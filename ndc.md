## Classe :
- **Client :** Nom (string), prénom (string), date de naissance (date), adresse (string), téléphone (string)
- **Personnel :** Nom (string), prénom (string), date de naissance (date), adresse (string), téléphone (string), poste {véto, assistant}, specialites (json)
- **Patient (Classe composite) :** nom (string), date de naissance (date ou NULL), taille {petite, moyenne}, numéro de puce d’id (string ou NULL), numéro de passeport (string ou NULL)
- **Médicament :** NomMolécule (string), Description (string), InterditPour (json)
- **Espèce :** espèce {félins, canidés, reptiles, rongeurs, oiseaux, autres}
- **Mesure (Classe partie de Patient) :** Date et heure (datetime), taille (integer ou NULL), poids (float ou NULL) 
- **Traitement (Classe partie de Patient) :** Date et heure (datetime), DateDebut (date), Duree (integer)
- **Traitement_Quantité :** Quantité (integer)
- **Résultats_analyse (Classe partie de Patient) :** Date et heure (datetime), Résultat (string)
- **Observation_générale (Classe partie de Patient) :** Date et heure (datetime), Observation (string)
- **Procédure (Classe partie de Patient) :** Date et heure (datetime), Description (string)
- **Durée :** DateDebut (date), DateFin (date or NULL) (si NULL, c’est que c’est le proprio/soignant actuel)

## Association :
- Patient appartient à Client (\*,\*) + Durée associée
- Patient appartient à Espèce (\*,1)
- Patient est soigné par Personnel (\*,\*) + Durée associée
- Mesure compose le dossier médical de Patient (\*,1) 
- Traitement compose le dossier médical de Patient (\*,1) 
- Médicament est pris dans Traitement (\*,\*) + Traitement_quantité associé
- Résultat Analyse compose le dossier médical de Patient (\*,1) 
- Observation générale compose le dossier médical de Patient (\*,1)
- Observation générale faite par Personnel (\*,1)
- Procédure compose le dossier médical de Patient (\*,1)

## Héritages :
- Classe mère **individu_Humain :**  Nom (string), prénom (string), date de naissance (date), adresse (address), téléphone (number)
- Client et Personnel sont filles de cette classe mère.
On aurait une transformation de l'héritage par classes filles car il s'agit d'un héritage exclusif non complet. Les attributs clé primaire de la classe mère seraient alors utilisés comme clé primaire pour chaque classe fille.

## Contraintes et remarques :
- On suppose que chaque attribut est non NULL sauf si spécifié.
- La date_de_naissance pour patient peut être DD/MM/AAAA ou AAAA ou NULL
- La date_de_naissance pour client et personnel est sous la forme DD/MM/AAAA
- La date pour mesure, traitement, resultat_analyse, observation, procedure est sour la forme DD/MM/AAAA HH:MM
- Un personnel_soignant ne peut pas être propriétaire d'un patient
- Dans un lien client/patient ou personnel/patient si la dateFin est NULL, c’est que c’est le proprio/soignant actuel
- Un traitement ne peut être prescrit que par un personnel véto
- Un médicament ne peut pas être donné à un animal si son espèce est incompatible
- Dans mesure, poids et taille ne peuvent pas être NULL tous les deux


## Utilisateurs et droits d'accès de la BDD
- admin : accès complet en lecture et écriture
- personnel : accès aux patients et leur dossier médical (lecture et écriture), accès aux médicaments (lecture)
- client : accès à ses patients et son dossier médical (lecture)

## Vues
- Quantites de medicaments consommes
- Nombre de traitements
- Nombre de procedures effectuees
- Nombre de traitements par espece
- Soignant actuel pour un patient
- Soignant passé pour un patient
- Propriétaire actuel pour un patient
- Propriétaire passé pour un patient