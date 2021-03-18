#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 

def espece_menu(conn):
    choice = 0
    continu = True
    while(continu):
        os.system("clear")
        print("\n\t\tGestion des espèces")
        print("\n\t### Que voulez-vous faire ? ###")
        print("\t0\tRevenir au menu principal\n")
        print("\t1\tVoir les espèces")
        print("\t2\tAjouter une espèce")
        choice = int(input("\n> "))
        os.system("clear")

        if(choice == 0):
            continu = False
            print("\n\tRetour au menu")
        elif(choice == 1):
            voir_especes(conn)
        elif(choice==2):
            ajouter_espece(conn)
       
def voir_especes(conn):
    cur = conn.cursor()
    sql = "SELECT * FROM ESPECE ORDER BY ESPECE ASC;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\tVoici les espèces :")
    for raw in res:
        print("\t - %s" % (raw[0]))
    input()
    cur.close()

def ajouter_espece(conn):  
    cur = conn.cursor()
    print("\tInsertion d'une nouvelle espèce :")
    nom = quote(input("\tIndiquez le nom de l'espèce\n\t> "))   
    try: 
        sql = "INSERT INTO ESPECE (Espece) VALUES (%s);" % (nom)
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
