# Calculadora de numeros complejos
Este programa consisite en poder calcular diferentes operaciones con numeros complejos, siendo posible realizarlas con vectores o matrices.

El programa esta dividido en dos partes, una es la libreria con todas sus funciones y una segunda parte que son todas las respectivas pruebas para cada una de las funciones.

Los numeros estan compuestos en forma de tupla **[a,b]** en donde **a** sera la parte real y **b** sera la parte imaginaria.

En el programa se podran encontrar las siguientes funciones:

### Operaciones basicas
1. **Sumar numeros complejos:**
> Dada una pareja de numeros complejos **[a,b]** y **[c,d]** la funcion retornara la suma de la pareja de numeros complejos de la forma **[e,f]**.

2. **Restar numeros complejos:**
>Dada una pareja de numeros complejos **[a,b]** y **[c,d]** la funcion retornara la resta de la pareja de numeros complejos de la forma **[e,f]**.

3. **Multiplicar:**
>Dada una pareja de numeros complejos **[a,b]** y **[c,d]** la funcion retornara la multiplicacion de la pareja de numeros complejos de la forma **[e,f]**.

4. **Dividir:**
>Dada una pareja de numeros complejos **[a,b]** y **[c,d]** la funcion retornara la divicion de la pareja de numeros complejos de la forma **[e,f]**.

5. **Modulo:**
>Dado un numero complejo **[a,b]** la funcion retornara el modulo del numero complejo de la forma **[c,d]**.

6. **Conjugado:** 
>Dado un numero complejo **[a,b]** la funcion retornara el conjugado del numero complejo de la forma **[c,d]**.

7. **Convertor de cartecianos a polares:**
>Dado un numero complejo **[a,b]** la funcion retornara las coordenadas polares del numero complejo de la forma **[c,d]**.

8. **Fase de un numero complejo:**
>Dado un numero complejo **[a,b]** la funcion retornara la fase del numero complejo de la forma **[c,d]**.

### Operacion de vectores complejos
9. **Adición de vectores complejos:**
>Dada una pareja de vectores complejos **[[a1, b1], [a2, b2], [an, bn]]** y **[[c1, d1], [c2, d2], [cn, dn]]** la funcion retornara la suma de la pareja de vectores complejos de la forma **[[e1, f1], [e2, f2], [en, fn]]**.

10. **Inverso (aditivo) de un vector complejo:**
> Dado un vector complejo **[[a1, b1], [a2, b2], [an, bn]]** la funcion retornara el inverso del vector complejo de la forma **[[c1, d1], [c2, d2], [cn, dn]]**.

11. **Multiplicación de un escalar por un vector complejo:**
> Dado un numero complejo **[a,b]** y un vector complejo de la forma **[[a1, b1], [a2, b2], [an, bn]]** la funcion retornara la multiplicacion por un escalar de la forma **[[c1, d1], [c2, d2], [cn, dn]]**.

12. **Transpuesta de un vector**
> Dado un vector complejo **[[a1, b1], [a2, b2], [an, bn]]** la funcion retornara el inverso del vector complejo de la forma **[[[c1, d1]], [[c2, d2]], [[cn, dn]]]**.

13. **Producto tensor de dos vectores:**
> Dada una pareja de vectores complejos **[[a1, b1], [a2, b2], [an, bn]]** y **[[c1, d1], [c2, d2], [cn, dn]]** la funcion retornara el producto tensor de la pareja de vectores complejos de la forma **[[e1, f1], [e2, f2], [en, fn]]**.

14. **Conjugada de un vector:**
> Dado un vector complejo **[[a1, b1], [a2, b2], [an, bn]]** la funcion retornara el conjugado del vector complejo de la forma **[[[c1, d1]], [[c2, d2]], [[cn, dn]]]**.

15. **Producto de dos vectores:**
> Dada una pareja de vectores complejos **[[a1, b1], [a2, b2], [an, bn]]** y **[[c1, d1], [c2, d2], [cn, dn]]** la funcion retornara el producto de la pareja de vectores complejos de la forma **[[e1, f1], [e2, f2], [en, fn]]**.

16. **Norma de un vector:**
> Dado un vector complejo **[[a1, b1], [a2, b2], [an, bn]]** la funcion retornara la norma del vector complejo de la forma **a**.

17. **Distancia entre dos vectores:**
> Dada una pareja de vectores complejos **[[a1, b1], [a2, b2], [an, bn]]** y **[[c1, d1], [c2, d2], [cn, dn]]** la funcion retornara la distancia de la pareja de vectores complejos de la forma **a**.

### Operaciones de matrices complejas
18 . **Adición de matrices complejas:** [[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]] / [[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]
> Dada una pareja de matrices complejas **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** y **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]** la funcion retornara la suma de la pareja de matrices complejas de la forma **[[[e1,f1],[e2,f2]],[[e3,f3],[en,fn]]]**.

19. **Inversa (aditiva) de una matriz compleja:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara el inverso de la matriz compleja de la forma **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]**.

20. **Multiplicación de un escalar por una matriz compleja:**
> Dada un numero complejo **[a,b]** y una matriz compleja de la forma **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara la multiplicacion por un escalar de la forma **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]**.

21. **Transpuesta de una matriz:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara la transpuesta de la matriz compleja de la forma **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]**.

22. **Conjugada de una matriz:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara la conjugada de la matriz compleja de la forma **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]**.

23. **Adjunta (daga) de una matriz/vector:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara la adjunta de la matriz compleja de la forma **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]**.

24. **Producto de dos matrices:**
> Dada una pareja de matrices complejas **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** y **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]** la funcion retornara el producto de la pareja de matrices complejas de la forma **[[[e1,f1],[e2,f2]],[[e3,f3],[en,fn]]]**.

25. **Producto tensor de dos matrices:**
> Dada una pareja de matrices complejas **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** y **[[[c1,d1],[c2,d2]],[[c3,d3],[cn,dn]]]** la funcion retornara el producto tensor de la pareja de matrices complejas de la forma **[[[e1,f1],[e2,f2]],[[e3,f3],[en,fn]]]**.

26. **Revisar si una matriz es unitaria:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara si la matriz compleja es unitaria.

27. **Revisar si una matriz es Hermitiana:**
> Dada una matriz compleja **[[[a1,b1],[a2,b2]],[[a3,b3],[an,bn]]]** la funcion retornara si la matriz compleja es hermitiana.

# Autor
Santiago López Osorio
