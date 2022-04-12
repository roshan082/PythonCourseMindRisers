adj = input("Adjective : ")
verb1 = input("Verb : ")
verb2 = input("Verb Second : ")
famous_person = input("Famous Person : ")

def madlibs(inuput_adj, input_verb, input_verb1):
    madlib = f"Computer Programming is so {adj}! It makes me so exicited all the time because I love to {verb1}. Also Programmer or Developers should {verb2} 1.5 liters of water like {famous_person}."
    return madlib
print(madlibs(adj, verb1, verb2))
