from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')  ##le estoy diciendo a flask cuando el usuario entre a esta ruta ejecuta esta funcion
def inicio():
    return render_template('login.html')

@app.route('/datos')
def datos():
    user = {'nombre' : 'david'}
    return render_template('datos.html',title='Titulo personalizado', user = user)

@app.route('/validar', methods = ['POST'])   ###metodo get en la etiqueta form de html me sirve para capturar los datos y poder visualizarlos en el url, con el metodo post puedo guardar esos datos pero no visualizarlos en el url para mayor seguridad
def validar(): ##MENSAJE QUE SE ENVIA al servidor para verificar informacion que captura se llama request
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        resultado = verificar(usuario,password)
        # return resultado
        return render_template('menu.html', title = 'Sistema DABM')

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