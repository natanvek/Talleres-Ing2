package inge2.dataflow;

public class StackAr {

    /**
     * Capacidad por defecto de la pila.
     */
    private final static int DEFAULT_CAPACITY = 10;

    /**
     * Arreglo que contiene los elementos de la pila.
     */
    private final int[] elems;

    /**
     * Indice del tope de la pila.
     */
    private int top = -1;

    public StackAr() {
        this(DEFAULT_CAPACITY);
    }

    //@ requires capacity > 0;
    public StackAr(int capacity) {
        elems = new int[capacity];
    }

    //@ pure;
    public boolean isEmpty() {
        return top == -1;
    }

    //@ pure;
    public boolean isFull() {
        return top == elems.length - 1;
    }

    //@ pure;
    public int size() {
        return top + 1;
    }

    //@ requires this.top < this.elems.length - 1;
    //@ ensures this.top == \old(this.top) + 1;
    //@ ensures this.elems[this.top] == o;
    //@ ensures (\forall int i; 0 <= i < this.top; this.elems[i] == \old(this.elems[i]))
    public void push(int o) {
        elems[++top] = o;
    }

    //@ requires 0 <= this.top;
    //@ ensures \result == this.elems[this.top];
    //@ ensures this.top == \old(this.top) - 1;
    //@ ensures (\forall int i; 0 <= i <= this.top; this.elems[i] == \old(this.elems[i]))
    public int pop() {
        return elems[top--];
    }

    //@ pure;
    //@ requires this.top >= 0;
    //@ ensures \result == this.elems[this.top];
    public int peek() {
        return elems[top];
    }
}


