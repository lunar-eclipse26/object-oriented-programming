class doge:
    species = "doge"
    def __init__(self, name, height):
        self.name = name
        self.height = height
corgi = doge("corgi", 25)
jjba = doge("jonathans dog", 76)
print("corgi is a {}".format(corgi.species))
print("jonathans dog is also a {}".format(jjba.species))
print("{} is {} cm tall".format( corgi.name, corgi.height))
print("{} is {} cm tall".format( jjba.name, jjba.height))