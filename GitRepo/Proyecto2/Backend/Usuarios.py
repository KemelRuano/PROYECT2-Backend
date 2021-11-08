class Users:
     def __init__(self,nombre,genero ,nombreus,correo,contraseña):
         self.nombre = nombre
         self.genero = genero
         self.nombreus = nombreus
         self.correo = correo
         self.contraseña = contraseña

#------------------------------------- Metodo get

     def getNombre(self):
          return self.nombre
     
     def getGenero(self):
          return self.genero
     
     def getNombreUs(self):
          return self.nombreus
     def getCorreo(self):
          return self.correo

     def getContras(self):
          return self.contraseña
     
     
     
     
#--------------------------------------Metodo set       

     def setNombre(self , nombre):
          self.nombre = nombre
     
     def setGenero(self , genero):
         self.genero = genero

     def setNombreUsuario(self , nombreus):
          self.nombreus = nombreus
          
     def setCorreo(self, correo):
          self.correo = correo
     
     def setContras(self, contraseña):
          self.contraseña = contraseña






