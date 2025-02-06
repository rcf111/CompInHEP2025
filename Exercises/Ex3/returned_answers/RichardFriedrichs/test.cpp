#include "MET.h"
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void test_MET_class()
{
    MET met_custom(10.0, 20.0);
    cout << "MET (x, y): (" << met_custom.MET_return_x() << ", " << met_custom.MET_return_y() << ")" << endl;
    cout << "MET phi: " << met_custom.MET_return_phi() << " radians" << endl;

    vector<double> input_vector = {10.0, 20.0};
    MET met_vector(input_vector);
    cout << "Vector input MET (x, y): (" << met_vector.MET_return_x() << ", " << met_vector.MET_return_y() << ")" << endl;
    cout << "Vector input MET phi: " << met_vector.MET_return_phi() << " radians" << endl;

    MET met_quadrant_2(-5.0, 5.0);
    cout << "Quadrant 2 MET phi: " << met_quadrant_2.MET_return_phi() << " radians" << endl;

    MET met_quadrant_3(-5.0, -5.0);
    cout << "Quadrant 3 MET phi: " << met_quadrant_3.MET_return_phi() << " radians" << endl;

    MET met_quadrant_4(5.0, -5.0);
    cout << "Quadrant 4 MET phi: " << met_quadrant_4.MET_return_phi() << " radians" << endl;
    vector<double> pull_out_vector = met_quadrant_4.MET_return_vector();
    cout << "x y = ";
    for (double coord : pull_out_vector)
    {
        cout << coord << " ";
    }
    cout << endl;
}

int main()
{
    test_MET_class();
    return 0;
}
