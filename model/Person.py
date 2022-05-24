

class Person:
    def __init__(self, name, surname, personId):
        self.name = name
        self.surname = surname
        self.personId = personId
        self.doctors=[]


    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getId(self):
        return self.personId

    def setDoctor(self, doctor):
        if len(self.doctors)==0:
            self.doctors.append(doctor)
            print("dottore aggiunto")
        else:
            for i in self.doctors:
                if i.doctorId == doctor.doctorId:
                    print("Il dottor.",doctor.name,doctor.surname,"è gia un tuo medico")
                else:
                    self.doctors.append(doctor)
                    print("dottore aggiunto")


    def getDoctor(self):
        return self.doctor
