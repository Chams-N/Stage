import mysql.connector

#menu
def menu():
    ch = -1;
    while (ch < 0) or (ch > 7):
        print("-------------------------------------------------------------------------------")
        print("1-Enregistrer un patient")
        print("2-Mise à jour d'un vaccin existant ou ajouter un nouveau vaccin")
        print("3-Mise à jour d'un serum existant ou ajouter un nouveau serum")
        print("4-Effacer vaccin à partir de son nombre de lot")
        print("5-Effacer serum à partir de son nombre de lot")
        print("6-Effacer sérotherapie à partir du numero cin du patient")
        print("0-Quitter")
        ch = int(input("Entrer le choix : "))
    return ch

def menu1():
    ch1 = -1;
    while (ch1 < 0) or (ch1 > 2):
        print("-------------------------------------------------------------------------------")
        print("1-Mise à jour d'un vaccin existant ")
        print("2-Ajouter un nouveau vaccin")
        print("0-Retour au menu principal")
        ch1 = int(input("Entrer le choix : "))
    return ch1


def menu2():
    ch2 = -1;
    while (ch2 < 0) or (ch2 > 2):
        print("-------------------------------------------------------------------------------")
        print("1-Mise à jour d'un vaccin existant ")
        print("2-Ajouter un nouveau vaccin")
        print("0-Retour au menu principal")
        ch2 = int(input("Entrer le choix : "))
    return ch2


#DataBase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    port=3306,
    database="python"
)

# Insert functions
def insertPatient(cin, nom, prenom, numero):
    cursor = mydb.cursor()
    sql = "INSERT INTO Patients VALUES (%s, %s, %s, %s)"
    val = (cin, nom, prenom, numero)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.fetchall(), "record inserted.")

def insertVaccin(dlc_vaccin, numero_lot, quantite):
    cursor = mydb.cursor()
    sql = "INSERT INTO Vaccins VALUES (%s, %s, %s)"
    val = (dlc_vaccin, numero_lot, quantite)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")

def insertSerum(dlc_serum, numero_lot, quantite, type_serum):
    cursor = mydb.cursor()
    sql = "INSERT INTO Serums VALUES (%s, %s, %s, %s)"
    val = (dlc_serum, numero_lot, quantite, type_serum)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")

def insertVaccination(date_vaccination, numero_lot, nombre_dose, patient_id):
    cursor = mydb.cursor()
    sql = "INSERT INTO vaccination VALUES (%s, %s, %s, %s)"
    val = (date_vaccination, numero_lot, nombre_dose, patient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")

def insertSerotherapie(dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot):
    cursor = mydb.cursor()
    sql = "INSERT INTO serotherapie VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")

# Delete functions

def deletePatient(patient_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM patients WHERE cin = %s"
    val = (patient_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

def deleteVaccin(vaccin_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM vaccins WHERE numero_lot = %s"
    val = (vaccin_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

def deleteSerum(serum_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM serums WHERE numero_lot = %s"
    val = (serum_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

def deleteVaccination(vaccination_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM vaccination WHERE patient_id = %s"
    val = (vaccination_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

def deleteSerotherapie(serotherapie_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM serotherapie WHERE patient_id = %s"
    val = (serotherapie_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

#Update functions

def updatePatient(oldPatientId, cin, nom, prenom, numero):  # to update you need the current id and then u add the new data(that concerns the id itself)
    cursor = mydb.cursor()
    sql = "UPDATE patients SET cin = %s, nom = %s, prenom = %s, numero = %s WHERE cin = %s"
    val = (cin, nom, prenom, numero, oldPatientId)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected.")

def updateVaccin(oldnumero_lot, dlc_vaccin, numero_lot, quantite):   # to update you need the current id and then u add the new data(that concerns the id itself)
    try:
        cursor = mydb.cursor()
        sql = "UPDATE vaccins SET dlc_vaccin = %s, numero_lot = %s, quantite = %s WHERE numero_lot = %s"
        val = (dlc_vaccin, numero_lot, quantite, oldnumero_lot)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) affected.")
    except mysql.connector.Error as err:
        print("Error:", err)
        mydb.rollback()  # Rollback changes if there's an error
    finally:
        cursor.close()


def updateSerum(oldnumero_lot, dlc_serum, numero_lot, quantite, type_serum):
    cursor = mydb.cursor()
    sql = "UPDATE serums SET dlc_serum = %s, numero_lot = %s, quantite = %s, type_serum = %s WHERE numero_lot = %s"
    val = (dlc_serum, numero_lot, quantite, type_serum, oldnumero_lot)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected.")

def updateVaccination(oldpatient_id, date_vaccination, numero_lot, nombre_dose, patient_id):
    cursor = mydb.cursor()
    sql = "UPDATE vaccination SET date_vaccination = %s, numero_lot = %s, nombre_dose = %s, patient_id = %s WHERE patient_id = %s"
    val = (date_vaccination, numero_lot, nombre_dose, patient_id, oldpatient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected.")

def updateSerotherapie(oldpatient_id, dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot):
    cursor = mydb.cursor()
    sql = "UPDATE serotherapie SET dose_id = %s, dose_total = %s, date_administration = %s, quantite_local = %s, quantite_generale = %s, patient_id = %s, numero_lot = %s WHERE patient_id = %s"
    val = (dose_id, dose_total, date_administration, quantite_local, quantite_generale, patient_id, numero_lot, oldpatient_id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) affected.")

#Get Functions

def getPatients():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM patients"
    cursor.execute(sql)
    return cursor.fetchall()

def getPatientByCin(cin):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM patient WHERE cin = %s"
    val = (cin,)
    cursor.execute(sql, val)
    return cursor.fetchall()

def getVaccins():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM vaccins"
    cursor.execute(sql)
    return cursor.fetchall()

def getVaccinByNmLot(numero_lot):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM vaccins WHERE numero_lot = %s"
    val = (numero_lot,)
    cursor.execute(sql, val)
    return cursor.fetchall()

def getSerum():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM serums"
    cursor.execute(sql)
    return cursor.fetchall()

def getSerumByNmLot(numero_lot):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM serums WHERE numero_lot = %s"
    val = (numero_lot,)
    cursor.execute(sql, val)
    return cursor.fetchall()

def getVaccination():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM vaccination"
    cursor.execute(sql)
    return cursor.fetchall()

def getSerotherapie():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM serotherapie"
    cursor.execute(sql)
    return cursor.fetchall()



