package server;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.paint.Color;

import java.io.IOException;
import java.net.ServerSocket;

public class Controller {

    @FXML
    private Label clientGuessLabel;
    @FXML
    private Label tryNumLabel;
    @FXML
    private Label drawnNumberLabel;
    @FXML
    private Label serverStatusLabel;
    @FXML
    private Button turnOffButton;
    @FXML
    private Button turnOnButton;

    private boolean serverStatus = false;

    public Controller() {
    }

    public void updateRandomLabel(int value){
        drawnNumberLabel.setText(String.valueOf(value));
    }

    @FXML
    protected void handleTurnOnButton(ActionEvent event) {
        if (!serverStatus) {
            if (WhatTheNumber.serverSocket == null) {
                try {
                    WhatTheNumber.serverSocket = new ServerSocket(20194);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (!WhatTheNumber.serverSocket.isClosed() && !WhatTheNumber.threadServer.isInterrupted()) {
                WhatTheNumber.threadServer.start();
            }

            serverStatus = true;
            serverStatusLabel.setText("Online");
            serverStatusLabel.setTextFill(Color.GREEN);

        }
    }

    @FXML
    protected void handleTurnOffButton(ActionEvent event) {
        if (serverStatus) {
            try {
                WhatTheNumber.threadServer.interrupt();
                if(WhatTheNumber.server!= null)
                    WhatTheNumber.server.close();
            } catch (IOException e) {
                System.out.println("Unable to close");
            }
            serverStatus = false;
            serverStatusLabel.setText("Offline");
            serverStatusLabel.setTextFill(Color.RED);

        }
    }

}
