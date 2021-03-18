#!/usr/local/bin/python3
import psycopg2
import os
import datetime
import json 



def print_rapport(conn):
    cur = conn.cursor()

    print("\t### Résumé ###")
    sql = "SELECT * FROM NBR_MESURE;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\t Nombre de mesures : %s" % (res[0]))

    sql = "SELECT * FROM NBR_RESULTAT_ANALYSE;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\t Nombre de résultats d'analyses : %s" % (res[0]))

    sql = "SELECT * FROM NBR_TRAITEMENT;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\t Nombre de traitements : %s" % (res[0]))

    sql = "SELECT * FROM NBR_PROCEDURE;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\t Nombre de procédures : %s" % (res[0]))

    sql = "SELECT * FROM NBR_PATIENTS_EN_COURS;"
    cur.execute(sql)
    res = cur.fetchall()
    print("\n\t Nombre de patients actuels : %s" % (res[0]))

    print("\n\n\tConsommation de médicaments")
    sql = "SELECT * FROM STATS_MEDICAMENTS;"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print("\t - %s (%s)" % (raw[0],raw[1]))

    print("\n\n\tNombre de traitements par espèces")
    sql = "SELECT * FROM NBR_TRAITEMENT_PAR_ESPECE;"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print("\t - %s (%s)" % (raw[0],raw[1]))
    input()
