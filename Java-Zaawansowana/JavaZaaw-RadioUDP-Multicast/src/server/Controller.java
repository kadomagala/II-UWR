package server;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.scene.paint.Color;

public class Controller {
    @FXML
    private Label songNameLbl;
    @FXML
    private Label serverStatusLbl;


    private Server server;

    public void setServer(Server server) {
        this.server = server;
    }

    public void initialize() {
        try {
            server = new Server(this);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void handleStartServer(ActionEvent event) {
        if (serverStatusLbl.getText().equals("Offline")) {
            server = new Server(this);
            server.start();
            serverStatusLbl.setText("Online");
            serverStatusLbl.setTextFill(Color.GREEN);
        }
    }


    @FXML
    public void handleStopServer(ActionEvent event) {
        if (serverStatusLbl.getText().equals("Online")) {
            server.closeServer();
            serverStatusLbl.setText("Offline");
            serverStatusLbl.setTextFill(Color.RED);
        }

    }

    public void updateSongName(String name){
        songNameLbl.setText(name);
    }
}
