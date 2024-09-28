package org.autotest.mutantGenerator.operators.returns;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtExpression;
import spoon.reflect.code.CtReturn;
import spoon.reflect.declaration.CtElement;
import spoon.reflect.reference.CtTypeReference;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#NULL_RETURNS
 *
 * Este operador reemplaza los valores de retorno de las funciones que devuelven un Object por null.
 */
public class NullReturnsMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtReturn)) {
            return false;
        }
        // COMPLETAR
        return false;
    }

    @Override
    public void process(CtElement candidate) {
        // COMPLETAR
    }

    private static CtTypeReference getReturnedExpressionType(CtReturn op) {
        return op.getReturnedExpression().getType();
    }

    private CtExpression getNullValueForReturnExpression(CtReturn op) {
        // COMPLETAR
        return null;
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtReturn op = (CtReturn)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getReturnedExpression().toString() + " por " + getNullValueForReturnExpression(op).toString() +
                " en la línea " + op.getPosition().getLine() + ".";
    }
}
