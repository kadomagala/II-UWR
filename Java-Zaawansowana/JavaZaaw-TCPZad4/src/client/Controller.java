package client;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

import java.io.IOException;

public class Controller {
    @FXML
    private TextField numberTextField;
    @FXML
    private Label serverRespondLabel;
    @FXML
    private Button checkButton;
    @FXML
    private Button surrenderButton;



    @FXML
    void handleCheckButton(ActionEvent event){
        int number;
        try{
            number = Integer.valueOf(numberTextField.getText());
        }catch (NumberFormatException e){
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("Error");
            alert.setContentText("Wrong number format");
            alert.show();
        }


    }

    @FXML
    void handleSurrenderButton(ActionEvent event){
        try {
            SelectNumber.socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
