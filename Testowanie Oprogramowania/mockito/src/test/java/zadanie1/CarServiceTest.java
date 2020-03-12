package zadanie1;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito.*;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.HashMap;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;


@ExtendWith(MockitoExtension.class)
class CarServiceTest {
    @Mock
    private CarDAO carDAO;

    @InjectMocks
    private CarService carService = new CarService();

    private Car []cars;

    @BeforeEach
    void init(){
        cars = new Car[7];
        cars[0] = new Car();
        cars[0].setId(0L);
        cars[0].setYearMileage(dataForZero);

        cars[1] = new Car();
        cars[1].setId(1L);
        cars[1].setYearMileage(dataForOne);

        cars[2] = new Car();
        cars[2].setId(2L);
        cars[2].setYearMileage(dataForTwo);

        cars[3] = new Car();
        cars[3].setId(3L);
        cars[3].setYearMileage(dataForThree);

        cars[4] = new Car();
        cars[4].setId(4L);
        cars[4].setYearMileage(dataForFour);

        cars[5] = new Car();
        cars[5].setId(5L);
        cars[5].setYearMileage(dataForFive);

        cars[6] = new Car();
        cars[6].setId(6L);
        cars[6].setYearMileage(dataForSix);
    }

    @ParameterizedTest
    @MethodSource("provideArgsForFindMileage")
    void findMileageBetweenYears(Long productId, String startYear, String endYear) {
        int id = Math.toIntExact(productId);
        when(carDAO.findById(productId)).thenReturn(cars[id]);

        long res = carService.findMileageBetweenYears(productId,startYear,endYear);

        long expected = 0;
        for(int i = Integer.valueOf(startYear); i <= Integer.valueOf(endYear); i++){
            expected += i + 100000L + productId * 100000L;
        }

        assertEquals(expected,res);
    }

    private static Stream<Arguments> provideArgsForFindMileage(){
        return Stream.of(
                Arguments.of(0L,"1990", "2000"),
                Arguments.of(1L,"1995", "2003"),
                Arguments.of(2L,"1993", "2000"),
                Arguments.of(3L,"1991", "2002"),
                Arguments.of(4L,"1997", "2001"),
                Arguments.of(5L,"1994", "2005"),
                Arguments.of(6L,"1990", "1999")
        );
    }

    private static HashMap<String,Long> dataForZero = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 100000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForOne = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 200000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForTwo = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 300000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForThree = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 400000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForFour = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 500000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForFive = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 600000L + i);
            }
        }
    };


    private static HashMap<String,Long> dataForSix = new HashMap<String,Long>(){
        {
            for(int i = 1990; i <= 2005; i++){
                put(String.valueOf(i), 700000L + i);
            }
        }
    };
}