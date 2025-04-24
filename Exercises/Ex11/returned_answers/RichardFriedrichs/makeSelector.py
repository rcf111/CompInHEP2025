#!/usr/bin/env python

import sys
import ROOT



fIN = ROOT.TFile.Open("DYJetsToLL.root")
tree = fIN.Get("Events")
tree.MakeSelector("MyAnalysis")
fIN.Close()


