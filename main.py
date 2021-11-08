
from flask import Flask,jsonify,request,render_template

from flask_cors import CORS

from Usuarios import Users
from Post import posts


import json
import re


Listado=[]
Video=[]
Imagen=[]
data = []
#--------------- para carga masiva
file = []
Carga = []
#--------------------
global numero
global contraseña
app = Flask(__name__)
CORS(app)

Listado.append(Users("Abner Cardona","M","admin","admin@ipc1.com","admin@ipc1"))




#-----------------------------------------------------------------------------------------------------

@app.route('/Listado', methods=['GET'])
def getListado():
    global Listado
    Datos = []
    for persona in Listado:
        objeto = {

            'name': persona.getNombre(),
            'gender': persona.getGenero(),
            'username': persona.getNombreUs(),
            'email': persona. getCorreo(),
            'password': persona. getContras()
            
        }
        Datos.append(objeto)  
    return(jsonify(Datos))


@app.route('/Listado/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 
    global Listado
    for persona in Listado:
        if persona.getNombreUs() == nombre:
  
            objeto = {
            'name': persona.getNombre(),
            'gender': persona.getGenero(),
            'username': persona.getNombreUs(),
            'email': persona. getCorreo(),
            'password': persona. getContras()
            }
            return(jsonify(objeto))     
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))
#--------------------------------------------------------------------------------------------------------------
@app.route('/Listado', methods=['POST'])
def Registro():
    global Listado
    nombre = request.json['name']
    genero = request.json['gender']
    nombreus = request.json['username']
    correo = request.json['email']
    contraseña = request.json['password']
#Validacion de contraseña   
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    pat = re.compile(reg)
    mat = re.search(pat,contraseña)
    if mat:
        print("exito")
    else:
        return jsonify({'Mensaje':'Contraseña invalida ---- Debe contener minimo 8  caracteres, un numero,un simbolo,Una letra',})    
# fin de validacion 
    for x in Listado:
        if( nombreus == x.getNombreUs()):
             return jsonify({'Mensaje':'el usuario ya existe',})
            
    NuevoObjet = Users(nombre,genero,nombreus,correo,contraseña)
    Listado.append(NuevoObjet)

    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})



#------------------------------------------------------------------------------------------------------------

@app.route('/Listado1', methods=['POST'])
def Login():
    if(  request.json['username'] == "admin" and request.json['password'] == "admin@ipc1" ): 
        return jsonify({'Mensaje1':'Bienvenido Administrador'})
         
    else:
        for Users in Listado:
           if(  request.json['username'] == Users.getNombreUs()): 
               if(request.json['password'] == Users.getContras()):
                   return jsonify({'Mensaje2':'Bienvenido'   + '-----------' + request.json['username']})
               else:
                   return jsonify({'Mensaje':'Contraseña incorrecta'})
           continue
        else:
           return jsonify({'Mensaje':'El usuario no existe',})

#---------------------------------------------------------------------------------------------------------------
#------------------------------------------------ POST VIDEOS------------------------------------------
@app.route('/Video', methods=['GET'])
def getListadoPosts():
    global Video
    Datos = []
    for x in Video:
        objeto12 = {
            'url': x.getURL(),
            'date': x.getFecha(),
            'category': x.getCategoria(),
            'author': x.getAuthor()
         
        }
        Datos.append(objeto12)  
    return(jsonify(Datos))
#----------------------------------------------------------------------------------------------

@app.route('/Video/<string:nombre>', methods=['GET'])
def ObtenerVideo(nombre): 
    global Video
    Datos = [] 
    for vid in Video:
        if vid.getAuthor() == nombre:  
            outlast = {
            'url': vid.getURL(),
            'date': vid.getFecha(),
            'category': vid.getCategoria(),
            'author': vid.getAuthor()
            }
            Datos.append(outlast)    
    return(jsonify(Datos))

@app.route('/Imagen/<string:nombre>', methods=['GET'])
def ObtenerImagen(nombre): 
    global Imagen
    Datos = []
    for ima in Imagen:
        if ima.getAuthor() == nombre:
  
            objeto = {
            'url': ima.getURL(),
            'date': ima.getFecha(),
            'category': ima.getCategoria(),
            'author': ima.getAuthor()
            }
            Datos.append(objeto)    
    return(jsonify(Datos))
#------------------------------------------------------------------------------------------

@app.route('/Video', methods=['POST'])
def video():
    global Video
    URL = request.json['url']
    fecha = request.json['date']
    categoria = request.json['category']
    author = request.json['author']

    NuevoObjet1 = posts(URL,fecha,categoria,author)
    Video.append(NuevoObjet1)

    return jsonify({'Mensaje45':'Post Realizado',})
 
#-----------------------------------------------POST Imagen----------------------------------
@app.route('/Imagen', methods=['POST'])
def imagen():
    global Imagen
    URL = request.json['url']
    fecha = request.json['date']
    categoria = request.json['category']
    author = request.json['author']

    NuevoObjetI = posts(URL,fecha,categoria,author)
    Imagen.append(NuevoObjetI)

    return jsonify({'Mensaje45':'Post Realizado',})


@app.route('/Imagen', methods=['GET'])
def getimagen():
    global Imagen
    Datos = []
    for m in Imagen:
        objeto123 = {
            'url': m.getURL(),
            'date': m.getFecha(),
            'category': m.getCategoria(),
            'author': m.getAuthor()
         
        }
        Datos.append(objeto123)  
    return(jsonify(Datos))

#---------------------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------------
@app.route('/Listado/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Listado
 
    for Users in Listado:

        if nombre == Users.getNombreUs():

            Users.setNombre(request.json['name'])
            Users.setGenero(request.json['gender'])
            Users.setNombreUsuario(request.json['username'])
            Users.setCorreo(request.json['email'])
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
            pat = re.compile(reg)
            mat = re.search(pat,request.json['password'])
            if mat:
             print("exito")
            else:
              return jsonify({'Mensaje':'Contraseña invalida ---- Debe contener minimo 8  caracteres, un numero,un simbolo,Una letra',})
            Users.setContras( request.json['password'])
            return jsonify({'Mensaje':'Usuario Actualizado exitosamente'})
        continue
    else:
     return jsonify({'Mensaje':'No se encontro ningun Usuario '})


#------------------------------------------------------------------------------------------------------------------
@app.route('/Listado/<string:nombre>', methods=['DELETE'])
def Elimina(nombre):
    global Listado
    global Imagen
    global Video

    for i in range(len(Listado)):
        if nombre =="Abner Cardona":
            return jsonify({'Mensaje':'El usuario admin no puede ser eliminado'}) 
        else:
         if nombre == Listado[i].getNombreUs():
            del Listado[i]    
         for x in range(len(Imagen)):
            if nombre == Imagen[x].getAuthor():
             del Imagen[x]
         for s in range(len(Video)):
           if nombre == Video[s].getAuthor():
             del Video[s]
               
    return jsonify({'Mensaje':'Usuario eliminado'})





#-------------------------------------------------CARGA MASIVA---------------------------------------------------

@app.route('/CargarUsuarios', methods=['POST'])
def CargarUsers():
  global Listado
  global file
  file = request.json['CargarUs']
  load = json.loads(file)

  for leer1 in load:

      NuevoObjet = Users(leer1['name'], leer1['gender'],leer1['username'],leer1['email'],leer1['password'])
      Listado.append(NuevoObjet)

  return jsonify({'Mensaje':'Post Realizado',})



@app.route('/CargarPost', methods=['POST'])
def CargarPost():
  global Video
  global Imagen
  global file

  file = request.json['CargarPOST']
  load = json.loads(file)

  for leerImagen in load['images']:

       NuevoObjet123 = posts(leerImagen['url'],leerImagen['date'],leerImagen['category'],leerImagen['author'])
       Imagen.append(NuevoObjet123)

       

  for leerVideo in load['videos']:

       NuevoObjet123 = posts(leerVideo['url'],leerVideo['date'],leerVideo['category'],leerVideo['author'])
       Video.append(NuevoObjet123)


  return jsonify({'Mensaje':'Post Realizado',})


#----------------------------------------------------------------------------------------

 




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)





