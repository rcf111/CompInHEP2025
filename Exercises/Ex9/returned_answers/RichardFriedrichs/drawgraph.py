import ROOT
import numpy as np

ROOT.gROOT.SetBatch(True)

def drawgraph():

    pt = []
    eta = []
    with open('pt.dat', 'r') as file:
        for line in file:
            line = line.strip()
            pt.append(float(line))
    
    with open('rapid.dat', 'r') as file:
        for line in file:
            line = line.strip()
            eta.append(float(line))



    n_bins_pt = len(pt)
    n_bins_eta = len(eta)
    hist_pt = ROOT.TH1F("hist1", "Transverse momentum distribution", n_bins_pt, min(pt), max(pt))
    

    for i in pt:
        hist_pt.Fill(i)

    hist_eta = ROOT.TH1F("hist2", "Pseudorapidity distribution", n_bins_eta, min(eta), max(eta))
    

    for i in eta:
        hist_eta.Fill(i)

    #bw_function = ROOT.TF1("bw", "[0] * ( 1 / ((x**2-[1]**2)**2 + [1]**2*[2]**2 ))", min(values), max(values))
    #bw_function.SetParameters(1.0, 125.0, 1.0)

    #hist.Fit(bw_function, "R")
    #k = bw_function.GetParameter(0)
    #m = bw_function.GetParameter(1)
    #gamma= bw_function.GetParameter(2)
    #gamma = np.abs(gamma)
    

    canvas = ROOT.TCanvas("canvas1", "Transverse momentum distribution", 800, 600)
    hist_pt.Draw()
    #bw_function.Draw("SAME")
    hist_pt.GetXaxis().SetTitle("Transverse momentum")
    hist_pt.GetYaxis().SetTitle("Number of events")
    canvas.Update()

    canvas.SaveAs("pt.pdf")
    canvas.SaveAs("pt.png")
    canvas.SaveAs("pt.C")

    canvas2 = ROOT.TCanvas("canvas2", "Pseudorapidity distribution", 800, 600)
    hist_eta.Draw()
    #bw_function.Draw("SAME")
    hist_eta.GetXaxis().SetTitle("Pseudorapidity")
    hist_eta.GetYaxis().SetTitle("Number of events")
    canvas2.Update()

    canvas2.SaveAs("eta.pdf")
    canvas2.SaveAs("eta.png")
    canvas2.SaveAs("eta.C")
    #print("The width is",gamma)


if __name__ == "__main__":
    drawgraph()
