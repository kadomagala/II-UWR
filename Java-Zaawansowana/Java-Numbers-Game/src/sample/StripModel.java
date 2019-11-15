package sample;

import java.util.Random;

public class StripModel {
    private final int width, height;
    private int numbersAmount;
    public volatile int [][] strip;
    private ZeroBean zeroBean;

    public void setNumbersAmount(int numbersAmount) {
        this.numbersAmount = numbersAmount;
    }

    public void setStrip(int[][] strip) {
        this.strip = strip;
    }

    public ZeroBean getZeroBean() {
        return zeroBean;
    }

    public void setZeroBean(ZeroBean zeroBean) {
        this.zeroBean = zeroBean;
    }

    public StripModel(int width, int height, int numbersAmount) {

        this.width = width;
        this.height = height;
        this.numbersAmount = numbersAmount;
        strip = new int[height][width];
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                strip[i][j] = -1;
            }
        }
    }


    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public int getNumbersAmount() {
        return numbersAmount;
    }

    public int[][] getStrip() {
        return strip;
    }


}
