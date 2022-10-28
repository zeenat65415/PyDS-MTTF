class Cat:
    #constructor 
    def _init_(self, name, age, breed):
        #self refers to the class itself .it is a keyword like this in java. _init_ is a constructor.In java constructor name is same as class name.
        #syntax for instance_variable:
        #self.<attribute> = <parameter>
        self.name = name
        self.age = age
        self.breed = breed

cat1= Cat("Soni", 3 ,"persian")
cat2= Cat("Mia" ,2 ,"Siamese")
cat3= Cat("Molly" ,4 ,"Egyptian")

print(cat1.name, cat1.age, cat1.breed)
print(cat2.name, cat2.age, cat2.breed)
print(cat3.name, cat2.age, cat3.breed)
