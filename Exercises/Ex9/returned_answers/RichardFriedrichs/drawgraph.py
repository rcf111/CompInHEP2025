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
    hist_pt.GetXaxis().SetTitle("Transverse momentum in GeV/c")
    hist_pt.GetYaxis().SetTitle("Number of events")
    """fit_func = ROOT.TF1("fit_func", "[1]*x**[2]*e**([3]*x)", 0.1, 8)
    fit_func.SetParameters(1.0, -1.0)
    hist_pt.Fit(fit_func, "R") 
    power = fit_func.GetParameter(2)
    decay = fit_func.GetParameter(3)"""
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
    
    print("The distribution of transverse momentum seems to be rising from 0 to a sharp peak at about 0.2-0.3 GeV/c and then sharply decaying to zero. If the values near zero being absent are an artefact of numerical generation, then an exponential or power law decay seems to fit the distribution well.")
    print("The distribution of pseudorapidity seems to be a relatively flat bump around 0. It might have a slightly tooth-like structure, with symmetric bumps on either side of 0.")

    hits_for_partII= 0
    for i in range(n_bins_pt):
        if pt[i]>5 and abs(eta[i])<2.5:
            hits_for_partII+=1
    print("The probability of detecting a muon is",hits_for_partII/n_bins_pt)


if __name__ == "__main__":
    drawgraph()
