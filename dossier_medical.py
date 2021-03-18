#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 

def dossier_medical_menu(conn,id):
    choice = 0
    os.system("clear")
    print("\n\t\tGestion du dossier medical du patient")
    print("\n\t### Que voulez-vous faire ? ###")
    print("\t0\tRevenir au menu principal\n")
    print("\t1\tAjouter un résultat d'analyse")
    print("\t2\tAjouter une mesure")
    print("\t3\tAjouter une procédure")
    print("\t4\tAjouter une observation")

    choice = int(input("\n> "))
    os.system("clear")

    if(choice == 1):
        ajouter_resultat_analyse(conn,id)
    elif(choice==2):
        ajouter_mesure(conn,id)
    elif(choice==3):
        ajouter_procedure(conn,id)
    elif(choice==4):
        ajouter_observation(conn,id)


def ajouter_mesure(conn,id):  
    cur = conn.cursor()
    taille = float(input("\tIndiquez une taille\n\t> ")) 
    poids = float(input("\tIndiquez un poids\n\t> "))    
    try: 
        sql = "INSERT INTO MESURE (IDPatient, DateEtHeure, Taille, Poids) VALUES (%s, NOW(), %s, %s);" % (id, taille, poids)
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def ajouter_resultat_analyse(conn,id):  
    cur = conn.cursor()
    resultat = quote(input("\tIndiquez le résultat (URL ou description)\n\t> "))    
    try: 
        sql = "INSERT INTO RESULTAT_ANALYSE (IDPatient, DateEtHeure, Resultat) VALUES (%s, NOW(), %s);" % (id, resultat)
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def ajouter_observation(conn,id):  
    cur = conn.cursor()
    ID_Personnel = quote(input("\tIndiquez l'ID du personnel soignant\n\t> "))    
    observation = quote(input("\tIndiquez l'observation faite\n\t> "))    
    try: 
        sql = "INSERT INTO OBSERVATION_GENERALE (IDPatient, IDPersonnel, DateEtHeure, Observation) VALUES (%s, %s, NOW(), %s);" % (id, ID_Personnel,observation)
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()



def ajouter_procedure(conn,id):  
    cur = conn.cursor()
    procedure = quote(input("\tIndiquez la procédure\n\t> ")) 
    try: 
        sql = "INSERT INTO PROCEDURE (IDPatient, DateEtHeure, Description) VALUES (%s, NOW(), %s);" % (id, procedure)
        cur.execute(sql)
        conn.commit()
        print("\tCommande exécutée")
    except psycopg2.IntegrityError as e: 
        conn.rollback()
        print(e)
    cur.close()

def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'
