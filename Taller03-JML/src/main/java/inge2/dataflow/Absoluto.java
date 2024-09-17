package inge2.dataflow;

public class Absoluto {

    // Calcula el valor absoluto de un número entero.
    // Si el número es negativo, devuelve el opuesto.
    //
    //@ pure;
    //@ requires n > Integer.MIN_VALUE;
    //@ ensures (n < 0 ==> \result == -n) && (n >= 0 ==> \result == n);
    public static int valorAbsoluto(int n) {
        if (n < 0) {
            return -n;
        } else {
            return n;
        }
    }
}