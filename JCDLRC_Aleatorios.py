
"""

Juan Camilo De Los Ríos 

GENERACIÓN DE NÚMEROS ALEATORIOS:

    Clase Aleat() ----> implementa el generador de números aleatorios LGC.

"""

class Aleat:
    def __init__(self):
        """
            Inicializa los valores de m, a, c y la semilla.
        """
        self.m = 2**48
        self.a = 25214903917
        self.c = 11
        self.semilla = 1212121

    def __iter__(self, m, a, c, semilla):
        """
            Sobrecarga de iter para cambiar los valores m, a, c,
            y semilla opcionalmente.
        """
        self.m = m
        self.a = a
        self.c = c
        self.semilla = semilla
        return self

"""
ESTA PARTE SERÍA PARA LA FUNCIÓN QUE DEVUELVE UN NÚM. ALEATORIO ENTRE 0 Y 1 

    def __next__(self):
       
            Sobrecarga de next. Devuelve un numero aleatorio
            en el rango 0 <= Xn < 1.
        
        x = (self.a * self.semilla + self.c)
        xn = (x / self.m - x // self.m) * self.m
        self.semilla = xn
        return self.semilla / self.m
"""


    def __next__(self):
        self.semilla = (self.a * self.semilla + self.c) % self.m
        return self.semilla 



    def __call__(self, semilla):  
        self.semilla = semilla


    def aleat (m = pow(48, 2), a = 25214903917, c = 11, semilla = 1212121):
       
	"""
        OTRA ESTRUCTURA DE CÓDIGO PARA LA GENERACIÓN DE NÚMEROS ALEATORIOS 

        >>> rand = aleat(m=64, a=5, c=46, x0=36)
        >>> for _ in range(4):
        ...     print(next(rand))
        ...
        34
        24
        38
        44
        >>> rand.send(24)
        38
        >>> for _ in range(4):
        ...     print(next(rand))
        ...
        44
        10
        32
        14
        """

while True:
    semilla = (a * semilla + c) % m
    ini = (yield semilla) 
    if ini : semilla = ini
