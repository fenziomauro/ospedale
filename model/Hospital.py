from model.Doctor import Doctor
from model.Person import Person


class Hospital:
    def __init__(self):
        self.person=list()
        self.employ=list()


    def addPerson(self, name, surname, personId):
        self.person.append(Person(name,surname,personId))

    def addDoctor(self, name, surname, personId, doctorId):
       self.employ.append(Doctor(name, surname, personId, doctorId))



    ## Person not present exception
    def getPerson(self, personId):
        for pers in self.person:
            if pers.personId==personId:
                return pers

            else:
                print("non presente")



    ## Doctor not present exception
    def getDoctor(self, doctorId):
        for doctor in self.employ:
            if doctorId == doctor.doctorId:
                return doctor
            else:
                print("Dottore non presente")

    def assignDoctor(self, doctorId, personId):
        for d in self.employ:
            if d.doctorId == doctorId:
                doc=d
            break
        for p in self.person:
            if p.personId == personId:
                pat=p
            break
        doc.addPatient(pat)
        pat.setDoctor(doc)
