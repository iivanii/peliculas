from peliculas import *

ruta='C:\\Users\\ivanb\\Desktop\\myp\\LAB-Peliculas-main\\data\\peliculas.csv'
registro= lee_peliculas(ruta)
def test_lee_peliculas():
    registro= lee_peliculas(ruta)
    print(' ')
    print(f'Total registros leidos: {len(registro)}')
    print(f'Mostrando los tres primeros registros:')
    for i in range(3):
        print(registro[i])

def test_peliculas_mas_ganancias():
    res=pelicula_mas_ganacias(registro, 'Drama')
    print(res)

def test_media_presupuesto_por_genero():
    sol=media_presupuesto_por_genero(registro)
    print(sol)

def test_peliculas_por_actor():
    sol=peliculas_por_actor(registro, 2010, 2020)
    print(sol)

def test_actores_mas_frecuentes():
    sol=actores_mas_frecuentes(registro,3, 2005, 2015)
    print(sol)

def test_recaudacion_total_por_año():
    sol=recaudacion_total_por_año(registro)
    print(sol)

def test_incrementos_recaudacion_por_año():
    sol=incrementos_recaudacion_por_año(registro,{'Drama', 'Acción'} )
    print(sol)

if __name__ == '__main__':
    #test_lee_peliculas()
    #test_peliculas_mas_ganancias()
    #test_media_presupuesto_por_genero()
    #test_peliculas_por_actor()
    #test_actores_mas_frecuentes()
    #test_recaudacion_total_por_año()
    test_incrementos_recaudacion_por_año()