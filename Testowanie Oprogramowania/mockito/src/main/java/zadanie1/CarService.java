package zadanie1;

import java.util.Map;

public class CarService {

    private CarDAO carDAO;

    public long findMileageBetweenYears(Long productId, String startYear, String endYear) {
        Car product = carDAO.findById(productId);
        long sum = 0;
        for (Map.Entry<String, Long> entry : product.getYearMileage().entrySet()) {
            if (startYear.compareTo(entry.getKey()) <= 0 && endYear.compareTo(entry.getKey()) >= 0) {
                sum += entry.getValue();
            }
        }
        return sum;
    }

    public void setEntityManager(CarDAO carDAO) {
        this.carDAO = carDAO;
    }
}
