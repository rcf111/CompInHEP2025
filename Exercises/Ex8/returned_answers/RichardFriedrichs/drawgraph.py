import ROOT
import numpy as np

ROOT.gROOT.SetBatch(True)

def drawgraph():

    values = []
    with open('masses.dat', 'r') as file:
        for line in file:
            line = line.strip()
            values.append(float(line))



    n_bins = len(values)
    hist = ROOT.TH1F("hist", "Mass distribution", n_bins, min(values), max(values))
    

    for mass in values:
        hist.Fill(mass)

    bw_function = ROOT.TF1("bw", "[0] * ( 1 / ((x**2-[1]**2)**2 + [1]**2*[2]**2 ))", min(values), max(values))
    bw_function.SetParameters(1.0, 125.0, 1.0)

    hist.Fit(bw_function, "R")
    k = bw_function.GetParameter(0)
    m = bw_function.GetParameter(1)
    gamma= bw_function.GetParameter(2)
    gamma = np.abs(gamma)
    

    canvas = ROOT.TCanvas("canvas", "Mass distribution", 800, 600)
    hist.Draw()
    #bw_function.Draw("SAME")
    hist.GetXaxis().SetTitle("Higgs mass in GeV")
    hist.GetYaxis().SetTitle("Number of events")
    canvas.Update()

    canvas.SaveAs("graph1.pdf")
    canvas.SaveAs("graph1.png")
    canvas.SaveAs("graph1.C")
    print("The width is",gamma)


if __name__ == "__main__":
    drawgraph()
