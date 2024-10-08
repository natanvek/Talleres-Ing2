# Respuestas Taller 4

## Ejercicio 1

a. Se generaron 55 mutantes.

b. El que más generó es `FalseConditionalsMutator`, con un total de 10 mutaciones. Porque dicho operador de mutación encontró la mayor cantidad de candidatos a mutar (i.e. `return X` donde `X` no es `false`).
  
c. El que menos generó es `NullReturnsMutator`, con un total de 2 mutaciones. Porque solo se habrán encontrado dos instancias de `return` para un objeto.


## Ejercicio 2

- StackTests1
	- Mutantes vivos: 41
	- Mutantes muertos: 14
	- Mutation score: 25%
	
- StackTests2
	- Mutantes vivos: 27
	- Mutantes muertos: 28
	- Mutation score: 50%
	
- StackTests3
	- Mutantes vivos: 27
	- Mutantes muertos: 28
	- Mutation score: 50%
	

## Ejercicio 3

a. El nuevo mutation score es 94%.

b.  
	- Mutantes vivos: 3  
	- Mutantes muertos: 52  
	 
c.   
	- `FalseConditionalsMutator`: reemplaza `this == obj` por `false` en la linea 96, pero es equivalente porque igualmente se detecta la igualdad consigo mismo.  
	- `FalseConditionalsMutator`: reemplaza `isEmpty()` por `false` en la linea 69, pero es equivalente porque igualmente se produce la excepción al llamar a `pop()`, que hace el mismo chequeo.  
	- `MathMutator`: reemplaza `*` por `/` en la linea 89, pero es equivalente porque dividir y multiplicar por 1 es lo mismo.  

d. El instruction coverage promedio es 59%.

e. El peor instruction coverage para una clase mutada es 5%. Es la mutación donde 10 se reemplaza por -1 en la linea 8, lo que significa que intenta inicializar un stack con `capacity` menor a 0, que inmediatamente resulta en un `IllegalArgumentException` y no permite cubrir las demás instrucciones.

## Ejercicio 4

a. Produjo 289 tests.
b. Pasó todos los tests.
c. No pudimos encontrar los reportes de JaCoCo siguiendo las instrucciones del enunciado.

## Ejercicio 5

a. Los tests mostraban que la implementación de StackAr no cumplía con el invariante: $\forall i > readIndex, elems_i = null$. Esto se puede solucionar asegurándose de que los elementos que se popean se vuelven null en el arreglo interno.

b. No pudimos encontrar los reportes de JaCoCo siguiendo las instrucciones del enunciado.


## Ejercicio 6

Mutation score obtenido: 100%