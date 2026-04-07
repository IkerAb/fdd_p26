from .Operaciones_basicas import suma, conteo
from .Estadistica_descriptiva import desviacion_estandar, media
from .utils import valida_1, valida_2

def covarianza(x, y):
    valida_2(x, y)
    
    n = conteo(x)
    
    if n < 2:
        raise ValueError("Se requieren al menos 2 datos")
    
    mx = media(x)
    my = media(y)
    
    return suma((xi - mx)*(yi - my) for xi, yi in zip(x, y)) / (n - 1)

def correlacion(x,y): 
    valida_2(x,y)
    return covarianza(x,y)/desviacion_estandar(x)* desviacion_estandar(y)

def normalizar(data): 
    valida_1(data)
    m = media(data)
    o = desviacion_estandar(data)

    if o == 0: 
        raise ValueError("No se puede normalizar si la desviacion estandar es 0")

    return [ (x - m) / o for x in data]
    