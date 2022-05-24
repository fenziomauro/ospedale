from model.Person import Person


class Doctor(Person):
    def __init__(self, name, surname, code, doctorId):
        super().__init__(name, surname, code)
        self.doctorId = doctorId
        self.patients = []

    def getDoctorId(self):
        return(self.doctorId)

    def addPatient(self, person):
       if len(self.patients)==0:
           self.patients.append(person)
       else:
           for i in self.patients:
            if i.personId==self.personId or i.personId==person.personId:
                print("Il medico e il paziente corrispondono oppure la persona è gia paziente di questo medico")
            else:
                print("test")



    def getPatients(self):
        if len(self.patients)>0:
            print("I pazienti assegnati al dottor:",self.name,self.surname,"sono:")
            for i in self.patients:
                print(i.name,i.surname)
        else:
            print("Il medico non ha pazienti")
