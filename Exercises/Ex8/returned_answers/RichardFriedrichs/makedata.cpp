#include "Pythia8/Pythia.h"

#include <iostream>
#include <fstream>
using namespace Pythia8;

int main() {

  Pythia pythia;
  pythia.readString("HiggsSM:all = on");
  pythia.readString("Print:quiet = on");
  pythia.readString("PDF:pSet = 8"); //CTEQ6L1
  pythia.init();
  std::ofstream output("masses.dat");
  for (int iEvent = 0; iEvent < 1000; ++iEvent) {
    if (!pythia.next()) continue;

    for (int iParticle = 0; iParticle < pythia.event.size(); ++iParticle) {
    if (pythia.event[iParticle].id() == 25){
      output << pythia.event[iParticle].m() << endl;
      break;
    }
  }
  }
  //pythia.stat();
  
  
  output.close();
  return 0; 
  }
