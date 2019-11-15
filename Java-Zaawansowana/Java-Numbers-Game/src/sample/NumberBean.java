package sample;

import java.io.Serializable;
import java.util.Random;
import java.beans.*;

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

public class NumberBean implements Serializable, Runnable {
    private volatile Cordinates cords = new Cordinates();
    private StripModel model;
    private VetoableChangeSupport veto = new VetoableChangeSupport(this);
    private boolean isAlive = true;
    private int value;

    public synchronized StripModel getModel() {
        return model;
    }

    public synchronized void setModel(StripModel model) {
        this.model = model;
    }

    public synchronized VetoableChangeSupport getVeto() {
        return veto;
    }

    public synchronized void setVeto(VetoableChangeSupport veto) {
        this.veto = veto;
    }



    public synchronized boolean isAlive() {
        return isAlive;
    }

    public synchronized void setAlive(boolean alive) {
        isAlive = alive;
    }


    public NumberBean() { }

    public NumberBean(Cordinates cords, int value) {
        this.setValue(value);
        this.cords = cords;

    }

    public synchronized Cordinates getCords() {
        return cords;
    }

    public synchronized void setCords(Cordinates newCords) throws PropertyVetoException {
        if(isAlive) {
            Cordinates oldCords = new Cordinates(this.cords.getX(), this.cords.getY());

            veto.fireVetoableChange("cords", oldCords, newCords);
            if(newCords.getX() == model.getZeroBean().getZeroCords().getX() && newCords.getY() == model.getZeroBean().getZeroCords().getY())
                throw new PropertyVetoException("Going on zre", new PropertyChangeEvent(this, "cords", oldCords, newCords));
            this.cords = newCords;
        }
    }


    public synchronized int getValue() {
        return value;
    }

    public synchronized void setValue(int value) {
        if(value == -1)
            isAlive = false;
        this.value = value;
    }


    public synchronized void addVetoableChangeListener(VetoableChangeListener l) {
        veto.addVetoableChangeListener(l);
    }

    public synchronized void removeVetoableChangeListener(VetoableChangeListener l) {
        veto.removeVetoableChangeListener(l);
    }


    public static boolean primeNumber(int number) {
        if (number == 2) return true;
        if (number % 2 == 0) return false;
        for (int i = 3; i * i <= number; i += 2) {
            if (number % i == 0)
                return false;
        }
        return true;
    }

    private synchronized int distanceToZero() {
        return abs(model.getZeroBean().getZeroCords().getX() - getCords().getX()) + abs(model.getZeroBean().getZeroCords().getY() - getCords().getY());
    }

    @Override
    public  void run() {
        while (isAlive) {

            Random r = new Random();
            for (int i = 0; i < 2; i++) {
                if (distanceToZero() > model.getWidth())  {
                    if (r.nextBoolean()) { // OX
                        int dest = (model.getZeroBean().getZeroCords().getX() > getCords().getX()) ? 1 : -1;
                        try {
                            if (getCords().getX() + dest >= 0 && getCords().getX() + dest < model.getWidth()) {
                                setCords(new Cordinates(getCords().getX() + dest, getCords().getY()));
                            }
                            else
                                continue;
                        } catch (PropertyVetoException e) {
                            continue;
                        }
                        break;
                    } else { //OY
                        int dest = (model.getZeroBean().getZeroCords().getY() > getCords().getY()) ? 1 : -1;
                        try {
                            if (getCords().getY() + dest >= 0 && getCords().getY() + dest < model.getHeight()) {
                                setCords(new Cordinates(getCords().getX(), getCords().getY() + dest));
                            }
                            else
                                continue;
                        } catch (PropertyVetoException e) {
                            continue;
                        }
                        break;
                    }
                } else {
                    if (r.nextBoolean()) {//OX
                        if (r.nextBoolean()) {//PRAWY
                            int newX = cords.getX() + 1;
                            if (newX < model.getWidth()) {
                                try {
                                    setCords(new Cordinates(newX, getCords().getY()));
                                } catch (PropertyVetoException e) {
                                    continue;
                                }
                                break;
                            }
                        } else {//LEWY
                            int newX = cords.getX() - 1;
                            if (newX >= 0) {
                                try {
                                    setCords(new Cordinates(newX, getCords().getY()));
                                } catch (PropertyVetoException e) {
                                    continue;
                                }
                                break;

                            }
                        }
                    } else {//OY
                        if (r.nextBoolean()) {//GORA
                            int newY = cords.getY() - 1;
                            if (newY >= 0) {
                                try {
                                    setCords(new Cordinates(getCords().getX(), newY));
                                } catch (PropertyVetoException e) {
                                    continue;
                                }
                                break;
                            }
                        } else {//DOL
                            int newY = cords.getY() + 1;
                            if (newY < model.getHeight()) {
                                try {
                                    setCords(new Cordinates(getCords().getX(), newY));
                                } catch (PropertyVetoException e) {
                                    continue;
                                }
                                break;
                            }
                        }
                    }
                }
            }
            try {
                //int delay = r.nextInt(500) + 600;
                int delay = 1000;
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
