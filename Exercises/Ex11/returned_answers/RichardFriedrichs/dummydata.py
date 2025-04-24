#!/usr/bin/env python3

import ROOT
import array

def dummydata():
    amount = 100000
    myfile = ROOT.TFile("DYJetsToLL.root", "RECREATE")
    datatree = ROOT.TTree("Events", "Events")
    
    trigger = array.array('b', [0]) 
    pileup = array.array('i', [0])
    datatree.Branch("HLT_IsoMu24", trigger, "HLT_IsoMu24/O")
    datatree.Branch("PV_npvs", pileup, "PV_npvs/I")
    
    RNG = ROOT.TRandom3(1234)
    
    for i in range(amount):
        temp = RNG.Gaus(0, 20)
        pileup[0] = round(temp)
        if temp >= 10:
            trigger[0] = 0
        else:
            trigger[0] = 1
        datatree.Fill()

    datatree.Write()

    myfile.Close()

if __name__ == "__main__":
    dummydata()