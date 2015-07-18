__author__ = 'ron'
def appendFile(): #function to append
 Name = input("what is the name of the file?")
 file_object = open(Name,"a") 
 Text = input("Insert the text you would like to append")
 file_object.write("\n" + Text + " ")
 file_object.close()
