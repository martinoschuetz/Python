class Rwc(object):

   __slots__= ("__d", "__vars", "__filename")

   def __init__(self,fname):
      self.__filename = fname
      self.__einlesen() 
  


   def __getD(self): return self.__d
   def __setD(self, d): self.__d = d
   d = property(__getD, __setD)


   def __getVars(self): return self.__vars
   def __setVars(self,vars): self.__vars = vars
   vars = property(__getVars, __setVars)

   def __getFilename(self): return self.__filename
   def __setFilename(self, f): self.__filename = f
   filename = property(__getFilename, __setFilename)
   
   
   import sys

   def __einlesen(self):
      f = open(self.__filename)
      self.__d = []

      line = f.readline().rstrip()

      print(line)
      self.__vars =  line.split(",")
      ll = len(self.__vars)
    
      weiter = True;

      while len(line)>0:

         line = f.readline().rstrip()

         vals = line.split(",")
      
         if len(vals)==ll:
            zd = {}
            for i in range(ll):
                zd[self.__vars[i]] = vals[i]
            self.__d.append(zd)

      # return (vars, d)
      print("einlesen beendet")


   def ausgeben(self, outf=""):
   
      import sys
      f2 = sys.stdout
      if outf : f2=open(outf,"w")

      
      print(",".join(self.__vars),file=f2)

      for listx in self.__d:
         e=[]
         for n in self.__vars: e.append(listx[n])
         record = ",".join(e)
         print(record, file=f2)

      if outf : f2.close()


if __name__=="__main__":

     r = Rwc("class.csv")
     r.ausgeben()

     r.ausgeben(outf="dummyX3.txt")

