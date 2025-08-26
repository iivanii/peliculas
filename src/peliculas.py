import csv
from typing import NamedTuple
from datetime import datetime
from datetime import date
from typing import List
from parsers import parsea_str_list


Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos", list[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", list[str])
    ]
)

def lee_peliculas(ruta):
    peliculas=[]
    with open(ruta, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno=datetime.strptime(fecha_estreno, '%d/%m/%Y').date()
            titulo=str(titulo)
            director=str(director)
            generos=parsea_str_list(generos)
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto=parsea_str_list(reparto)
            pelicula=Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            peliculas.append(pelicula)
        return peliculas
    
def pelicula_mas_ganacias(registro: List[Pelicula], generos:str= None):
    if generos != None:
        generos.strip
        generos_list=generos.split(',')
    pelis=[]
    for r in registro:
        ganancias=r.recaudacion - r.presupuesto
        titulo_ganacias=(r.titulo, ganancias)
        if generos == None:
            pelis.append(titulo_ganacias)
        else:
            for g in r.generos:
                if g in generos_list:
                    pelis.append(titulo_ganacias)


    pelis.sort(key=lambda x:x[1], reverse= True)

    return pelis[0]

from statistics import mean

def media_presupuesto_por_genero(registro):
    generos=[]
    res={}
    for r in registro:
        for g in r.generos:
            if g not in generos:
                generos.append(g)
                res[g] = [r.presupuesto]
            else:
                # for d in res:
                #     if d == g:
                        res[g].append(r.presupuesto)
    
    for e in res:
        res[e] = mean(res[e])

    return res


#4

def peliculas_por_actor(registro:List[Pelicula], año_inicial=None, año_final=None):
    actores=[]
    res={}
    for r in registro:
        if año_final == None or año_final == None:
            for a in r.reparto:
                if a not in actores:
                    actores.append(a)
                    res[a] = 1
                else:
                    res[a]+=1
        elif año_inicial <= r.fecha_estreno.year and año_final>=r.fecha_estreno.year:
            for a in r.reparto:
                if a not in actores:
                    actores.append(a)
                    res[a] = 1
                else:
                    res[a]+=1
            
    return res


#5

def actores_mas_frecuentes(registro,n, año_inicial=None,año_final=None):
    res=peliculas_por_actor(registro,año_inicial, año_final)
    res_sort=sorted(res.items(),key=lambda x:x[1], reverse=True)
    sol=res_sort[:n]
    sol.sort(key=lambda x:x[0])
    solfix=[]
    for s in sol:
        solfix.append(s[0])
    return solfix

#6

def recaudacion_total_por_año(registro: List[Pelicula], generos:str=None):
    

    res={}

    años=[]

    for r in registro:

        if generos == None:
            if r.fecha_estreno.year not in años:
                años.append(r.fecha_estreno.year)
                res[r.fecha_estreno.year] = r.recaudacion

            else:
                res[r.fecha_estreno.year] += r.recaudacion

        elif len(generos.intersection(set(r.generos))) >0:
            if r.fecha_estreno.year not in años:
                años.append(r.fecha_estreno.year)
                res[r.fecha_estreno.year] = r.recaudacion

            else:
                res[r.fecha_estreno.year] += r.recaudacion

    return res


#7

def incrementos_recaudacion_por_año(registro:List[Pelicula],generos:set= None):
    res=[]
    recaudacion_por_año=recaudacion_total_por_año(registro, generos)
    
    recaudacion_por_año_list=sorted(recaudacion_por_año.items(),key=lambda x:int(x[0]))

    list_fix=[]

    for e in recaudacion_por_año_list:
        list_fix.append(e[1])

    for i in range(1,len(list_fix)):
        if generos == None:
            diff=list_fix[i] -list_fix[i-1]
            res.append(diff)
        else:
            diff=list_fix[i] - list_fix[i-1]
            res.append(diff)
            
    return res


