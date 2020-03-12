package client;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.stage.Stage;

import java.net.URL;


public class RadioClient extends Application {



    @Override
    public void start(Stage primaryStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource("clientGUI.fxml"));
        primaryStage.setTitle("Radio");
        primaryStage.setScene(new Scene(root, 300, 275));
        primaryStage.show();

    }
    public static void main(String [] args){
        launch(args);
    }
}
