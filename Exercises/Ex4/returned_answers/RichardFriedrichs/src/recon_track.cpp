#include "recon_track.h"
#include <vector>
#include <cmath>

using namespace std;

recon_track::recon_track()
{
    fourvector.push_back(0);
    fourvector.push_back(0);
    fourvector.push_back(0);
    fourvector.push_back(0);
}

recon_track::~recon_track() {}

recon_track::recon_track(double t, double x, double y, double z)
{
    fourvector.push_back(t);
    fourvector.push_back(x);
    fourvector.push_back(y);
    fourvector.push_back(z);
}

recon_track::recon_track(vector<double> fourvector_input)
{
    fourvector = fourvector_input;
}

vector<double> recon_track::get_fourvector()
{
    return fourvector;
}
double recon_track::get_t()
{
    return fourvector[0];
}
double recon_track::get_x()
{
    return fourvector[1];
}
double recon_track::get_y()
{
    return fourvector[2];
}
double recon_track::get_z()
{
    return fourvector[3];
}
vector<double> recon_track::get_transverse_momentum()
{
    return {fourvector[1], fourvector[2]};
}
double recon_track::get_pseudorapidity()
{
    double phi = acos(get_z() / sqrt(pow(get_x(), 2) + pow(get_y(), 2) + pow(get_z(), 2)));
    return -log(tan(phi / 2));
}

simul_particle::simul_particle()
{
    fourvector.push_back(0);
    fourvector.push_back(0);
    fourvector.push_back(0);
    fourvector.push_back(0);
    id = 0;
    parent_id = 0;
}

simul_particle::~simul_particle() {}

simul_particle::simul_particle(double t, double x, double y, double z, int id_input, int parent_id_input)
{
    fourvector = {t, x, y, z};
    id = id_input;
    parent_id = parent_id_input;
}

simul_particle::simul_particle(vector<double> fourvector_input, int id_input, int parent_id_input)
{
    fourvector = fourvector_input;
    id = id_input;
    parent_id = parent_id_input;
}

int simul_particle::get_id()
{
    return id;
}
int simul_particle::get_parent_id()
{
    return parent_id;
}