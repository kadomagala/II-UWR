package server;

import javafx.application.Platform;
import javafx.scene.media.Media;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.*;
import java.util.Random;

public class Server extends Thread {
    private DatagramSocket socket;
    private InetAddress group;
    private byte[] buf;
    private Controller controller;
    private long delayTime;

    private File[] folder;

    public boolean isOnline() {
        return isOnline;
    }

    private boolean isOnline;

    public Server(Controller controller) {
        this.controller = controller;
        try {
            group = InetAddress.getByName("230.0.0.1");
            socket = new DatagramSocket();
        } catch (Exception e) {
            System.out.println("Cant start");
        }
        isOnline = true;
        File folderName = new File("D:\\II Uwr\\Java\\RadioUDP\\music");
        this.folder = folderName.listFiles();
    }

    public void sendMessage(String message){

        buf = message.getBytes();
        DatagramPacket packet = new DatagramPacket(buf, buf.length, group,4000);
        try {
            if(!socket.isClosed())
                socket.send(packet);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void closeServer(){
        if(socket!= null) {
            sendMessage("ENDS");
            socket.close();
        }
        isOnline = false;
    }


    public void readAndSendFile(){
        Random r = new Random();
        int a = r.nextInt(folder.length);
        Platform.runLater(()-> controller.updateSongName(folder[a].getName()));
        File toSend = folder[a];
        Media media = new Media(toSend.toURI().toString());
        sendMessage(toSend.getName());
        try {
            FileInputStream fin = new FileInputStream(toSend.getPath());
            int i = 0;
            buf = new byte[512];
            while((i = fin.read(buf)) != -1) {
                DatagramPacket packet = new DatagramPacket(buf, buf.length, group, 4000);
                socket.send(packet);
                sleep(1);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
        } catch (IOException e) {
            System.out.println("Cant read bytes");
        } catch (InterruptedException e) {
            System.out.println("cant sleep");
        }
    }

    @Override
    public void run() {
        while(isOnline) {
            try {
                delayTime = 60;
                sendMessage("Next");
                readAndSendFile();
                sendMessage("Done");
                sleep(delayTime > 60000? delayTime-60000:60000);

            } catch (InterruptedException e) {
                System.out.println("cant sleep");
            }
        }
        System.out.println("closed");
    }
}
