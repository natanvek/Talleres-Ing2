package org.autotest;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

public class StackTests3 extends MutationAnalysisRunner {
    @Override
    protected boolean useVerboseMode() {
        return false;
    }

    // Tests de StackTests2

    public void testSizeIncreasesByOne() throws Exception {
        Stack stack = createStack();
        assertEquals(0, stack.size());
        stack.push(42);
        assertEquals(1, stack.size());
    }

    public void testDefaultConstructor() throws Exception {
        Stack stack = createStack();
        assertTrue(stack.isEmpty());
    }

    public void testConstructorWithSpecifiedCapacity() throws Exception {
        Stack stack = createStack(5);
    }

    public void testConstructorWithNegativeCapacity() {
        assertThrows(IllegalArgumentException.class, () -> {
            Stack stack = createStack(-1);
        });
    }

    public void testIsEmptyMethod() throws Exception {
        Stack stack = createStack();
        assertTrue(stack.isEmpty());
        stack.push(42);
        assertFalse(stack.isEmpty());
        stack.pop();
        assertTrue(stack.isEmpty());
    }

    public void testIsFullMethod() throws Exception {
        Stack stack = createStack(1);
        assertFalse(stack.isFull());
        stack.push(42);
        assertTrue(stack.isFull());
        stack.pop();
        assertFalse(stack.isFull());
    }

    public void testToStringMethod() throws Exception {
        Stack stack = createStack(2);
        assertEquals("[]", stack.toString());
        stack.push(42);
        assertEquals("[42]", stack.toString());
        stack.push(43);
        assertEquals("[42,43]", stack.toString());
    }

    public void testEqualsToDifferentClass() throws Exception {
        Stack stack = createStack();
        assertFalse(stack.equals(new ArrayList<>()));
    }

    public void testEqualsToItself() throws Exception {
        Stack stack = createStack();
        assertTrue(stack.equals(stack));
    }

    public void testTopFromEmptyStack() throws Exception {
        Stack stack = createStack();
        assertThrows(IllegalStateException.class, () -> {
            stack.top();
        });
    }

    public void testCanCreateStackWithZeroCapacity() throws Exception {
        Stack stack = createStack(0);
    }

    public void testStacksAreEqual() throws Exception {
        Stack stack1 = createStack();
        Stack stack2 = createStack();
        assertEquals(stack1, stack2);
    }

    public void testStacksAreNotEqual() throws Exception {
        Stack stack1 = createStack();
        Stack stack2 = createStack();
        stack1.push(42);
        assertNotEquals(stack1, stack2);
    }

    public void testUnequalIfDifferentReadIndex () throws Exception {
        Stack stack1 = createStack();
        Stack stack2 = createStack();
        // Mismos elementos
        stack1.push(1);
        stack1.push(2);
        stack2.push(1);
        stack2.push(2);
        // Diferente readIndex
        stack1.pop();
        assertNotEquals(stack1, stack2);
    }

    public void testIsEmpty () throws Exception {
        Stack stack = createStack();
        assertTrue(stack.isEmpty());
    }

    public void testTopReturnsLastElement () throws Exception {
        Stack stack = createStack();
        stack.push(1);
        stack.push(2);
        assertEquals(2, stack.top());
    }

    public void testPopReturnsLastElement () throws Exception {
        Stack stack = createStack();
        stack.push(1);
        stack.push(2);
        assertEquals(2, stack.pop());
    }

    public void testDoesNotEqualNull () throws Exception {
        Stack stack = createStack();
        assertFalse(stack.equals(null));
    }

    public void testCannotPushToFullStack () throws Exception {
        Stack stack = createStack(1);
        stack.push(1);
        assertThrows(IllegalStateException.class, () -> {
            stack.push(2);
        });
    }

    public void testCannotPopFromEmptyStack () throws Exception {
        Stack stack = createStack();
        assertThrows(IllegalStateException.class, () -> {
            stack.pop();
        });
    }

    public void testAreUnequalByElements () throws Exception {
        Stack stack1 = createStack();
        Stack stack2 = createStack();
        stack1.push(1);
        stack2.push(2);
        assertNotEquals(stack1, stack2);
    }

    public void testHashCode () throws Exception {
        Stack stack = createStack();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        Object[] elems = new Object[10];
        elems[0] = 1;
        elems[1] = 2;
        elems[2] = 3;
        int expected = 1;
        expected = 31 * expected + Arrays.hashCode(elems);
        expected = 31 * expected + 2;

        assertEquals(expected, stack.hashCode());
    }


}
