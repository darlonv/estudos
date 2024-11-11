import static org.junit.Assert.*;

import org.junit.Test;
import arquivosjava.*;

public class TestEx01 {

    @Test
    public void teste(){
        // ClasseASerTestada obj = new ClasseASerTestada();
        // String retornoDoMetodo = obj.metodoASerTestado();
        // assertEquals("teste", retornoDoMetodo);
        assertEquals(1,1);
        assertEquals(0,0);
        assertEquals(Ex01.soma(0,0), 0);
        assertEquals(Ex01.soma(-1,1), 0);
    }
}
