def parsea_str_list(cadena:str):
    cadena=cadena.strip()
    cadena_pars=cadena.split(',')
    cadena_fix=[]
    for c in cadena_pars:
        c_fix=c.strip()
        cadena_fix.append(c_fix)

    return cadena_fix

