package sample;

import java.beans.*;
import java.util.Random;

public class StripController implements PropertyChangeListener, VetoableChangeListener {
    private StripView view;
    private StripModel model;

    private NumberBean[] numberBeans;
    private ZeroBean zeroBean;

    public synchronized StripView getView() {
        return view;
    }

    public synchronized void setView(StripView view) {
        this.view = view;
    }

    public synchronized StripModel getModel() {
        return model;
    }

    public synchronized void setModel(StripModel model) {
        this.model = model;
    }

    public synchronized NumberBean[] getNumberBeans() {
        return numberBeans;
    }

    public synchronized void setNumberBeans(NumberBean[] numberBeans) {
        this.numberBeans = numberBeans;
    }

    public synchronized ZeroBean getZeroBean() {
        return zeroBean;
    }

    public synchronized void setZeroBean(ZeroBean zeroBean) {
        this.zeroBean = zeroBean;
    }

    public StripController(StripView view, StripModel model) {
        this.view = view;
        this.model = model;
        init();


        view.updateView(model.getStrip());
    }

    private void init() {
        Random r = new Random();

        int x = r.nextInt(model.getWidth());
        int y = r.nextInt(model.getHeight());
        numberBeans = new NumberBean[model.getNumbersAmount() - 1];
        zeroBean = new ZeroBean();
        zeroBean.setZeroCords(new Cordinates(x, y));
        zeroBean.addPropertyChangeListener(this);
        zeroBean.setModel(model);
        model.setZeroBean(zeroBean);
        model.strip[y][x] = 0;
        int i = 0;
        while (i < model.getNumbersAmount() - 1) {
            int value = r.nextInt(model.getNumbersAmount() * 10) + 1;
            do {
                x = r.nextInt(model.getWidth());
                y = r.nextInt(model.getHeight());
            } while (model.strip[y][x] != -1);
            model.strip[y][x] = value;
            NumberBean bean = new NumberBean(new Cordinates(x, y), value);
            bean.addVetoableChangeListener(this);
            bean.setModel(model);
            numberBeans[i] = bean;
            i++;
        }
    }

    @Override
    public synchronized void propertyChange(PropertyChangeEvent evt) {

        if(evt.getPropertyName() == "zeroCords") {
            Cordinates newCords = (Cordinates) evt.getNewValue();
            Cordinates oldCords = (Cordinates) evt.getOldValue();
            int temp = model.strip[oldCords.getY()][oldCords.getX()];

            if (NumberBean.primeNumber(model.strip[newCords.getY()][newCords.getX()])) {

                int prime = model.strip[newCords.getY()][newCords.getX()];
                model.strip[oldCords.getY()][oldCords.getX()] = prime;
                model.strip[newCords.getY()][newCords.getX()] = temp;

            } else {
                for (var bean : numberBeans) {

                    if (bean.getCords().getX() == newCords.getX() && bean.getCords().getY() == newCords.getY()) {
                        System.out.println("deleting:" + bean.getValue());
                        bean.setAlive(false);
                        bean.setValue(-1);
                        break;
                    }
                }
                model.strip[oldCords.getY()][oldCords.getX()] = -1;
                model.strip[newCords.getY()][newCords.getX()] = temp;
            }
        }
    }

    @Override
    public synchronized void vetoableChange(PropertyChangeEvent evt) throws PropertyVetoException {
        if(evt.getPropertyName() == "cords") {
            Cordinates newCords = (Cordinates) evt.getNewValue();
            Cordinates oldCords = (Cordinates) evt.getOldValue();
            if (model.strip[newCords.getY()][newCords.getX()] != -1)
                throw new PropertyVetoException("Can't choose this pos", evt);
            else {
                int temp = model.strip[oldCords.getY()][oldCords.getX()];
                model.strip[oldCords.getY()][oldCords.getX()] = -1;
                model.strip[newCords.getY()][newCords.getX()] = temp;
            }
        }
    }


    public synchronized void updateView() {
        view.updateView(model.getStrip());
    }

}
