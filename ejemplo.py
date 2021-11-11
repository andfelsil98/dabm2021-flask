from flask import Flask,render_template,request
import os 
import random

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
    lectura = random.randint(0,45)
    #enviar a la interfaz
    color = 0
    if lectura >= int(datos[0][1]) and lectura <= int(datos[0][2]):
        color = 1
    if lectura >= int(datos[1][1]) and lectura <= int(datos[1][2]):
        color = 2
    if lectura >= int(datos[2][1]) and lectura <= int(datos[2][2]):
        color = 3
    return render_template('monitor.html', datos = datos, lectura = lectura, color=color)

@app.route('/config', methods=['GET','POST'])
def config():  ##recibo los elementos que me envia el submit config 
    if request.method == "POST":
        min_hipo = request.form['minHipo'] 
        max_hipo = request.form['maxHipo']
        min_norm = request.form['minNorm']
        max_norm = request.form['maxNorm']
        min_fie = request.form['minFie']
        max_fie = request.form['maxFie']
        print(min_hipo,max_hipo,min_norm,max_norm,min_fie,max_fie)
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