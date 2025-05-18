# Desafio_Introduccion_Python
Desafío evaluado - Introducción a Python

# Desafío - Introducción a Python

## Actividad 1: Velocidad de Escape

**Descripción:**  
La velocidad de escape de un planeta es la mínima velocidad necesaria para vencer la gravedad y salir del planeta.

**Fórmula:**  
`Ve = √(2*g*r)`  
Donde:  
- `Ve`: Velocidad de Escape [m/s]  
- `g`: Constante gravitacional [m/s²]  
- `r`: Radio del planeta [m]  

**Requerimientos:**  
1. Crear script `escape.py` que:  
   - Solicite mediante `input()`:  
     ```python
     "Ingrese el radio en Kilómetros:"
     "Ingrese la constante g:"
     ```  
   - Muestre el resultado como:  
     ```python
     "La velocidad de Escape es 11174.6 [m/s]"
     ```  

**Ejemplo de validación:**  
- Entrada:  
  `g = 9.8 [m/s²]`, `r = 6371 [Km]`  
- Salida:  
  `Velocidad de Escape = 11174.6 [m/s]`  

---
Actividad 2 - Rentabilidad

Un emprendedor quiere crear una app que provea un servicio de entrega de comida para mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántosusuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidadesdel proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 \* 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

Para ello, se te pide desarrollar este cálculo en tres versiones.

1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar como dato el precio de suscripción P , el número de usuarios U y el gasto total GT.

2. Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,los usuarios normales y los usuarios premium a los cuales se les cobrará una suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que permita considerar el caso recién expuesto. Para ello modifica la fórmula de utilidades en la cual se solicite mediante input() los parámetros de entrada precios de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT .

3. Considera ahora una tercera versión llamada emprendedor3.py. Necesitarás la fórmula original de utilidades

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 \* 𝑈 – 𝐺𝑇

Ahora, debes crear una nueva función en la que se pida (por medio de input()) los

siguientes datos:
● precio de suscripción P
● número de usuarios normales U
● gastos GT
● utilidades del año anterior Uanterior

El programa debe calcular las utilidades actuales Uactuales y mostrar la razón entre las utilidades actuales y las del año anterior

𝑅𝑎𝑧ó𝑛 = 𝑈𝑎𝑛𝑡𝑒𝑟𝑖𝑜𝑟

El resultado debe estar redondeado a dos decimales.

Nota: Dentro de las instrucciones del programa advierte al usuario de

valores que podrían impedir un buen funcionamiento de éste
