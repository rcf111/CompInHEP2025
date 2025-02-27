import ROOT

ROOT.gROOT.SetBatch(True)

def drawgraph():
    file = ROOT.TFile.Open("data2.root")
    tree = file.Get("datatree")
    hist = ROOT.TH1F("hist", "Data", 100, 5, 25)

    for entry in tree:
        hist.Fill(entry.values[0])

    canvas = ROOT.TCanvas("canvas", "Histogram with Fit", 800, 600)
    canvas.SetFillColor(ROOT.kWhite)
    tree.Draw("values>>hist")
    hist.SetFillColor(ROOT.kYellow)
    hist.SetLineColor(ROOT.kBlack)
    hist.SetLineWidth(3)
    hist.Draw()

    hist.GetXaxis().SetTitle("Number")
    hist.GetYaxis().SetTitle("Generated amount")
    hist.Fit("gaus")
    canvas.Update()

    canvas.SaveAs("gaussian2.pdf")
    canvas.SaveAs("gaussian2.png")
    canvas.SaveAs("gaussian2.C")
    file.Close()

if __name__ == "__main__":
    drawgraph()
