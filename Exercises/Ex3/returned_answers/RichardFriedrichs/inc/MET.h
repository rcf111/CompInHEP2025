#ifndef MET_h
#define MET_h

#include <vector>

using namespace std;

class MET
{
private:
  vector<double> MET_vector;

public:
  MET();
  MET(double MET_x, double MET_y);
  MET(vector<double> MET_vector_input);
  ~MET();
  vector<double> MET_return_vector();
  double MET_return_x();
  double MET_return_y();
  double MET_return_phi();
};
#endif
