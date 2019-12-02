package sample;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.util.Timer;
import java.util.TimerTask;

public class Main extends Application {
    static int numOfBeans = 50;
    static int width = 10;
    static int height = 10;
    static StripModel model = new StripModel(width, height, numOfBeans);
    static StripView view = new StripView(width, height, model.getStrip());
    static StripController controller = new StripController(view,model);


    @Override
    public void start(Stage primaryStage) throws Exception{
        //Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
        primaryStage.setTitle("Game");
        //primaryStage.setScene(new Scene(root, 500, 500));

        Scene scene = new Scene(view, 700,700);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {

        Thread [] threads = new Thread[model.getNumbersAmount()];
        Runnable[] runnables = new Runnable[model.getNumbersAmount()];

        runnables[0] = controller.getZeroBean();
        for(int i = 1; i < numOfBeans-1; i++){
            runnables[i] = controller.getNumberBeans()[i-1];
        }

        for(int i = 0; i < numOfBeans; i++){
            threads[i] = new Thread(runnables[i]);
        }

        for(int i = 0; i < numOfBeans; i++)
           threads[i].start();


        launch(args);
    }
}
