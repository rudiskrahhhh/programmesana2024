class Cilveks : 
    def __init__(self,vards,dzimums,vecums) :
        self.name=vards
        self.sex=dzimums
        self.age=vecums
    def dzimene(self) :
        self.age +=1
    def Bazars(self) :
        if self.sex == "V":
            dzimums = "vīrietis"
        elif self.sex == "S":
            dzimums = "sieviete"
        else:
            dzimums = self.sex
        print("Sveiki, mani sauc {}, es esmu {} gadus vecs. Es esmu {}".format(self.name, self.age, dzimums))
	
persona=Cilveks("Rudis","kjhakjhkjh",18)

persona.dzimene()

persona.Bazars() 