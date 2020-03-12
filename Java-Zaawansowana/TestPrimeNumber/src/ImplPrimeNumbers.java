import java.rmi.RemoteException;

public class ImplPrimeNumbers implements RMIPrimeNumbersInterface {
    @Override
    public boolean isPrime(long x) throws RemoteException {
        return false;
    }

    @Override
    public long[] factorize(long x) throws RemoteException {
        return new long[0];
    }
}
