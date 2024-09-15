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

    //@ requires true;
    public StackAr() {
        this(DEFAULT_CAPACITY);
    }

    //@ requires capacity > 0;
    public StackAr(int capacity) {
        elems = new int[capacity];
    }

    //@ pure;
    //@ requires true;
    //@ ensures \result == (top == -1);
    public boolean isEmpty() {
        return top == -1;
    }

    //@ pure;
    //@ requires true;
    //@ ensures \result == (top == elems.length - 1);
    public boolean isFull() {
        return top == elems.length - 1;
    }

    //@ pure;
    //@ requires true;
    //@ ensures \result == (top + 1);
    public int size() {
        return top + 1;
    }

    //@ pure;
    //@ requires !isFull();
    //@ ensures top == \old(top) + 1;
    //@ ensures elems[top] == o;
    public void push(int o) {
        elems[++top] = o;
    }

    //@ requires !isEmpty();
    //@ ensures \result == elems[top];
    //@ ensures top == \old(top) - 1;
    public int pop() {
        return elems[top--];
    }

    //@ pure;
    //@ requires !isEmpty();
    //@ ensures \result == elems[top];
    public int peek() {
        return elems[top];
    }
}

