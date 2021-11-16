from flask import Flask,render_template,request
import os 
import random


#################################################funciones#################################
class temperatura:
    def __init__(self,condicion,minimo,maximo):
        self.condicion = condicion
        self.minimo = int(minimo)
        self.maximo = int(maximo)
        self._file = ruta
    
    # def save_to_file(self):
        
    #     file = open(self._file,'a')
    #     datos = self.condicion + ';' + str(self.minimo) + ';' + str(self.maximo) + '\n'  
    #     file.write(datos)
    #     # print(datos)
    #     file.close()
    #     # datos_arduino()
        

def mod_info():
    global ruta
    directory = os.path.dirname(__file__)
    nombre_archivo = 'C:/Users/Administrador/Desktop/DABM PYTHONv2/flask/bd/parametros.csv'
    ruta = os.path.join(directory, nombre_archivo)
    

    f = open(ruta,'r')
    datos_mod = f.readlines()
    

    for d in datos_mod:
        # print(d)
        if name_range in d:
            # print(d)
            datos_mod.remove(d)
                
        
    datos_mod.append(name_range + ';' + str(minimo) + ';' + str(maximo) + '\n')
    # file_sensores = 'C:/Users/Administrador/Desktop/DABM PYTHONv2/flask/bd/parametros.csv'
    archivo = open(ruta,'w')
    archivo.writelines(datos_mod)
    archivo.close()
    # input('Cambios guardados exitosamente')
    # datos_arduino()
    

##############################################################################################

app = Flask(__name__)

@app.route('/')  ##le estoy diciendo a flask cuando el usuario entre a esta ruta ejecuta esta funcion
def inicio():
    return render_template('login.html')

@app.route('/datos')
def datos():
    user = {'nombre' : 'david'}
    return render_template('datos.html',title='Titulo personalizado', user = user)

@app.route('/validar', methods = ["POST"])   ###metodo get en la etiqueta form de html me sirve para capturar los datos y poder visualizarlos en el url, con el metodo post puedo guardar esos datos pero no visualizarlos en el url para mayor seguridad
def validar(): ##MENSAJE QUE SE ENVIA al servidor para verificar informacion que captura se llama request
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']
        resultado = verificar(usuario,password)
        
        # return resultado
        return render_template('menu.html', title = 'Sistema DABM')

@app.route('/monitor')
def monitor():
    #consultar archivo de parametros
    datos = get_datos()
    #print(datos)
    #obtener lectura
    lecturas = []
    for i in range(100):
        lectura = random.randint(0,45)
        lecturas.append(lectura)
    #enviar a la interfaz
    colores = []
    for lectura in lecturas:
        color = 0
        if lectura >= int(datos[0][1]) and lectura <= int(datos[0][2]):
            color = 1
        if lectura >= int(datos[1][1]) and lectura <= int(datos[1][2]):
            color = 2
        if lectura >= int(datos[2][1]) and lectura <= int(datos[2][2]):
            color = 3
        colores.append(color)
    return render_template('monitor2.html', datos = datos, lecturas = lecturas, colores=colores)

@app.route('/config', methods=['GET','POST'])
def config():  ##recibo los elementos que me envia el submit config 
    global minimo
    global maximo
    global t
    global name_range
    if request.method == "POST":
        minimo= request.form['minHipo'] 
        maximo = request.form['maxHipo']
        name_range = 'hipotermia'
        t = temperatura(name_range,minimo,maximo)
        mod_info()
        minimo = request.form['minNorm']
        maximo = request.form['maxNorm']
        name_range = 'normal'
        t = temperatura(name_range,minimo,maximo)
        mod_info()
        minimo = request.form['minFie']
        maximo = request.form['maxFie']
        name_range = 'fiebre'
        t = temperatura(name_range,minimo,maximo)
        mod_info()

        
    return render_template('config.html')

def get_datos():
    directorio = os.path.dirname(__file__)
    nombre_archivo = 'bd/parametros.csv'
    ruta = os.path.join(directorio, nombre_archivo)
    f = open(ruta,'r')
    lineas = f.readlines()
    f.close()

    datos = []

    for l in lineas:
        l = l.replace('\n','')
        l = l.split(';')
        datos.append(l)
    return datos

def verificar(usuario,password):
    # file = open('C:/Users/Administrador/Desktop/DABM PYTHONv2/flask/bd/users.csv','r')
    # datos = file.readlines()
    # file.close()
    # for dato in datos:
    #     dato = dato.replace('\n','')
    #     us,contra = dato.split(';')
        
    #     if us == usuario and contra == password:
    #         return 'Usuario autenticado exitosamente'
    #     else:
    #         print(usuario,password)
    #         return 'Usuario no registrado'
    return True


if __name__ == '__main__':
    app.run(debug=True) 
    # validar()