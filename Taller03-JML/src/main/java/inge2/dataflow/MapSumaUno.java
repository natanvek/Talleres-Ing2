package inge2.dataflow;

public class MapSumaUno {

    // Suma uno a todos los elementos de un array.
    //
    //@ modifies arr[*];
    //@ requires true;
    //@ ensures (\forall int i; 0 <= i && i < arr.length; arr[i] == \old(arr[i] + 1));
    //@ ensures arr.length == \old(arr.length);
    public static void mapSumaUno(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] + 1;
        }
    }
}