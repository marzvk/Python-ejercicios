def fun1():
    print('hola amiga')
    return


def fun_2(param):
    print('Hola' + param)
    return


def fun_3(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def fun_4(valor, iva=0.21):
    total = valor + (valor * iva)
    return total


def area_circ(radio):
    area = 3.14 * (radio**2)
    return area


def vol_cilin(radio, altura):
    vol = area_circ(radio) * altura
    return vol


# print(vol_cilin(4,7))


def media(param):
    sum = 0
    for i in param:
        sum += i
    media = sum / len(param)
    return media


lista = [3, 5, 8, 7, 3, 6, 4]

# print(media(list))


def cuadrados(param):
    cuad = []
    for i in param:
        cuad.append(i**2)
    return cuad


# print(cuadrados(list))


def varianza(param):
    mid = media(param)
    sumatoria = 0
    for i in param:
        sumatoria = sumatoria + (i - mid)**2
    var = sumatoria / len(param)
    return var


def desviacion_std(param):
    wed = varianza(param)
    return wed**0.5


def dicc_compl(param):
    dic = dict()
    dic = dic.fromkeys(['media', 'varianza', 'desviacion std'])
    dic['media'] = media(param)
    dic['varianza'] = varianza(param)
    dic['desviacion std'] = desviacion_std(param)
    return dic


# print(dicc_compl(lista))

cadecar = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'


def cadena(param):
    lulo = param.split(" ")
    dic = dict()
    lulo_set = set(lulo)

    for i in lulo_set:
        dic[i] = lulo.count(i)
    return dic


def max_elem_dic(dic):
    ftr = sorted(dic.items(), key=lambda a: a[1], reverse=True)
    return ftr[0]


print(max_elem_dic(cadena(cadecar)))
