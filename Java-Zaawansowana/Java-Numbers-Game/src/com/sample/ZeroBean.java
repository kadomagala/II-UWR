package sample;

import java.beans.*;
import java.io.Serializable;
import java.util.Random;

public class ZeroBean implements Serializable, Runnable {


    private volatile Cordinates zeroCords = new Cordinates();
    private PropertyChangeSupport chg = new PropertyChangeSupport(this);
    private StripModel model;

    public synchronized PropertyChangeSupport getChg() {
        return chg;
    }

    public synchronized void setChg(PropertyChangeSupport chg) {
        this.chg = chg;
    }

    public synchronized StripModel getModel() {
        return model;
    }

    public synchronized void setModel(StripModel model) {
        this.model = model;
    }

    public ZeroBean() { }

    public synchronized Cordinates getZeroCords() {
        return zeroCords;
    }

    public synchronized void setZeroCords(Cordinates zeroCords) {
        Cordinates oldCords = new Cordinates(this.zeroCords.getX(), this.zeroCords.getY());
        chg.firePropertyChange("zeroCords", oldCords, zeroCords);
        this.zeroCords = zeroCords;
    }

    public synchronized void addPropertyChangeListener(PropertyChangeListener l){
        chg.addPropertyChangeListener(l);
    }

    public synchronized void removePropertyChangeListener(PropertyChangeListener l){
        chg.removePropertyChangeListener(l);
    }



    @Override
    public void run() {
        Random r = new Random();
        while(true) {
            for (int i = 0; i < 2; i++) {
                if (r.nextBoolean()) { //OX
                    if (r.nextBoolean()) { //PRAWO
                        if (zeroCords.getX() + 1 < model.getWidth()) {
                            setZeroCords(new Cordinates(zeroCords.getX() + 1, zeroCords.getY()));
                            break;
                        }
                    } else { //LEWO
                        if (zeroCords.getX() - 1 >= 0) {
                            setZeroCords(new Cordinates(zeroCords.getX() - 1, zeroCords.getY()));
                            break;
                        }
                    }
                } else { //OY
                    if (r.nextBoolean()) {//gora
                        if (zeroCords.getY() - 1 >= 0) {
                            setZeroCords(new Cordinates(zeroCords.getX(), zeroCords.getY() - 1));
                            break;
                        }
                    } else {
                        if (zeroCords.getY() + 1 < model.getHeight()) {
                            setZeroCords(new Cordinates(zeroCords.getX(), zeroCords.getY() + 1));
                            break;
                        }
                    }
                }
            }
            try {
                //int delay = r.nextInt(500) + 300;
                int delay = 500;
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
