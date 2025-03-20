#include "Pythia8/Pythia.h"

#include <iostream>
#include <fstream>
using namespace Pythia8;

int main() {

  Pythia pythia;
  pythia.readString("HiggsSM:all = on");
  pythia.readString("Print:quiet = on");
  pythia.init();
  cout << "The width is " << setprecision(15) << pythia.particleData.mWidth(25) << endl;
  return 0; 
  }
