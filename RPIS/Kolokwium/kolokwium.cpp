#include <cmath>
#include <iostream>
#include <vector>
using namespace std;



double roomberg_method(double (*f)(double ), int n, double a, double b){
    vector<vector<double>> R(n, vector<double>(n));

    // trapezoid rule
    for(int i = 0; i < n; i++){    
        double h_i = (double)(b - a) / (double)(1 << i);
        double r_i = 0.0;
        double x_prev = a;
        for(int k = 0; k <= (1 << i); k++){
            r_i += f(x_prev) + f(x_prev + h_i);
            x_prev += h_i;
        }

        R[0][i] = r_i * h_i;
    }

    for(int m = 1; m < n; m++){
        for(int j = 0; j < n - m; j++){
            double four_to_pow_m = pow(4.0, m);
            R[m][j] = (four_to_pow_m * R[m-1][j+1] - R[m-1][j]) / (four_to_pow_m - 1.0); 
        }
    }

    return R[n-1][0];
}


double g(double x){
    return exp(-(x*x)/2.0);
}

int main(){
    int n;
    cin >> n;
    double t;
    cin >> t;
    double result = roomberg_method(g, n, 0.0, t);
    cout << result;
    return 0;
}