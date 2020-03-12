package client;


import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;

public class Controller {
    @FXML
    private Label currentLbl;


   @FXML
    private MediaView mediaView;
    private Media media;
    private MediaPlayer mediaPlayer;
    private Reciever reciever;

    public void initialize(){
        reciever = new Reciever(this);
        reciever.start();
    }

    public Label getCurrentLbl() {
        return currentLbl;
    }
    public void modifyCurrentLbl(String msg){
        currentLbl.setText(msg);
    }
    public void playMedia(String path){
        if(mediaPlayer!= null)
            mediaPlayer.stop();
        media = new Media(path);
        mediaPlayer = new MediaPlayer(media);
        mediaPlayer.play();
        mediaView.setMediaPlayer(mediaPlayer);

    }
}
