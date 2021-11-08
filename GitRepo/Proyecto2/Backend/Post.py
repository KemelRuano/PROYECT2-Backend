class posts:
    def __init__(self,URL,fecha,categoria,author):
        #self.tipo = tipo
        self.URL = URL
        self.fecha = fecha
        self.categoria = categoria
        self.author = author

#--------------------------------------Metodo get
    def getTipo(self):
        return self.tipo
    
    def getURL(self):
        return self.URL
    
    def getFecha(self):
        return self.fecha
    
    def getCategoria(self):
        return self.categoria
    
    def getAuthor(self):
        return self.author
#------------------------------------- Metodos set   
    def setTipo(self,tipo):
        self.tipo = tipo

    def setTipo(self,URL):
        self.URL = URL
    
    def setTipo(self,fecha):
        self.fecha = fecha
    
    def setTipo(self,categoria):
        self.categoria = categoria
        
    def setAuthor(self,author):
        self.author =  author


    


        