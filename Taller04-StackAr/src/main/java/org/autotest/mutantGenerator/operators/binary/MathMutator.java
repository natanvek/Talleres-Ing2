package org.autotest.mutantGenerator.operators.binary;

import org.autotest.helpers.BinaryOperatorKindToString;
import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.BinaryOperatorKind;
import spoon.reflect.code.CtBinaryOperator;
import spoon.reflect.declaration.CtElement;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#MATH
 *
 * Este operador de mutación reemplaza las operaciones aritméticas binarias para enteros o punto flotante con otra operación.
 */
public class MathMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtBinaryOperator)) {
            return false;
        }

        CtBinaryOperator op = (CtBinaryOperator)candidate;
        List<BinaryOperatorKind> targetOperations = Arrays.asList(
            BinaryOperatorKind.PLUS, // +
            BinaryOperatorKind.MINUS, // -
            BinaryOperatorKind.MUL, // *
            BinaryOperatorKind.DIV, // /
            BinaryOperatorKind.MOD // %
        );
        return targetOperations.contains(op.getKind());
    }

    @Override
    public void process(CtElement candidate) {
        CtBinaryOperator op = (CtBinaryOperator)candidate;
        op.setKind(getReplacement(op.getKind()));
    }

    public BinaryOperatorKind getReplacement(BinaryOperatorKind kind) {
        // NOTA: A falta de mas informacion, se reemplaza la operacion por la operacion inversa.

        switch (kind) {
            case PLUS:
                return BinaryOperatorKind.MINUS;
            case MINUS:
                return BinaryOperatorKind.PLUS;
            case MUL:
                return BinaryOperatorKind.DIV;
            case DIV:
                return BinaryOperatorKind.MUL;
            case MOD:
                return BinaryOperatorKind.DIV;
        }
        return null;
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtBinaryOperator op = (CtBinaryOperator)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                BinaryOperatorKindToString.get(op.getKind()) + " por " + BinaryOperatorKindToString.get(getReplacement(op.getKind())) +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
