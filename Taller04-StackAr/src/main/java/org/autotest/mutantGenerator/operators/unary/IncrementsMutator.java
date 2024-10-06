package org.autotest.mutantGenerator.operators.unary;

import org.autotest.helpers.UnaryOperatorKindToString;
import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtUnaryOperator;
import spoon.reflect.code.UnaryOperatorKind;
import spoon.reflect.declaration.CtElement;

import java.util.Arrays;
import java.util.List;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#INCREMENTS
 *
 * Este operador de mutación reemplaza los operadores de incremento y decremento de variables locales (variables de pila).
 */
public class IncrementsMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // call super method to check if the candidate is not part of randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtUnaryOperator)) {
            return false;
        }

        CtUnaryOperator op = (CtUnaryOperator)candidate;
        List<UnaryOperatorKind> targetOperations = Arrays.asList(
            UnaryOperatorKind.POSTDEC, // --
            UnaryOperatorKind.POSTINC, // ++
            UnaryOperatorKind.PREDEC, // --
            UnaryOperatorKind.PREINC // ++
        );

        return targetOperations.contains(op.getKind());
    }

    @Override
    public void process(CtElement candidate) {
        CtUnaryOperator op = (CtUnaryOperator)candidate;
        op.setKind(getReplacement(op.getKind()));
    }

    public UnaryOperatorKind getReplacement(UnaryOperatorKind kind) {
        switch (kind) {
            case POSTDEC:
                return UnaryOperatorKind.POSTINC;
            case POSTINC:
                return UnaryOperatorKind.POSTDEC;
            case PREDEC:
                return UnaryOperatorKind.PREINC;
            case PREINC:
                return UnaryOperatorKind.PREDEC;
        }
        return null;
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtUnaryOperator op = (CtUnaryOperator)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                UnaryOperatorKindToString.get(op.getKind()) + " por " + UnaryOperatorKindToString.get(getReplacement(op.getKind())) +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
