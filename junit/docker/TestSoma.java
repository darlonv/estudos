import static org.junit.Assert.*;

import org.junit.Test;
import zz.Soma;

public class TestSoma {
    @Test
    public void testHello() {
        System.out.println("hello world");
        assertEquals(2, 1 + 1);
    }

    @Test
    public void testSoma() {
        System.out.println("Teste Soma");
        int x = Soma.somar(1,2);
        assertEquals(3, x);
    }
}

