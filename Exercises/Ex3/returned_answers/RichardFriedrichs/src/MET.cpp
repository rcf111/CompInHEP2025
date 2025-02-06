#include "MET.h"
#include <vector>
#include <cmath>

using namespace std;

MET::MET()
{
    MET_vector.push_back(0);
    MET_vector.push_back(0);
}

MET::~MET() {}

MET::MET(double MET_x, double MET_y)
{
    MET_vector.push_back(MET_x);
    MET_vector.push_back(MET_y);
}

MET::MET(vector<double> MET_vector_input)
{
    MET_vector = MET_vector_input;
}

vector<double> MET::MET_return_vector()
{
    return MET_vector;
}
double MET::MET_return_x()
{
    return MET_vector[0];
}
double MET::MET_return_y()
{
    return MET_vector[1];
}
double MET::MET_return_phi()
{
    double x = MET_return_x();
    double y = MET_return_y();
    return (x >= 0) ? atan(y / x) : atan(y / x) + M_PI;
}