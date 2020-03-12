import org.junit.jupiter.api.Assertions;

import java.util.LinkedList;

import static org.junit.jupiter.api.Assertions.*;

class StringExtensionsTest {

    /**
     * Test dla poprawnych danych
     */
    @org.junit.jupiter.api.Test
    void listWO1() {
        LinkedList<String> te1 = new LinkedList<>();
        te1.add("ola");
        te1.add("agata");
        te1.add("asd");
        LinkedList<String> res = new LinkedList<>();
        res.add("ola");
        res.add("agata");
        assertEquals(StringExtensions.listWO(te1,"asd"),res);
    }


    /**
     * Test dla null pierwszego argumentu
     */
    @org.junit.jupiter.api.Test
    void listWO2() {
        LinkedList<String> te1 = null;
        Exception thrown = Assertions.assertThrows(IllegalArgumentException.class, () ->{
            LinkedList<String> res = StringExtensions.listWO(te1, "asd");
        });
        assertEquals(thrown.getMessage(), "Lista jest null");
    }

    /**
     * Testy dla listy zawierajacej nulle
     */
    @org.junit.jupiter.api.Test
    void listWO3() {
        LinkedList<String> te1 = new LinkedList<>();
        te1.add("ola");
        te1.add(null);
        te1.add("agata");
        te1.add("asd");
        te1.add(null);
        LinkedList<String> res = new LinkedList<>();
        res.add("ola");
        res.add(null);
        res.add("agata");
        res.add(null);
        assertEquals(StringExtensions.listWO(te1,"asd"),res);
    }

}