import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.text.SimpleDateFormat;

public class Date extends Thread {
    private ServerSocket serverSocket;

    public Date() throws IOException{
        serverSocket = new ServerSocket(20191);
    }


    public void run(){
        while (true){
            try {
                System.out.println("Waiting for client...");
                Socket server = serverSocket.accept();

                System.out.println("Connected to client");

                SimpleDateFormat formatter= new SimpleDateFormat("yyyy-MM-dd 'at' HH:mm:ss z");
                java.util.Date date = new java.util.Date(System.currentTimeMillis());
                DataOutputStream out = new DataOutputStream(server.getOutputStream());
                out.writeUTF(formatter.format(date));
                server.close();


            }catch (SocketTimeoutException s){
                System.out.println("Socket timed out");
                break;
            }
            catch (IOException e){
                e.printStackTrace();
                break;
            }
        }
    }

    public static void main(String[] args) {
        try{
            Thread t = new Date();
            t.start();

        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
