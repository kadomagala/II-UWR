package sample;

import javafx.beans.property.SimpleIntegerProperty;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderStroke;
import javafx.scene.layout.BorderStrokeStyle;
import javafx.scene.layout.BorderWidths;
import javafx.scene.text.Font;
import javafx.util.Duration;

import java.util.Random;

public class StripView extends GridPane {
    private final int width, height;
    private Label[][] number;

    public StripView(int width, int height, int [][]strip){

        this.width = width;
        this.height = height;
        number = new Label[height][width];
        setHgap(10);
        setVgap(10);

        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                number[i][j] = new Label();
                number[i][j].setMinSize(60,60);
                number[i][j].setFont(new Font("Arial", 20));
                number[i][j].setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, null, new BorderWidths(1))));
                int finalI = i;
                int finalJ = j;
                Timeline timeline = new Timeline(new KeyFrame(Duration.millis(1),
                        event -> {
                            number[finalI][finalJ].setText((strip[finalI][finalJ] == -1) ? "   " : String.valueOf(strip[finalI][finalJ]));
                            if(strip[finalI][finalJ] == 0){
                                number[finalI][finalJ].setTextFill(Color.RED);
                            }else if(NumberBean.primeNumber(strip[finalI][finalJ])){
                                number[finalI][finalJ].setTextFill(Color.GREEN);
                            }
                            else
                                number[finalI][finalJ].setTextFill(Color.BLACK);
                        }),
                        new KeyFrame(Duration.millis(1)));
                timeline.setCycleCount(Animation.INDEFINITE);
                timeline.play();
                add(number[i][j], i , j);
            }
        }
    }

    public void updateView(int strip[][]){
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                int value = strip[i][j];
                number[i][j].setText(value == -1 ? "" : String.valueOf(value));
                if(strip[i][j] == 0){
                    number[i][j].setTextFill(Color.RED);
                }else if(NumberBean.primeNumber(strip[i][j])){
                    number[i][j].setTextFill(Color.GREEN);
                }
                else
                    number[i][j].setTextFill(Color.BLACK);
            }
        }
    }

}
