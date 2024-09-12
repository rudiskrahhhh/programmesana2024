class Cilveks : 
    def __init__(self,vards,dzimums,vecums) :
        self.name=vards
        self.sex=dzimums
        self.age=vecums
    def dzimene(self) :
        self.age +=1
        self.bazars()
    
    def mainit_dzimumu(self, jaunais_dzimums):
        if jaunais_dzimums == "":
            if self.sex == "s":
                self.sex = "v"
            else:
                self.sex = "s"
        else:
            self.sex = jaunais_dzimums
        self.bazars()
            
    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards
        self.bazars()




    def bazars(self) :
        if self.sex == "V":
            dzimums = "vīrietis"
        elif self.sex == "S":
            dzimums = "sieviete"
        else:
            dzimums = self.sex
        print("Sveiki, mani sauc {}, es esmu {} gadus vecs. Es esmu {}".format(self.name, self.age, dzimums))
	
persona=Cilveks("Rudis","V",18)

persona.dzimene()

persona.bazars() 