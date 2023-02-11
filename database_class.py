class Patient:

    def __init__(self, firstname, lastname, mrn, age):
        self.firstname = ""
        self.lastname = ""
        self.mrn = 0
        self.age = 0
        self.tests = []

    def get_full_name(self):
        full_name = self.firstname + " " + self.lastname
        return full_name

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False


def main():
    new_patient = Patient("Anusha", "Krishnamoorthy", 2, 22)
    second_patient = Patient("Ann", "Ables", 1, 13)
    print(new_patient)
    print(second_patient)
    new_patient.tests.append(("HDL", 100))
    print(new_patient.get_full_name())
    print(new_patient.tests)
    print(second_patient.firstname)
    print(second_patient.age)
    print(second_patient.is_adult())


if __name__ == "__main__":
    main()
