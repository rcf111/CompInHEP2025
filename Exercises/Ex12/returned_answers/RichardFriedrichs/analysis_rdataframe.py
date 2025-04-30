#!/usr/bin/env python

import datetime

import ROOT

ROOT.ROOT.EnableImplicitMT()
ROOT.gROOT.SetBatch(True)

def main():

    df = ROOT.RDataFrame("Events", "DYJetsToLL.root")
    df = df.Filter("HLT_IsoMu24 == 1", "Events wtriggering IsoMu24")

    histo = df.Histo1D(("pileup", ";x-axis;y-axis", 50, 0, 50), "PV_npvs")

    fOUT = ROOT.TFile.Open("output3.root","RECREATE")

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    now = datetime.datetime.now()
    m = "produced: %s %s"%(days[now.weekday()],now)
    timestamp = ROOT.TNamed(m,"")
    timestamp.Write()

    histo.Write()

    c = ROOT.TCanvas()
    histo.Draw()
    histo.GetXaxis().SetTitle("Number of primary vertices")
    histo.GetYaxis().SetTitle("Number of events") 
    c.SaveAs("pileup_histogram_root.png")

    fOUT.Close()

if __name__ == "__main__":
    main()

