#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 

def client_menu(conn):
    choice = 0
    continu = True
    while(continu):
        os.system("clear")
        print("\n\t\tGestion des clients")
        print("\n\t### Que voulez-vous faire ? ###")
        print("\t0\tRevenir au menu principal\n")
        print("\t1\tVoir les clients")
        print("\t2\tAjouter un client")
        print("\t3\tModifier un client")
        print("\t4\tRechercher un client par son nom ou prénom")
        print("\t5\tVoir le détail de la fiche d'un client")
        
        choice = int(input("\n> "))
        os.system("clear")

        if(choice == 0):
            continu = False
            print("\n\tRetour au menu")
        elif(choice == 1):
            voir_clients(conn)
        elif(choice==2):
            ajouter_client(conn)
        elif(choice==3):
            modifier_client(conn)
        elif(choice==4):
            rechercher_client(conn)
        elif(choice==5):
            detail_client(conn)


def voir_clients(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM CLIENT ORDER BY ID ASC;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les clients :")
    print("\t#ID")
    for raw in res:
        print("\t#%s\t%s %s" % (raw[0], raw[1], raw[2]))
    input()
    cur.close()

def ajouter_client(conn):  
    cur = conn.cursor()
    print("\tInsertion d'un nouveau client :")
    nom = quote(input("\tIndiquez le nom\n\t> "))
    prenom = quote(input("\tIndiquez le prénom\n\t> "))
    adresse = quote(input("\tIndiquez l'adresse\n\t> "))
    numero_tel = quote(input("\tIndiquez le numéro de téléphone\n\t> "))    
    annee_bd = int(input("\tIndiquez l'annee de naissance\n\t> "))
    mois_bd = int(input("\tIndiquez le mois de naissance\n\t> "))
    jour_bd= int(input("\tIndiquez le jour de naissance\n\t> "))
    date_de_naissance= quote(datetime.date(annee_bd, mois_bd, jour_bd))

    try: 
        sql = "INSERT INTO CLIENT (Nom, Prenom, DateDeNaissance, Adresse, NumeroTel) VALUES (%s, %s, %s, %s, %s);" % (nom, prenom, date_de_naissance, adresse, numero_tel)
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def modifier_client(conn):
    print("\tVeuillez indiquer l'ID du client à modifier :")
    id = int(input("\n> "))
    print("\n\tVeuillez indiquer l'information que vous voulez modifier :")
    print("\tnom")
    print("\tprenom")
    print("\tadresse")
    print("\tnumeroTel")
    column = str(input("\n> "))
    cur = conn.cursor()
    print("\n\tVeuillez indiquer la nouvelle valeur :")
    value = quote(input("\n> "))
    try:
        sql = "UPDATE CLIENT SET %s = %s WHERE ID=%i;" % (column,value,id)
        cur.execute(sql)
        print("\tCommande exécutée")
        conn.commit()
        cur.close()
    except psycopg2.Error:
        print("Erreur lors de la mise à jour, merci de réessayer.")

def rechercher_client(conn):
    print("\tVeuillez indiquer le nom ou prénom du client :")
    string = quote(input("\n> "))
    cur = conn.cursor()
    sql = "SELECT * FROM CLIENT WHERE strpos(nom,%s)>0 OR strpos(prenom,%s)>0 ORDER BY ID ASC;" % (string,string)
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les clients trouvés pour votre requête :")
    print("\t#ID")
    for raw in res:
        print("\t#%s\t%s %s" % (raw[0], raw[1], raw[2]))
    input()
    cur.close()

def detail_client(conn):
    print("\tVeuillez indiquer l'ID du client:")
    ID = int(input("\n> "))
    cur = conn.cursor()
    sql = "SELECT * FROM CLIENT WHERE id=%i;" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\t#ID : %i" % (ID))
    for raw in res:
        print("\t%s %s (né le %s)" % (raw[2],raw[1],raw[3]))
        print("\tTelephone : %s" % raw[5])
        print("\tAdresse : %s" % raw[4])
    
    sql = "SELECT * FROM PROPRIETAIRE_ACTUEL WHERE ID_Client=%i" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\n\tAnimaux actuels")
    for raw in res:
        print("\t  - #%s\t%s (depuis le %s)" % (raw[1],raw[0],raw[5]))
   
    sql = "SELECT * FROM PROPRIETAIRE_PASSE WHERE ID_Client=%i" % (ID)
    cur.execute(sql)
    res = cur.fetchall()
    print("\n\tAnciens animaux")
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
