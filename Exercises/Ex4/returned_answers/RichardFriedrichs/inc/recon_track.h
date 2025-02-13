#ifndef recon_track_h
#define recon_track_h

#include <vector>

using namespace std;

class recon_track
{
protected:
  vector<double> fourvector;

public:
  recon_track();
  recon_track(double t, double x, double y, double z);
  recon_track(vector<double> fourvector_input);
  ~recon_track();
  vector<double> get_fourvector();
  double get_t();
  double get_x();
  double get_y();
  double get_z();
  vector<double> get_transverse_momentum();
  double get_pseudorapidity();
};

class simul_particle : public recon_track
{
protected:
  int id;
  int parent_id;

public:
  simul_particle();
  simul_particle(double t, double x, double y, double z, int id_input, int parent_id_input);
  simul_particle(vector<double> fourvector_input, int id_input, int parent_id_input);
  ~simul_particle();
  int get_id();
  int get_parent_id();
};
#endif
