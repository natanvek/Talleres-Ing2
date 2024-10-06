package org.autotest.mutants;

/**
 * FalseConditionalsMutator: Se reemplazó getClass() != obj.getClass() por false en la línea 100.
 */
public class StackArMutated182 extends org.autotest.Stack {
    private static final int DEFAULT_CAPACITY = 10;

    private final java.lang.Object[] elems;

    private int readIndex = -1;

    public StackArMutated182() {
        this(org.autotest.mutants.StackArMutated182.DEFAULT_CAPACITY);
    }

    public StackArMutated182(int capacity) throws java.lang.IllegalArgumentException {
        if (capacity < 0) {
            throw new java.lang.IllegalArgumentException();
        }
        this.elems = new java.lang.Object[capacity];
    }

    /**
     * El "invariante de representación" de una clase es una propiedad que deben cumplir todas las instancias de la clase.
     * Al utilizar la anotación @CheckRep, podemos indicarle a Randoop qué métodos en las clases bajo test son métodos de
     * invariante de representación. Randoop llamará a estos métodos; si el método falla en algún momento, Randoop generará
     * el test como un test fallido.
     *
     * A continuación, utilizamos la anotación @CheckRep sobre un método de instancia público sin argumentos y con tipo de
     * retorno booleano. En este caso, Randoop interpretará un valor de retorno verdadero como la satisfacción del
     * invariante de representación, y un valor de retorno falso como la violación del invariante de representación.
     */
    @randoop.CheckRep
    public boolean repOK() {
        try {
            // COMPLETAR
            return true;
        } catch (java.lang.Exception | java.lang.Error e) {
            java.lang.System.err.println("ERROR en el método repOK.");
            e.printStackTrace();
            return false;
        }
    }

    public int size() {
        return readIndex + 1;
    }

    public boolean isEmpty() {
        return size() == 0;
    }

    public boolean isFull() {
        return size() == elems.length;
    }

    public void push(java.lang.Object o) throws java.lang.IllegalStateException {
        if (isFull()) {
            throw new java.lang.IllegalStateException();
        }
        this.readIndex++;
        this.elems[readIndex] = o;
    }

    public java.lang.Object pop() throws java.lang.IllegalStateException {
        if (isEmpty()) {
            throw new java.lang.IllegalStateException();
        }
        java.lang.Object rv = this.top();
        readIndex--;
        return rv;
    }

    public java.lang.Object top() throws java.lang.IllegalStateException {
        if (isEmpty()) {
            throw new java.lang.IllegalStateException();
        }
        java.lang.Object rv = this.elems[readIndex];
        return rv;
    }

    @java.lang.Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = (prime * result) + java.util.Arrays.hashCode(elems);
        result = (prime * result) + readIndex;
        return result;
    }

    @java.lang.Override
    public boolean equals(java.lang.Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (false) {
            return false;
        }
        org.autotest.mutants.StackArMutated182 other = ((org.autotest.mutants.StackArMutated182) (obj));
        if (!java.util.Arrays.equals(elems, other.elems)) {
            return false;
        }
        if (readIndex != other.readIndex) {
            return false;
        }
        return true;
    }

    @java.lang.Override
    public java.lang.String toString() {
        java.lang.StringBuffer b = new java.lang.StringBuffer();
        b.append("[");
        for (int i = 0; i <= readIndex; i++) {
            if (i > 0) {
                b.append(",");
            }
            java.lang.Object o = elems[i];
            java.lang.String s = java.lang.String.valueOf(o);
            b.append(s);
        }
        b.append("]");
        return b.toString();
    }
}