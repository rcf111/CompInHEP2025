#include "recon_track.h"
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

void test_recon_track_class()
{
    recon_track recon_track_1(500.0, 300.0, 0.0, 400.0);
    cout << "The coordinates are: x = " << recon_track_1.get_x() << ", y = " << recon_track_1.get_y() << ", z = " << recon_track_1.get_z() << " and the total energy is " << recon_track_1.get_t() << endl;
    cout << "The transverse momentum is ( x y ) = ( ";
    for (double coord : recon_track_1.get_transverse_momentum())
    {
        cout << coord << " ";
    }
    cout << ")" << endl;
    cout << "The pseudorapidity is " << recon_track_1.get_pseudorapidity() << endl;
    // now testing subclass
    simul_particle particle_1(recon_track_1.get_fourvector(), 1, 0);
    simul_particle particle_2(206.0, 100.0, 81.0, 25.0, 2, particle_1.get_id());
    cout << "The transverse momentum of the parent particle is ( x y ) = ( ";
    for (double coord : particle_1.get_transverse_momentum())
    {
        cout << coord << " ";
    }
    cout << ")" << endl;
    cout << "The pseudorapidity of the parent particle is " << particle_1.get_pseudorapidity() << endl;

    cout << "The transverse momentum of the child particle is ( x y ) = ( ";
    for (double coord : particle_2.get_transverse_momentum())
    {
        cout << coord << " ";
    }
    cout << ")" << endl;
    cout << "The pseudorapidity of the child particle is " << particle_2.get_pseudorapidity() << endl;

    cout << "To confirm parenthood, let's compare the ids: the id of the parent particle is " << particle_1.get_id() << " and the parent id of the child particle is " << particle_2.get_parent_id() << endl;
    cout << "NB: I wasn't sure whether particle id was referring to the particle type or an integer, like a normal id, so I set it to integer as a precaution - since integers can always be interpreted as codenames for particle types." << endl;
}

int main()
{
    test_recon_track_class();
    return 0;
}
