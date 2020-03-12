import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Echo {

    public static void main(String [] args){
        try {
            ServerSocket serverSocket = new ServerSocket(20192);
            Socket server = serverSocket.accept();
            server.setSoTimeout(120000);
            try{
                BufferedReader socketReader = new BufferedReader(new InputStreamReader(server.getInputStream()));
                String inMsg;
                while((inMsg = socketReader.readLine()) != null){
                    System.out.println(inMsg);
                }
                server.close();

            }catch (Exception e){
                e.printStackTrace();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
