
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

�
## Actividad 2 - Rentabilidad

Un emprendedor quiere crear una app que provea un servicio de entrega de comida para mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántosusuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidadesdel proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇 Donde: P: Precio de Suscripción U: Número de Usuarios GT: Gastos Totales

Para ello, se te pide desarrollar este cálculo en tres versiones.

1. Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar como dato el precio de suscripción P , el número de usuarios U y el gasto total GT.

## Versiones del Programa

### Versión 2: Usuarios Premium
#### emprendedor2.py
- **Objetivo**: Diferenciar entre usuarios normales y premium
- **Fórmula modificada**:
```python
Utilidades = (P * U_normal) + (P * 1.5 * U_premium) - GT
```
- **Inputs requeridos**:
  - P: Precio base de suscripción
  - U_normal: Cantidad usuarios normales
  - U_premium: Cantidad usuarios premium
  - GT: Gastos totales

### Versión 3: Análisis Comparativo
#### emprendedor3.py
- **Fórmula base**: `Utilidades = P * U - GT`
- **Variables requeridas**:
  | Variable | Descripción |
  |----------|-------------|
  | P | Precio suscripción |
  | U | Usuarios totales |
  | GT | Gastos totales |
  | U_anterior | Utilidades año previo |

#### Cálculo de Razón
```python
Razón = U_actuales / U_anterior  # Round(2)
```

#### ⚠️ Validaciones Importantes
1. Todos los inputs deben ser numéricos
2. U_anterior no puede ser cero
3. Valores negativos no son válidos

El resultado debe estar redondeado a dos decimales.

Nota: Dentro de las instrucciones del programa advierte al usuario de valores que podrían impedir un buen funcionamiento de éste
