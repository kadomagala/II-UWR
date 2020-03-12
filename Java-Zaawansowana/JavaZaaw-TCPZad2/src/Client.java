import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Client {
    public static void main(String [] args){
        try {
            Socket socket = new Socket("localhost", 20192);
            BufferedWriter socketWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            String outMsg;

            while((outMsg = consoleReader.readLine()) != null){
                if(outMsg.equals(".")){
                    break;
                }

                socketWriter.write(outMsg);
                socketWriter.write("\n");
                socketWriter.flush();
            }
            socket.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
