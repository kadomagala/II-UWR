import java.io.DataInputStream;
import java.io.InputStream;
import java.net.Socket;

public class Client {
    public static void main(String [] args){
        try {
            System.out.println("Connecting...");
            Socket client = new Socket("localhost",20191);
            System.out.println("Connected success");

            InputStream inFromServer  = client.getInputStream();
            DataInputStream in = new DataInputStream(inFromServer);

            System.out.println("Server respond: " + in.readUTF());
            client.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
