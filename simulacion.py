from calculadoraCom import *

def main():
   print()
   
def canicas(proba,vector,rendijas):
   for i in range(rendijas):
      vector = multi_matrices(proba,vector)
   return vector

def  cuantico_de_rendijas(proba,vector,rendijas,target):
   if len(proba) != target:
      print("Error")
   else:
      for i in range(rendijas):
         vector = multi_matrices(proba,vector)
   return vector

def probabilistico_mas_de_dos_rendijas(proba,vector,rendijas,target):
   if len(proba) != target:
      print("Error")
   else:
      for i in range(rendijas):
         vector = multi_matrices(proba,vector)
   return vector



   
main()
