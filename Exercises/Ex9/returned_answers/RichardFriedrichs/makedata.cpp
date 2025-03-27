#include "Pythia8/Pythia.h"

#include <iostream>
#include <fstream>
using namespace Pythia8;

int main() {

  Pythia pythia;
  pythia.readString("Print:quiet = on");
  pythia.readString("SoftQCD:nonDiffractive = on");
  pythia.readString("Beams:eCM = 13600");
  pythia.init();
  std::ofstream ptOut("pt.dat");
  std::ofstream rapidOut("rapid.dat");
  for (int iEvent = 0; iEvent < 10000; ++iEvent) {
    if (!pythia.next()) continue;

    for (int iParticle = 0; iParticle < pythia.event.size(); ++iParticle) {
    if (pythia.event[iParticle].id() == 13){
      ptOut << pythia.event[iParticle].pT() << endl;
      rapidOut << pythia.event[iParticle].eta() << endl;
      //break;
    }
  }
  }
  //pythia.stat();
  
  
  ptOut.close();
  rapidOut.close();
  return 0; 
  }
