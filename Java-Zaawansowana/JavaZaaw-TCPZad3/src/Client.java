import java.io.*;
import java.net.Socket;

public class Client {

    public static void main(String[] args){
        try {
            Socket socket = new Socket("localhost", 20193);
            BufferedWriter socketWriter = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            BufferedReader socketReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            String outMsg="";
            boolean err = false;
            while(!err ) {
                outMsg = consoleReader.readLine();
                String inMsg;
                if(outMsg.equals("."))
                    break;

                socketWriter.write(outMsg);
                socketWriter.write("\n");
                socketWriter.flush();

                inMsg = socketReader.readLine();
                if(!inMsg.equals("Wrong number format")){
                    err = true;
                }
                System.out.println(inMsg);
            }
            if(!outMsg.equals(".")) {
                String inMsg;
                while ((inMsg = socketReader.readLine()) != null) {
                    System.out.println(inMsg);
                }
            }
            socketWriter.close();
            socketReader.close();
            consoleReader.close();
            socket.close();
        }catch (Exception e){

        }
    }
}
