class pillarmen:
    species = "pillarmen"
    def __init__(self, name, age):
        self.name = name
        self.age = age
kars = pillarmen("kars", 102000)
wamuu = pillarmen("wamuu", 12000)
print("kars is a {}".format(kars.species))
print("wamuu is also one of the {}".format(wamuu.species))
print("{} is {} years old".format( kars.name, kars.age))
print("{} is {} years old".format( wamuu.name, wamuu.age))