package inge2.dataflow;

public class BusquedaLineal {

    // Busca un elemento en un arreglo de enteros.
    //
    //@ pure;
    //@ requires true;
    //@ ensures \result == (\exists int i; 0 <= i && i < arr.length; arr[i] == elem);
    public static boolean busquedaLineal(int elem, int[] arr) {
        boolean result = false;

        for (int i = 0; i < arr.length; i++) {
            if (elem == arr[i]) {
                result = true;
            }
        }

        return result;
    }
}