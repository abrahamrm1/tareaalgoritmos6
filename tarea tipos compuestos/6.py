#Este método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.

>>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
>>> print versiones_plone.index(4)
3
#El método admite como argumento adicional un índice inicial a partir de donde comenzar la búsqueda, opcionalmente también el índice final.

>>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
>>> versiones_plone[2]
3.6
>>> print versiones_plone.index(4, 2)
3
>>> versiones_plone[3]
4
>>> print versiones_plone.index(4, 5)
6
>>> versiones_plone[6]
4
#El método devuelve un excepción ValueError si el elemento no se encuentra en la lista, o en el entorno definido.

>>> versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6, 4]
>>> print versiones_plone.index(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 9 is not in list
