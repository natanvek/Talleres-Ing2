package inge2.dataflow;

public class BusquedaLineal {

    // Busca un elemento en un arreglo de enteros.
    //
    //@ requires true;
    //@ ensures (\forall int k; 0 <= k < arr.length; arr[k] == \old(arr[k]));
    //@ ensures \result == (\exists int j; 0 <= j && j < arr.length; arr[j] == elem);
    public static boolean busquedaLineal(int elem, int[] arr) {
        boolean result = false;

        //@ maintaining 0 <= i <= arr.length;
        //@ maintaining result == (\exists int j; 0 <= j && j < i; arr[j] == elem);
        //@ decreases arr.length - i;
        for (int i = 0; i < arr.length; i++) {
            if (elem == arr[i]) {
                result = true;
            }
        }
        return result;
    }
}

