#!/usr/local/bin/python3
import psycopg2
import os
from personnel import personnel_menu
from clients import client_menu
from patients import patient_menu
from especes import espece_menu
from medicaments import medicament_menu
from rapports import print_rapport

def init(conn):
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cursor.fetchall()
    for row in rows:
        try:
            cursor.execute("drop table IF EXISTS " + row[1] + " cascade")
        except psycopg2.Error:
            pass
        try:
            cursor.execute("drop view IF EXISTS " + row[1] + " cascade")
        except psycopg2.Error:
            pass
    sqlfile = open('init.sql', 'r')
    cursor.execute(sqlfile.read())
    cursor.close()
    print("\tInitialisation de la BDD correctement effectuée.")


def menu(conn):
    os.system("clear")
    print('\tVous etes bien connectes !')

    choice = 0
    continu = True
    while(continu):
        print("\n\t### Que voulez-vous faire ? ###")
        print("\n\t0\tQuitter")
        print("\n\t1\tInitialisation de la BDD")
        print("\n\t2\tGestion des clients")
        print("\t3\tGestion des patients")
        print("\t4\tGestion du personnel")
        print("\t5\tGestion des espèces")
        print("\t6\tGestion des médicaments")
        print("\n\t7\tVoir le rapport")
        
        try:
            choice = int(input("\n> "))
        except:
            pass
        os.system("clear")

        if(choice == 0):
            continu = False

            print("\n\tAu revoir.")
        elif(choice == 1):
            os.system("clear")
            print("\n\tEtes-vous sûr d'initialiser la BDD ? Cela supprimera les tables et données déjà existentes.")
            print("\t0\tNon")
            print("\tautre\tOui")
            choice = int(input("\n> "))
            if(choice != 0):
                init(conn)
        elif(choice == 2):
            client_menu(conn)
        elif(choice == 3):
            patient_menu(conn)
        elif(choice == 4):
            personnel_menu(conn)
        elif(choice == 5):
            espece_menu(conn)
        elif(choice == 6):
            medicament_menu(conn)
        elif(choice == 7):
            print_rapport(conn)
def main():
    try:
        server = quote(
            input("Nom du serveur : "))
        dbname = quote(input("Nom de la BDD : "))
        username = quote(input("Nom utilisateur : "))
        password = quote(input("Mot de passe : "))
        # server = 'localhost'
        # dbname = 'nf18'
        # username = 'postgres'
        # password = 'admin'
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (
            server, dbname, username, password))

        menu(conn)
        conn.close()
        print("\n\tVous êtes déconnecté.")

    except psycopg2.Error as e:
        print("\n\tLa connexion a échoué...")
        print(e)


def quote(s):
    if s:
        return '\'%s\'' % s
    else:
        return 'NULL'


# Exécution du programme
main()
