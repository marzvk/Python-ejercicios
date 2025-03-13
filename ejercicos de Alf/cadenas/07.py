email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es') # : es el inicio del correo hasta que llega a @
                                    # .find() busca una caracter en el string
