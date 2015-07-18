from Append import * 
from Write import *
from Read import *
from Directory import *  # these import all of the needed functions

L = 0 # L for loop
while L != 1 :
 print(" A = Append")
 print(" D = Directory")
 print(" R = Read")
 print(" W = Write")
 print(" Q = quit")

 Choice = input("what is your input").strip().upper() #removes whitespace and capitalizes input
 if Choice == 'A':
  appendFile()
 if Choice == 'D':
     print("C = Create Directory")
     print("D = Delete Directory")
     print("X = Change Directory")
     Choice = input().strip().upper()
     if Choice == 'C':
        CreateDirectory()
     if Choice == 'D':
        DeleteDirectory()
     if Choice == 'X':
        ChangeDirectory()
 if Choice == 'R':
     readFile()
 if Choice == 'W':
     CreateFile()
 if Choice == 'Q': #breaks loop
     L = 1 
