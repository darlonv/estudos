import static org.junit.Assert.*;

import org.junit.Test;
import arquivosjava.*;

public class TestEx02 {

    @Test
    public void teste(){
        assertEquals(1,1);
        assertEquals(Ex02.soma(1,1), 2);
        assertEquals(Ex02.soma(1,2), 3);
    }
}
