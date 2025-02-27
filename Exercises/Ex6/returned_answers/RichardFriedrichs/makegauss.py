#!/usr/bin/env python3

import ROOT

def makegauss():
    amount = 1000
    myfile = ROOT.TFile("data2.root", "RECREATE")
    datatree = ROOT.TTree("datatree", "Tree with gaussian data")
    
    # Create a variable to hold the values
    value = ROOT.std.vector('float')()  # Use a vector to hold the value
    datatree.Branch("values", value)
    
    RNG = ROOT.TRandom3(1234)
    
    for i in range(amount):
        value.push_back(RNG.Gaus(15, 3))
        datatree.Fill()

    datatree.Write()

    myfile.Close()

if __name__ == "__main__":
    makegauss()