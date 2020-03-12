import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends ImplPrimeNumbers {
    public Server() {
        super();
    }

    public static void main(String[] args) {

        try {
            ImplPrimeNumbers obj = new ImplPrimeNumbers();
            RMIPrimeNumbersInterface stub = (RMIPrimeNumbersInterface) UnicastRemoteObject.exportObject(obj, 0);

            Registry registry = LocateRegistry.getRegistry();

            registry.bind("RMIPrimeNumbersInterface", stub);
            System.err.println("Server ready");

        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
