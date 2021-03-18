#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 

def personnel_menu(conn):
    choice = 0
    continu = True
    while(continu):
        os.system("clear")
        print("\n\t\tGestion du personnel")
        print("\n\t### Que voulez-vous faire ? ###")
        print("\t0\tRevenir au menu principal\n")
        print("\t1\tVoir les membres du personnel")
        print("\t2\tAjouter un membre du personnel")
        print("\t3\tModifier un membre du personnel")
        print("\t4\tRechercher un personnel par son nom ou prénom")
        print("\t5\tVoir le détail de la fiche d'un membre du personnel")
        choice = int(input("\n> "))
        os.system("clear")

        if(choice == 0):
            continu = False
            print("\n\tRetour au menu")
        elif(choice == 1):
            voir_membres_personnel(conn)
        elif(choice==2):
            ajouter_membre_personnel(conn)
        elif(choice==3):
            modifier_membre_personnel(conn)
        elif(choice==4):
            rechercher_membre_personnel(conn)
        elif(choice==5):
            detail_membre_personnel(conn)


def voir_membres_personnel(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM PERSONNEL ORDER BY ID ASC;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les membres du personnel :")
    print("\t#ID")
    for raw in res:
        print("\t#%s\tPOSTE : %s\t%s %s" % (raw[0], raw[6], raw[1], raw[2]))
    input()
    cur.close()

def ajouter_membre_personnel(conn):  
    cur = conn.cursor()
    print("\tInsertion d'un nouveau membre du personnel :")
    nom = quote(input("\tIndiquez le nom\n\t> "))
    prenom = quote(input("\tIndiquez le prénom\n\t> "))
    adresse = quote(input("\tIndiquez l'adresse\n\t> "))
    numero_tel = quote(input("\tIndiquez le numéro de téléphone\n\t> "))    
    annee_bd = int(input("\tIndiquez l'annee de naissance\n\t> "))
    mois_bd = int(input("\tIndiquez le mois de naissance\n\t> "))
    jour_bd= int(input("\tIndiquez le jour de naissance\n\t> "))
    date_de_naissance= quote(datetime.date(annee_bd, mois_bd, jour_bd))
    poste = quote(input("\tIndiquez le poste (Veto, Assistant)\n\t> "))
    specialites = []
    specialite = "aa"
    while specialite != "":
        print("\tSpecialites possibles :")
        sql = "SELECT * FROM ESPECE ORDER BY ESPECE ASC"
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            print("\t- %s" % (result[0]))
        specialite = str(input("\n\tIndiquez une spécialité à ajouter ('entrée' quand fini)\n\t> "))
        if(specialite!=""):
            sql = "SELECT * FROM ESPECE WHERE ESPECE=%s;" % (quote(specialite))
            cur.execute(sql)
            if(cur.fetchall()):
                specialites.append(specialite)
                print("\tLa spécialité a été ajoutée")
            else:
                print("\t! La spécialité indiquée n'existe pas")
    try: 
        sql = "INSERT INTO PERSONNEL (Nom, Prenom, DateDeNaissance, Adresse, NumeroTel, Poste, Specialites) VALUES (%s, %s, %s, %s, %s, %s, '{\"specialites\" : %s}');" % (nom, prenom, date_de_naissance, adresse, numero_tel, poste, json.dumps(specialites))
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def modifier_membre_personnel(conn):
    print("\tVeuillez indiquer l'ID du personnel à modifier :")
    id = int(input("\n> "))
    print("\n\tVeuillez indiquer l'information que vous voulez modifier :")
    print("\tnom")
    print("\tprenom")
    print("\tadresse")
    print("\tnumeroTel")
    print("\tposte")
    print("\tspecialites")
    column = str(input("\n> "))
    cur = conn.cursor()
    if(column=="specialites"):
        specialites = []
        specialite = "aa"
        while specialite != "":
            print("\tSpecialites possibles :")
            sql = "SELECT * FROM ESPECE ORDER BY ESPECE ASC"
            cur.execute(sql)
            results = cur.fetchall()
            for result in results:
                print("\t- %s" % (result[0]))
            specialite = str(input("\n\tIndiquez une spécialité à ajouter ('entrée' quand fini)\n\t> "))
            if(specialite!=""):
                sql = "SELECT * FROM ESPECE WHERE ESPECE=%s;" % (quote(specialite))
                cur.execute(sql)
                if(cur.fetchall()):
                    specialites.append(specialite)
                    print("\tLa spécialité a été ajoutée")
                else:
                    print("\t! La spécialité indiquée n'existe pas")
        value = quote("{\"specialites\" : %s}" % (json.dumps(specialites)))
    else:
        print("\n\tVeuillez indiquer la nouvelle valeur :")
        value = quote(input("\n> "))
    try:
        sql = "UPDATE PERSONNEL SET %s = %s WHERE ID=%i;" % (column,value,id)
        cur.execute(sql)
        print("\tCommande exécutée")
        conn.commit()
        cur.close()
    except psycopg2.Error:
        conn.rollback()
        print("Erreur lors de la mise à jour, merci de réessayer.")

def rechercher_membre_personnel(conn):
    print("\tVeuillez indiquer le nom ou prénom du personnel :")
    string = quote(input("\n> "))
    cur = conn.cursor()
    sql = "SELECT * FROM PERSONNEL WHERE strpos(nom,%s)>0 OR strpos(prenom,%s)>0 ORDER BY ID ASC;" % (string,string)
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les membres du personnel trouvés pour votre requête :")
    print("\t#ID")
    for raw in res:
        print("\t#%s\tPOSTE : %s\t%s %s" % (raw[0], raw[6], raw[1], raw[2]))
    input()
    cur.close()

def detail_membre_personnel(conn):
    print("\tVeuillez indiquer l'ID du membre du personnel :")
    ID = int(input("\n> "))
    cur = conn.cursor()
    sql = "SELECT * FROM PERSONNEL WHERE id=%i;" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\t#ID : %i" % (ID))
    for raw in res:
        print("\t%s %s (né le %s)" % (raw[2],raw[1],raw[3]))
        print("\tPoste : %s" % (raw[6]))
        print("\tTelephone : %s" % raw[5])
        print("\tAdresse : %s" % raw[4])
        try:
            print("\tSpecialités :")
            for specialite in raw[7]["specialites"]:
                print("\t  - %s" % (specialite))
        except:
            pass

    sql = "SELECT * FROM SOIGNANT_ACTUEL WHERE ID_Personnel=%i" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\n\tPatients actuels")
    for raw in res:
        print("\t  - #%s\t%s (depuis le %s)" % (raw[1],raw[0],raw[5]))
   
    sql = "SELECT * FROM SOIGNANT_PASSE WHERE ID_Personnel=%i" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\n\tAnciens patients")
    for raw in res:
        print("\t  - #%s\t%s (du %s au %s)" % (raw[1],raw[0],raw[5],raw[6]))
    print('\n')
    input()
    cur.close()

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'
