package inge2.dataflow;

public class MapSumaUno {

    // Suma uno a todos los elementos de un array.
    //
    //@ requires (\forall int j; 0 <= j < arr.length; arr[j] < Integer.MAX_VALUE);
    //@ ensures (\forall int j; 0 <= j < arr.length; arr[j] == \old(arr[j])+1);
    public static void mapSumaUno(int[] arr) {
        
        //@ maintaining 0 <= i <= arr.length;
        //@ maintaining (\forall int j; 0 <= j < i; arr[j] == \old(arr[j])+1);
        //@ maintaining (\forall int j; i <= j < arr.length; arr[j] == \old(arr[j]));
        //@ decreases arr.length - i;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = arr[i] + 1;
        }
    }
}
