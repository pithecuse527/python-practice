import pickle

myMovie = {"Superman vs Batman" : 9.8, "Ironman" : "9.6"}

pickle.dump(myMovie, open("save.p", "wb"))

myMovie2 = pickle.load(open("save.p", "rb"))
print(myMovie2)
