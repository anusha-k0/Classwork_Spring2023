def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient
   
def main_driver():
    db = []
    db.append(create_patient_entry('Ann Ables', 1, 34))
    db.append(create_patient_entry('Bob Boyles', 2, 24))
    db.append(create_patient_entry('Charles Lyles', 3, 65))
    print(db)
    add_test_to_patient(1, db, "HDL", 120)
    add_test_to_patient(2, db, "LDL", 100)
    add_test_to_patient(2, db, "HDL", 99)
    room_numbers = ["103", "232", "333"]
    print(db)
    print_directory(db, room_numbers)
    test_val1 = test_value_finder(db, 2, 'LDL')
    print(test_val1)
    
def test_value_finder(db, mrn_to_find, test_name):
    for patient in db:
        if patient[1] == mrn_to_find:
            for test in patient[3]:
                if test[0] == test_name:
                    return test[1]
                else:
                    print('Test not done!')
    else:
        print('MRN not found')
            
            
    
def print_directory(db, room_numbers):
    for idx, patient in enumerate(db):
        print(f"Patient {db[idx][0]} in room {room_numbers[idx]}")
    for patient, rn in zip(db, room_numbers):
        print(f"Patient {patient[0]} in room {rn}")
    
    #print("Get patient Ann")
    #mrn_to_find = 4
    #found_patient = get_patient_entry(mrn_to_find, db)
    #if found_patient is False:
     #   print(f"Patient MRN ({mrn_to_find}) not found")
    #print(found_patient)
    
def get_patient_entry(mrn_to_find, db):
    for patient in db:
        if mrn_to_find == patient[1]:
            return patient
    return False
    
def add_test_to_patient(mrn_to_find, db, test_name, test_value):
    patient = get_patient_entry(mrn_to_find, db)
    if patient == False:
        print("Bad Entry")
    else:
        patient[3].append([test_name, test_value])
    
if __name__ =="__main__":
    main_driver()
    