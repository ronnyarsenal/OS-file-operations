import os #operating system module

def CreateDirectory(): 
    path = input("insert the path you would like to create:") 
    os.mkdir(path)

def DeleteDirectory():
    path = input("Insert the path you would like to remove")
    os.removedirs(path)

def ChangeDirectory():
    path = input("Select new directory")
    os.chdir(path)
