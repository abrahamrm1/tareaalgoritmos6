Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> index()
... #Comparte el mismo método index() del tipo lista. Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la tupla.
... 
... >>> valores = ("Python", True, "Zope", 5)
... >>> print valores.index(True)
... 1
... >>> print valores.index(5)
... 3
... #El método devuelve un excepción ValueError si el elemento no se encuentra en la tupla, o en el entorno definido.
... 
... >>> valores = ("Python", True, "Zope", 5)
... >>> print valores.index(4)
... Traceback (most recent call last):
...   File "<stdin>", line 1, in <module>
