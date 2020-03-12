import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RMIPrimeNumbersInterface extends Remote {
    public boolean isPrime(long x) throws RemoteException;
    public long[] factorize(long x)throws RemoteException;
}
