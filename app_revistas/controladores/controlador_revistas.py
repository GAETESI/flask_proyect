from flask import render_template, redirect, request, session
from app_revistas.modelos.modelo_revistas import Revista
from app_revistas.modelos.modelo_usuarios import Usuario
from app_revistas import app

@app.route ('/revistas', methods = ['GET'])
def desplegar_revistas():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        lista_revista = Revista.obtener_todas_con_usuarios()
        print (lista_revista)
        return render_template ('/revistas.html', lista_revista = lista_revista, id_usuario =session["id_usuario"]  )
    

@app.route ('/formulario/revista', methods =['GET'])
def desplegar_formulario_revista():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        return render_template ('formulario_revista.html')

@app.route ('/crear/revista', methods =['POST'])
def nueva_revista():
    data = {
        **request.form,
        "id_usuario" : session['id_usuario']
    }
    if Revista.validar_formulario_revistas ( data) == False:
        return redirect('/formulario/revista')
    else:
        id_revista = Revista.crear_uno ( data )
        return redirect('/revistas')
    
@app.route ('/eliminar/revista/<int:id>', methods = ['POST'])
def eliminar_revista (id):
    data = {
        "id" : id
    }
    Revista.elimina_uno (data)
    return redirect ('/revistas')

@app.route('/revista/<int:id>', methods =['GET'])
def desplegar_revista(id):
    if "id_usuario" not in session:
        return redirect('/')
    else:
        data ={
            "id" : id
        }
        revista = Revista.obtener_uno_con_usuario(data)
        return render_template('revista.html', revista = revista, id_usuario = session['id_usuario'])
    
    
@app.route ('/eliminar/revista/<int:id>', methods = ['POST'])
def eliminar_receta (id):
    data = {
        "id" : id
    }
    Revista.elimina_uno (data)
    return redirect ('/revistas')


@app.route('/formulario/editar/usuario/<int:id>', methods =['GET'])
def desplegar_editar_usuario(id):
    if "id_usuario" not in session:
        return redirect('/')
    else:
        data ={
            "id" : id
        }
        usuario = Usuario.obtener_usuario(data)
        lista_revista = Revista.obtener_todas_con_revistas( data)
        return render_template('editar_usuario.html', usuario = usuario, lista_revista = lista_revista )

@app.route('/editar/usuario/<int:id>', methods =['POST'])
def editar_usuario(id):
    if Usuario.validar_registro (request.form) == False:
        return redirect ( f'/formulario/editar/usuario/{id}' )
    else:
        data = {
            **request.form,
            "id" : id
        }
        Usuario.editar_uno (data)
        return redirect ('/revistas')






    
    
    
