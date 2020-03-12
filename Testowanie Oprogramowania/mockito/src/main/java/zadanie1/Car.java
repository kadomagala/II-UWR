package zadanie1;

import java.util.HashMap;

public class Car {

    private Long id;

    private HashMap<String, Long> yearMileage;

    public void setId(Long id) {
        this.id = id;
    }

    public Long getId() {
        return id;
    }

    public void setYearMileage(HashMap<String, Long> yearMileage) {
        this.yearMileage = yearMileage;
    }

    public HashMap<String, Long> getYearMileage() {
        return yearMileage;
    }
}
