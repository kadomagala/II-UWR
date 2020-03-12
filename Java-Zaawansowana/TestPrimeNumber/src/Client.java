import java.awt.*;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {
    private Client(){

    }
    public static void main(String [] args){
        try {
            Registry registry = LocateRegistry.getRegistry(null);

            RMIPrimeNumbersInterface stub = (RMIPrimeNumbersInterface) registry.lookup("RMIPrimeNumbersInterface");

            EventQueue.invokeLater(() -> new MyFrame(stub));

        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
