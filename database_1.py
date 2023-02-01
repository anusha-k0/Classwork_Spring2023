def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age]
    return new_patient
   
def main_driver():
    db = []
    db.append(create_patient_entry('Ann Ables', 1, 34))
    db.append(create_patient_entry('Bob Boyles', 2, 24))
    db.append(create_patient_entry('Charles Lyles', 3, 65))
    print(db)
    print(f'{db[0][0]}'s age: {db[0][1]}')
    
if __name__ =="__main__":
    main_driver()
    