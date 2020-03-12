import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyFrame extends JFrame {
    private RMIPrimeNumbersInterface stub;
    private JButton btnIsPrime;
    private JButton btnFactorise;
    private JLabel lblResult;
    private JTextField textFieldNumber;
    private JPanel pane;
    private GridBagConstraints c;
    private JButton button;

    public MyFrame(RMIPrimeNumbersInterface stub) {
        super("Prime Number tester");
        this.stub = stub;
        pane = new JPanel();
        pane.setLayout(new GridBagLayout());
        c = new GridBagConstraints();
        c.fill = GridBagConstraints.HORIZONTAL;


        c.weightx = 0.5;
        c.fill = GridBagConstraints.HORIZONTAL;
        c.gridx = 0;
        c.gridy = 0;
        c.gridwidth = 3;
        pane.add(new JLabel("Enter number here:"), c);

        c.fill = GridBagConstraints.HORIZONTAL;
        c.weightx = 0.5;
        c.gridx = 0;
        c.gridy = 1;
        textFieldNumber = new JTextField();
        pane.add(textFieldNumber , c);



        btnIsPrime = new JButton("Check if num is prime");
        btnIsPrime.addActionListener(e -> {

        });
        c.fill = GridBagConstraints.HORIZONTAL;
        c.weightx = 0.5;
        //c.gridwidth = 3;
        c.gridx = 0;
        c.gridy = 2;
        pane.add(btnIsPrime, c);


        btnFactorise = new JButton("Factorize");
        btnFactorise.addActionListener(e -> {

        });
        c.fill = GridBagConstraints.HORIZONTAL;
        c.weightx = 0.5;
        //c.gridwidth = 3;
        c.gridx = 1;
        c.gridy = 2;
        pane.add(btnFactorise, c);



        lblResult = new JLabel();




        add(pane);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 300);
        setLocation(400, 400);
        setVisible(true);
    }
}
