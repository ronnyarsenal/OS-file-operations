__author__ = 'ron'
def CreateFile():
 Name = input("what is the name of the file you wish to create")
 file_object = open(Name,"w")
 print(Name + " created")
