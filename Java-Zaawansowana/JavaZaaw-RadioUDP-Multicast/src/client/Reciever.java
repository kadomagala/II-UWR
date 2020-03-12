package client;

import javafx.application.Platform;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;

import java.io.*;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class Reciever extends Thread {
    protected MulticastSocket socket = null;
    protected byte[] buf = new byte[512];
    private Controller controller;

    private String msg = "XD";

    public Reciever(Controller controller) {
        this.controller = controller;
    }

    @Override
    public void run(){
        try {
            socket = new MulticastSocket(4000);
            InetAddress group = InetAddress.getByName("230.0.0.1");
            socket.joinGroup(group);
            Runnable updater = () -> controller.modifyCurrentLbl(msg);
            while (true) {
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                socket.receive(packet);
                if(packet.getLength() == 4) {
                    File myFile = new File("temp.mp3");
                    String recieved = new String(packet.getData(), 0, packet.getLength());
                    if(recieved.equals("Next")){
                        packet = new DatagramPacket(buf, buf.length);
                        socket.receive(packet);
                        recieved = new String(packet.getData(), 0, packet.getLength());
                        msg = recieved;
                        Platform.runLater(updater);
                        ByteArrayOutputStream baos = new ByteArrayOutputStream();
                        do{
                            packet = new DatagramPacket(buf, buf.length);
                            socket.receive(packet);
                            baos.write(packet.getData());
                        }while (packet.getLength() != 4);
                        recieved = new String(packet.getData(), 0, packet.getLength());
                        OutputStream outStream = null;
                        try {
                            outStream = new FileOutputStream(myFile);
                            // writing bytes in to byte output stream
                            baos.writeTo(outStream);

                        } catch (IOException e) {
                            e.printStackTrace();
                        } finally {
                            outStream.close();
                        }
                    }
                    if(recieved.equals("Done")){
                        System.out.println("Done");
                        Platform.runLater(()-> controller.playMedia(myFile.toURI().toString()));


                    }else if(recieved.equals("ENDS")){
                        System.out.println("ENDS");
                        break;
                    }
                }

            }
            socket.leaveGroup(group);
            socket.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

}
