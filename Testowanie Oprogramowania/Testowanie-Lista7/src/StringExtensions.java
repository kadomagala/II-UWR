import java.util.LinkedList;

public class StringExtensions {
    public static LinkedList<String> listWO(LinkedList<String> ls, String x) throws IllegalArgumentException{

        if(ls == null)
            throw new IllegalArgumentException("Lista jest null");
        if(x == null)
            throw new IllegalArgumentException("String jest null");

        LinkedList<String> result = new LinkedList<>();

        for (String s : ls){
            if( s == null || !s.equals(x))
                result.add(s);
        }
        return result;
    }
}
