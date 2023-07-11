from app_revistas.config.mysqlconnection import connectToMySQL
from app_revistas import BASE_DATOS
from app_revistas.modelos.modelo_usuarios import Usuario
from flask import flash 

class Revista:
    def __init__(self, data) :
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']        
        self.id_usuario = data['id_usuario']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuario = None
        
    @classmethod
    def crear_uno(cls, data):
        query = """
                INSERT INTO revistas (titulo, descripcion, id_usuario)
                VALUES ( %(titulo)s, %(descripcion)s, %(id_usuario)s)
                """
        id_revista = connectToMySQL (BASE_DATOS).query_db (query, data)
        return id_revista
    
    @staticmethod
    def validar_formulario_revistas (data):
        es_valido = True
        if len(data ['titulo']) < 3:
            es_valido = False
            flash("Debes proporcionar el titulo de la revista.", "error_titulo")
        if len(data ['descripcion']) < 3:
            es_valido = False
            flash("Debes proporcionar la descripcion de la revista.", "error_descripcion")
        return es_valido
            
    @classmethod
    def obtener_todas_con_usuarios (cls):
        query = """
                SELECT *
                FROM revistas r JOIN usuarios u
                ON  r.id_usuario = u.id                
                """
        resultado = connectToMySQL (BASE_DATOS).query_db (query)
        lista_revista = []
        for renglon in resultado:
            revista = Revista (renglon)
            data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['nombre'],
                "apellido" :renglon ['apellido'],
                "email" :renglon ['email'],
                "contraseña" :renglon ['contraseña'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
            usuario = Usuario (data_usuario)
            revista.usuario = usuario
            lista_revista.append(revista)
        
        return lista_revista
            
    @classmethod
    def elimina_uno (cls, data):
        query = """
                DELETE FROM revistas
                WHERE id = %(id)s ;              
                """
        return connectToMySQL(BASE_DATOS).query_db(query, data)
    
    @classmethod
    def obtener_uno_con_usuario (cls, data):
        query = """
                SELECT *
                FROM revistas r JOIN usuarios u
                ON  r.id_usuario = u.id  
                WHERE r.id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DATOS).query_db (query, data)
        renglon = resultado [0]
        revista = Revista (renglon)
        data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['nombre'],
                "apellido" :renglon ['apellido'],
                "email" :renglon ['email'],
                "contraseña" :renglon ['contraseña'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
        revista.usuario = Usuario (data_usuario)
        return revista
    
    
    @classmethod
    def obtener_uno (cls, data):
        query = """
                SELECT *
                FROM revistas  
                WHERE id= %(id)s;             
                """
        resultado = connectToMySQL(BASE_DATOS).query_db( query, data)
        revista = Revista (resultado [0])
        return revista
    
    @classmethod
    def elimina_uno (cls, data):
        query = """
                DELETE FROM revistas
                WHERE id = %(id)s ;              
                """
        return connectToMySQL(BASE_DATOS).query_db(query, data)
    
                
    @classmethod
    def obtener_todas_con_revistas (cls, data):
        query = """
                SELECT *
                FROM revistas r JOIN usuarios u
                ON  r.id_usuario = u.id 
                WHERE u.id = %(id)s               
                """
        resultado = connectToMySQL (BASE_DATOS).query_db (query, data)
        lista_revista = []
        for renglon in resultado:
            revista = Revista (renglon)
            data_usuario = {
                "id" : renglon ['u.id'],
                "nombre" : renglon ['nombre'],
                "apellido" :renglon ['apellido'],
                "email" :renglon ['email'],
                "contraseña" :renglon ['contraseña'],
                "fecha_creacion" :renglon ['u.fecha_creacion'],
                "fecha_actualizacion" :renglon ['u.fecha_actualizacion'],                    
            }
            usuario = Usuario (data_usuario)
            revista.usuario = usuario
            lista_revista.append(revista)
        
        return lista_revista
    