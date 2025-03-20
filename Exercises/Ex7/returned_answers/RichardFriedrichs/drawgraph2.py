import ROOT

ROOT.gROOT.SetBatch(True)

def drawgraph():

    xvalues1 = []
    yvalues1 = []
    with open('br.sm2', 'r') as file:
        skip=0
        for line in file:
            skip+=1
            if skip  >=4:
                line = line.strip().split()
                xvalues1.append(float(line[0]))
                yvalues1.append(float(line[-1]))

    xvalues2 = []
    yvalues2 = []
    with open('data.dat', 'r') as file:
        skip=0
        for line in file:
            if line== "\n": break
            line = line.strip().split()
            xvalues2.append(float(line[0]))
            yvalues2.append(float(line[-1]))


    n_points = len(xvalues1)

    graph = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph.SetPoint(i, xvalues1[i], yvalues1[i])

    canvas = ROOT.TCanvas("canvas", "Higgs decay width as function mass comparison", 1200, 800)
    canvas.SetFillColor(ROOT.kWhite)

    pad1 = ROOT.TPad("pad1", "pad1", 0.0, 0.25, 1.0, 1.0)
    pad1.SetBottomMargin(0.03)  # Space between the two plots
    pad1.Draw()

    pad2 = ROOT.TPad("pad2", "pad2", 0.0, 0.0, 1.0, 0.25)
    pad2.SetTopMargin(0.03)  # Small margin between the plots
    pad2.SetBottomMargin(0.3)
    pad2.Draw()

    pad1.cd()

    graph.SetLineColor(ROOT.kBlue)
    graph.SetLineWidth(2)
    graph.Draw("AL")

    graph2 = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph2.SetPoint(i, xvalues2[i], yvalues2[i])
    graph2.SetLineColor(ROOT.kRed)
    graph2.SetLineWidth(2)
    graph2.Draw("SAME")


            

    graph.GetXaxis().SetTitle("Higgs mass in GeV")
    graph.GetYaxis().SetTitle("Higgs decay width")

    legend = ROOT.TLegend(0.6, 0.7, 0.9, 0.9) 
    legend.AddEntry(graph, "HDecay", "l")  
    legend.AddEntry(graph2, "FeynHiggs", "l")  
    legend.Draw()

    pad2.cd()

    ratio_graph = ROOT.TGraph(n_points)

    for i in range(n_points):
        ratio_graph.SetPoint(i, xvalues2[i], yvalues2[i] / yvalues1[-i-1])
    ratio_graph.SetLineColor(ROOT.kGreen)
    ratio_graph.SetLineWidth(2)
    ratio_graph.SetTitle("Ratio")
    ratio_graph.GetXaxis().SetTitle("Higgs mass in GeV")
    ratio_graph.GetYaxis().SetTitle("Ratio (FeynHiggs/HDecay)")

    ratio_graph.Draw("AL")

    pad1.SetBottomMargin(0.1)  
    pad2.SetTopMargin(0.1)     


    ratio_graph.GetXaxis().SetTitleSize(0.1)  
    ratio_graph.GetYaxis().SetTitleSize(0.1) 
    ratio_graph.GetXaxis().SetLabelSize(0.1) 
    ratio_graph.GetYaxis().SetLabelSize(0.1) 

    ratio_graph.GetXaxis().SetTitleFont(42)
    ratio_graph.GetYaxis().SetTitleFont(42)

    ratio_graph.GetXaxis().SetLabelFont(42)
    ratio_graph.GetYaxis().SetLabelFont(42)




    canvas.Update()

    canvas.SaveAs("graph2.pdf")
    canvas.SaveAs("graph2.png")
    canvas.SaveAs("graph2.C")


if __name__ == "__main__":
    drawgraph()
