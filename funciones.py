# La función se llama “dibujo”, dibuja un rectángulo y las variables (parámetros) que solicita son el ancho y el alto de la figura 
def dibujo(width, height): 
   # se utiliza una estructura de control. 
   if width < 10 or height < 10: 
      print("Error: La figura es muy pequeña o muy grande.") 
      quit() 
   # Dibuja la parte superior de la figura 
   print("*" * width) 
   # Dibuja los lados, en este caso se utiliza un bucle para el valor del alto de la figura 
   for i in range(height - 2): 
      print("*" + " " * (width - 2) + "*") 
   # Dibuja la parte inferior 
   print("*" * width)

# Función de una sucesión geométrica 
def sumGeometric(a, r, n): 
   # Si el radio tiene un valor de uno 
   if r == 1: 
      return a * n 
   # Calcula la suma geométrica cuando el radio es diferente de uno 
   s = a * (1 - r ** n) / (1 - r) 
   #regresa el valor de s 
   return s
print(sumGeometric(1,2,3))
