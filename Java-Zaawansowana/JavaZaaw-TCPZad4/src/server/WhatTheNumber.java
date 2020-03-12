package server;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class WhatTheNumber extends Application {
    public static ServerSocket serverSocket;
    public static Socket server;
    public static Controller controller;
    public static Thread threadServer = new Thread(){
        @Override
        public void run(){
            try {
                System.out.println("Waiting for client");
                server = serverSocket.accept();
                System.out.println("Accepted connection");
                game();
            } catch (IOException e) {
                System.out.println("Interrupted");
            }
        }
    };


    public static void main(String[] args) {
        launch(args); }

    @Override
    public void start(Stage primaryStage) {

        Parent root = null;
        try {
            root = FXMLLoader.load(getClass().getResource("gui.fxml"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        primaryStage.setTitle("What The Number Server");
        primaryStage.setScene(new Scene(root));
        primaryStage.show();
        FXMLLoader fxmlLoader = new FXMLLoader();
        try {
            Pane p = fxmlLoader.load(getClass().getResource("foo.fxml").openStream());
        } catch (IOException e) {
            e.printStackTrace();
        }
        controller = (Controller) fxmlLoader.getController();

    }

    public static void game(){
        System.out.println("client playing");

        Random r = new Random();
        int random = r.nextInt(8999)+1000;
        controller.updateRandomLabel(random);

    }


}
