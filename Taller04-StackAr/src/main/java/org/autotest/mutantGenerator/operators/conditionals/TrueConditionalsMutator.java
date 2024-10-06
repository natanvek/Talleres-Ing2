package org.autotest.mutantGenerator.operators.conditionals;

import org.autotest.mutantGenerator.operators.MutationOperator;
import spoon.reflect.code.CtIf;
import spoon.reflect.declaration.CtElement;

/**
 * Operador de mutación basado en https://pitest.org/quickstart/mutators/#REMOVE_CONDITIONALS
 *
 * Este operador reemplaza los valores en las condiciones de guardas por true.
 */
public class TrueConditionalsMutator extends MutationOperator {
    @Override
    public boolean isToBeProcessed(CtElement candidate) {
        // llamo al método super para verificar que el candidato no es parte de randoop.CheckRep: repOK method
        if (!super.isToBeProcessed(candidate)) {
            return false;
        }

        if (!(candidate instanceof CtIf)) {
            return false;
        }

        CtIf op = (CtIf)candidate;
        // No se debe mutar una condición que ya es true
        if (op.getCondition().toString().equals("true")) {
            return false;
        }

        return false;
    }

    @Override
    public void process(CtElement candidate) {
        CtIf op = (CtIf)candidate;
        op.setCondition(op.getFactory().Code().createLiteral(true));
    }

    @Override
    public String describeMutation(CtElement candidate) {
        CtIf op = (CtIf)candidate;
        return this.getClass().getSimpleName() + ": Se reemplazó " +
                op.getCondition().toString() + " por true"+
                " en la línea " + op.getPosition().getLine() + ".";
    }
}