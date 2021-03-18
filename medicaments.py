#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 

def medicament_menu(conn):
    choice = 0
    continu = True
    while(continu):
        os.system("clear")
        print("\n\t\tGestion des médicaments")
        print("\n\t### Que voulez-vous faire ? ###")
        print("\t0\tRevenir au menu principal\n")
        print("\t1\tVoir les médicaments")
        print("\t2\tAjouter un médicament")
        print("\t3\tModifier un médicament")
        print("\t4\tVoir le détail d'un médicament")
        choice = int(input("\n> "))
        os.system("clear")

        if(choice == 0):
            continu = False
            print("\n\tRetour au menu")
        elif(choice == 1):
            voir_medicaments(conn)
        elif(choice==2):
            ajouter_medicament(conn)
        elif(choice==3):
            modifier_medicament(conn)
        elif(choice==4):
            detail_medicament(conn)


def voir_medicaments(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM MEDICAMENT ORDER BY NomMolecule ASC;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les médicaments :")
    for raw in res:
        print("\t#%s" % (raw[0]))
    input()
    cur.close()

def ajouter_medicament(conn):  
    cur = conn.cursor()
    print("\tInsertion d'un nouveau médicament :")
    nom = quote(input("\tIndiquez le nom de la molécule\n\t> "))   
    description = quote(input("\tAjoutez une description du médicament\n\t> "))   
    especes = []
    espece = "aa"
    while espece != "":
        print("\tEspèces possibles :")
        sql = "SELECT * FROM ESPECE ORDER BY ESPECE ASC"
        cur.execute(sql)
        results = cur.fetchall()
        for result in results:
            print("\t- %s" % (result[0]))
        espece = str(input("\n\tIndiquez une espèce ne pouvant pas prendre le médicament ('entrée' quand fini)\n\t> "))
        if(espece!=""):
            sql = "SELECT * FROM ESPECE WHERE ESPECE=%s;" % (quote(espece))
            cur.execute(sql)
            if(cur.fetchall()):
                especes.append(espece)
                print("\tL'espèce a été ajoutée")
            else:
                print("\t! L'espèce indiquée n'existe pas")
    try: 
        sql = "INSERT INTO MEDICAMENT (nomMolecule, Description, interditPour) VALUES (%s, %s, '{\"interditPour\" : %s}');" % (nom, description, json.dumps(especes))
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def modifier_medicament(conn):
    print("\tVeuillez indiquer le nom de la molécule du médicament à modifier :")
    nomMolecule = quote(input("\n> "))
    print("\n\tVeuillez indiquer l'information que vous voulez modifier :")
    print("\tdescription")
    print("\tinterditPour")
    column = str(input("\n> "))
    cur = conn.cursor()
    if(column=="interditPour"):
        especes = []
        espece = "aa"
        while espece != "":
            print("\tEspèces possibles :")
            sql = "SELECT * FROM ESPECE ORDER BY ESPECE ASC"
            cur.execute(sql)
            results = cur.fetchall()
            for result in results:
                print("\t- %s" % (result[0]))
            espece = str(input("\n\tIndiquez une espèce ne pouvant pas prendre le médicament ('entrée' quand fini)\n\t> "))
            if(espece!=""):
                sql = "SELECT * FROM ESPECE WHERE ESPECE=%s;" % (quote(espece))
                cur.execute(sql)
                if(cur.fetchall()):
                    especes.append(espece)
                    print("\tL'espèce a été ajoutée")
                else:
                    print("\t! L'espèce indiquée n'existe pas")
        value = quote("{\"interditPour\" : %s}" % (json.dumps(especes)))
    else:
        print("\n\tVeuillez indiquer la nouvelle valeur :")
        value = quote(input("\n> "))
    try:
        sql = "UPDATE MEDICAMENT SET %s = %s WHERE nomMolecule=%s;" % (column,value,nomMolecule)
        cur.execute(sql)
        print("\tCommande exécutée")
        conn.commit()
        cur.close()
    except psycopg2.Error:
        conn.rollback()
        print("Erreur lors de la mise à jour, merci de réessayer.")

def detail_medicament(conn):
    print("\tVeuillez indiquer le nom de la molécule:")
    nomMolecule = quote(input("\n> "))
    cur = conn.cursor()
    sql = "SELECT * FROM MEDICAMENT WHERE nomMolecule=%s;" % (nomMolecule)
    cur.execute(sql)
    res = cur.fetchall()
    print("\t#Molécule : %s" % (nomMolecule))
    for raw in res:
        print("\tDescription : %s" % raw[1])
        try:
            print("\tInterdit pour les espèces :")
            for espece in raw[2]["interditPour"]:
                print("\t  - %s" % (espece))
        except:
            pass
    input()
    cur.close()

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'
