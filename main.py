from model.Hospital import Hospital


StGeorge=Hospital()
StGeorge.addDoctor("Mario","Rossi","A113B","Fisio1")
StGeorge.addPerson("marco","ferri","A123Z")
#StGeorge.getPerson("A123Z")
#print(Person.getName("A123Z"))
rossi=StGeorge.getDoctor("Fisio1")
rossi.addPatient(StGeorge.getPerson("A123Z"))
rossi.addPatient(StGeorge.getPerson("A123Z"))
rossi.getPatients()
StGeorge.assignDoctor("Fisio1","A123Z")
#rossi=StGeorge.getDoctor("Fisio1")
rossi.getPatients()
#paz=StGeorge.getPerson("A123Z")

