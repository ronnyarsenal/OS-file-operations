__author__ = 'ron'
def readFile():
 Name = input("what is the name of the file?")
 file_object = open(Name,"r")
 contents = file_object.read()
 print(contents)
 file_object.close()
