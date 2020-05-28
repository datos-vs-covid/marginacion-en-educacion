import requests
import csv
import time
from datetime import datetime
import unicodedata
import os.path
from os import path


def get_entidad(session,i):
    url = "http://www.mejoratuescuela.org/api/localidades"
    options = {"entidad":i}
    try:
        entidad_page = session.post(url,options).json()        
        
        for element in entidad_page:
            entidad_dict = element['entidad']
            entidad = entidad_dict['nombre'].upper()
            entidad = entidad.replace(" ","_")        
            entidad = unicodedata.normalize("NFKD", entidad).encode("ascii","ignore").decode("ascii")
            break    
        
        return entidad
    except:
        print ("No hay valores para la entidad %i" %(i))
        if i == 7 :
            entidad = 'CHIAPAS' #la pagina tiene un error con este estado
            return entidad

def get_page(session,url,options):    
    page = session.post(url,options).json()
    return page   

def get_num_pages(session,url,options):
    first_page = get_page(session,url,options)
    pagination = first_page['pagination']
    num_pages =  pagination['document_pages']
    return num_pages

def get_escuela_fields(page):
    escuelas_list = []    
    # Leer la lista "escuelas". Es una lista de diccionarios
    escuelas = page['escuelas']  
    
    # Iterar en la lista y leer cada diccionario
    for count, escuela in enumerate(escuelas):
        campos_escuela = []

        cct = escuela['cct']
        latitud = float(escuela['latitud'])
        longitud = (lambda x: float(x)*-1 if float(x) > 0 else x) (escuela['longitud'])
        #longitud = lambda_longitud(escuela['longitud'])
        nombre = escuela['nombre']
        localidad = escuela['localidad']
        entidad = escuela['entidad']
        nivel = escuela['nivel']
        control = escuela['control']
        planea_semaforo = escuela['planea_semaforo']
        planea_year = escuela['planea_year']
        planea_rank_entidad = escuela['planea_rank_entidad']

        matematicas_insuficiente_escuela = escuela['planea_matematicas_charts'][1][1]   
        matematicas_insuficiente_entidad = escuela['planea_matematicas_charts'][1][3]
        matematicas_insuficiente_nacional = escuela['planea_matematicas_charts'][1][4]   
        matematicas_indispensable_escuela = escuela['planea_matematicas_charts'][2][1]   
        matematicas_indispensable_entidad = escuela['planea_matematicas_charts'][2][3]
        matematicas_indispensable_nacional = escuela['planea_matematicas_charts'][2][4]   
        matematicas_satisfactorio_escuela = escuela['planea_matematicas_charts'][3][1]   
        matematicas_satisfactorio_entidad = escuela['planea_matematicas_charts'][3][3]
        matematicas_satisfactorio_nacional = escuela['planea_matematicas_charts'][3][4]   
        matematicas_sobresalientes_escuela = escuela['planea_matematicas_charts'][4][1]   
        matematicas_sobresalientes_entidad = escuela['planea_matematicas_charts'][4][3]
        matematicas_sobresalientes_nacional = escuela['planea_matematicas_charts'][4][4]   

        espaniol_insuficiente_escuela = escuela['planea_espaniol_charts'][1][1]   
        espaniol_insuficiente_entidad = escuela['planea_espaniol_charts'][1][3]
        espaniol_insuficiente_nacional = escuela['planea_espaniol_charts'][1][4]   
        espaniol_indispensable_escuela = escuela['planea_espaniol_charts'][2][1]   
        espaniol_indispensable_entidad = escuela['planea_espaniol_charts'][2][3]
        espaniol_indispensable_nacional = escuela['planea_espaniol_charts'][2][4]   
        espaniol_satisfactorio_escuela = escuela['planea_espaniol_charts'][3][1]   
        espaniol_satisfactorio_entidad = escuela['planea_espaniol_charts'][3][3]
        espaniol_satisfactorio_nacional = escuela['planea_espaniol_charts'][3][4]   
        espaniol_sobresalientes_escuela = escuela['planea_espaniol_charts'][4][1]   
        espaniol_sobresalientes_entidad = escuela['planea_espaniol_charts'][4][3]
        espaniol_sobresalientes_nacional = escuela['planea_espaniol_charts'][4][4]   

        
        planea_evaluados = escuela['planea_evaluados']
        promedio_general = escuela['promedio_general']
        promedio_matematicas = escuela['promedio_matematicas']
        promedio_espaniol = escuela['promedio_espaniol']
        rank = escuela['rank']
        rank_nacional = escuela['rank_nacional']
        direccion = escuela['direccion']
        poco_confiables = escuela['poco_confiables']
        domicilio = escuela['domicilio']


        # Agragar campos a la lista
        campos_escuela.append(cct)
        campos_escuela.append(latitud)
        campos_escuela.append(longitud)
        campos_escuela.append(nombre)
        campos_escuela.append(localidad)
        campos_escuela.append(entidad)
        campos_escuela.append(nivel)
        campos_escuela.append(control)
        campos_escuela.append(planea_semaforo)
        campos_escuela.append(planea_year)
        campos_escuela.append(planea_rank_entidad)
        campos_escuela.append(matematicas_insuficiente_escuela)
        campos_escuela.append(matematicas_insuficiente_entidad)
        campos_escuela.append(matematicas_insuficiente_nacional)
        campos_escuela.append(matematicas_indispensable_escuela)
        campos_escuela.append(matematicas_indispensable_entidad)
        campos_escuela.append(matematicas_indispensable_nacional)
        campos_escuela.append(matematicas_satisfactorio_escuela)
        campos_escuela.append(matematicas_satisfactorio_entidad)
        campos_escuela.append(matematicas_satisfactorio_nacional)
        campos_escuela.append(matematicas_sobresalientes_escuela)
        campos_escuela.append(matematicas_sobresalientes_entidad)
        campos_escuela.append(matematicas_sobresalientes_nacional)

        campos_escuela.append(espaniol_insuficiente_escuela)
        campos_escuela.append(espaniol_insuficiente_entidad)
        campos_escuela.append(espaniol_insuficiente_nacional)
        campos_escuela.append(espaniol_indispensable_escuela)
        campos_escuela.append(espaniol_indispensable_entidad)
        campos_escuela.append(espaniol_indispensable_nacional)
        campos_escuela.append(espaniol_satisfactorio_escuela)
        campos_escuela.append(espaniol_satisfactorio_entidad)
        campos_escuela.append(espaniol_satisfactorio_nacional)
        campos_escuela.append(espaniol_sobresalientes_escuela)
        campos_escuela.append(espaniol_sobresalientes_entidad)
        campos_escuela.append(espaniol_sobresalientes_nacional)        

        campos_escuela.append(planea_evaluados)
        campos_escuela.append(promedio_general)
        campos_escuela.append(promedio_matematicas)
        campos_escuela.append(promedio_espaniol)
        campos_escuela.append(rank)
        campos_escuela.append(rank_nacional)
        campos_escuela.append(direccion)
        campos_escuela.append(poco_confiables)
        campos_escuela.append(domicilio)
        
        escuelas_list.append(campos_escuela)        

    return escuelas_list

def archivo_existe(entidad):
    if not entidad:
        entidad="Desconocido"
    
    folder = "../../datos/crudos/planea/"
    filename=folder+entidad+'_planea_resultados_escuela.csv'

    if path.exists(filename):
        return True
    else:
        return False
   

def generar_archivo(entidad,global_list):

    if not entidad:
        entidad="Desconocido"

    path = "../../datos/crudos/planea/"
    filename=path+entidad+'_planea_resultados_escuela.csv'
    print(filename)

    
    with open(filename, 'w', newline='',encoding='utf-8') as file:
        headers = ['cct', 'latitud', 'longitud', 'nombre', 'localidad', 'entidad', 'nivel', 'control', 
                    'planea_semaforo', 'planea_year', 'planea_rank_entidad', 'matematicas_insuficiente_escuela', 
                    'matematicas_insuficiente_entidad', 'matematicas_insuficiente_nacional', 
                    'matematicas_indispensable_escuela', 'matematicas_indispensable_entidad', 
                    'matematicas_indispensable_nacional', 'matematicas_satisfactorio_escuela', 
                    'matematicas_satisfactorio_entidad', 'matematicas_satisfactorio_nacional', 
                    'matematicas_sobresalientes_escuela', 'matematicas_sobresalientes_entidad',
                    'matematicas_sobresalientes_nacional','espaniol_insuficiente_escuela','espaniol_insuficiente_entidad',
                    'espaniol_insuficiente_nacional','espaniol_indispensable_escuela','espaniol_indispensable_entidad',
                    'espaniol_indispensable_nacional','espaniol_satisfactorio_escuela','espaniol_satisfactorio_entidad',
                    'espaniol_satisfactorio_nacional','espaniol_sobresalientes_escuela','espaniol_sobresalientes_entidad',
                    'espaniol_sobresalientes_nacional','planea_evaluados','promedio_general','promedio_matematicas',
                    'promedio_espaniol','rank','rank_nacional','direccion','poco_confiables','domicilio']
        writer = csv.writer(file,delimiter=';',quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(headers)
        writer.writerows(global_list)


def get_entidad_datos(session,entidad,i):
    entidad_list = []    
    url = "http://www.mejoratuescuela.org/api/escuelas" 
    options = {"entidad":i,"p":1,"sort":"Semáforo de Resultados Educativos","type_test":"planea","schoolStatus":1,"niveles":"12,13","pagination": "80"}
    num_pages = get_num_pages(session,url,options)

    print ("El numero de paginas para la entidad %s a revisar es %i" % (entidad,num_pages) )

    for num_page in range (1, num_pages+1):
    #for num_page in range (200, 201):    
        time.sleep(2)
        try:            
            options = {"entidad":i,"p":num_page,"sort":"Semáforo de Resultados Educativos","type_test":"planea","schoolStatus":1,"niveles":"12,13","pagination": "80"}
            #print ("Procesando página " + str(num_page))
            page = get_page(session,url,options)

            for row in get_escuela_fields(page):
                entidad_list.append(row)                                                

        except Exception as identifier:
            dateTimeObj = datetime.now()
            print ("%s : Error en página %i de %i para la entidad %s" %(dateTimeObj,num_page,num_pages,entidad) )  
            print(identifier)
            page = get_page(session,url,options)
            #break
        finally:
            dateTimeObj = datetime.now()
            print ("%s : Finalizando página %i de %i para la entidad %s" %(dateTimeObj,num_page,num_pages,entidad) ) 
    return entidad_list

    

def main():
    session = requests.Session()
    
    #for i in range (1,33):
    lista_entidades=[15,30]
    for i in lista_entidades:
        entidad = get_entidad(session,i)
        print ("Entidad a procesar: %i %s" %(i,entidad))
        if archivo_existe(entidad):
            print ("El archivo para la entidad %s ya existe" %(entidad))
        else:
            entidad_datos = get_entidad_datos(session,entidad,i)
            generar_archivo(entidad,entidad_datos)   
            # si corres el script local va a generar los archivos
            # pero estos no se guardan en el repo
            # Por favor revisa el Readme de la carpeta
            # /datos/crudos/planea de este repositorio

    
        

if __name__ == "__main__":
    main()






