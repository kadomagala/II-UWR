import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Totient {

    private static int gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(20193);
            Socket server = serverSocket.accept();
            BufferedReader socketReader = new BufferedReader(new InputStreamReader(server.getInputStream()));
            BufferedWriter socketWriter = new BufferedWriter(new OutputStreamWriter(server.getOutputStream()));
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            int n = 0;

            String inMsg="";
            while((inMsg = socketReader.readLine()) != null)
            try {
                if(inMsg.equals(".")){
                    System.out.println("closing connection");
                    break;
                }
                n = Integer.parseInt(inMsg);
                break;
            }catch (NumberFormatException e) {
                socketWriter.write("Wrong number format");
                socketWriter.write("\n");
                socketWriter.flush();
            }
            if(!(inMsg != null && inMsg.equals("."))) {
                socketWriter.write("Working with good number");
                socketWriter.write("\n");
                socketWriter.flush();
                new Thread(() -> {
                    try {
                        String consoleMsg;
                        while ((consoleMsg = consoleReader.readLine()) != null) {
                            if(consoleMsg.equals("quit")){
                                socketReader.close();
                                socketWriter.close();
                                server.close();
                                //serverSocket.close();
                                break;
                            }
                        }
                    }catch (Exception e){
                        e.printStackTrace();
                    }
                }).start();
                for (int i = 2; i < n && !server.isClosed(); i++) {
                    if (gcd(i, n) == 1) {
                        if(!server.isClosed()) {
                            socketWriter.write(String.valueOf(i));
                            socketWriter.write("\n");
                            socketWriter.flush();
                        }
                    }
                }
            }

            socketReader.close();
            socketWriter.close();
            server.close();
            //serverSocket.close();
        } catch (IOException e) {

        }
    }


}
