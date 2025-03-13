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
            line = line.strip().split()
            xvalues2.append(float(line[0]))
            yvalues2.append(float(line[-1]))


    n_points = len(xvalues1)

    graph = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph.SetPoint(i, xvalues1[i], yvalues1[i])

    canvas = ROOT.TCanvas("canvas", "Higgs decay width as function mass comparison", 1200, 600)
    canvas.SetFillColor(ROOT.kWhite)

    graph.SetLineColor(ROOT.kBlue)
    graph.SetLineWidth(2)
    graph.Draw("AL")

    graph2 = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph2.SetPoint(i, xvalues2[i], yvalues2[i])
    graph2.SetLineColor(ROOT.kRed)
    graph2.SetLineWidth(2)
    graph2.Draw("SAME")



    scaler =     (graph.GetYaxis().GetXmax() +    graph.GetYaxis().GetXmin())/2


    graph3 = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph3.SetPoint(i, xvalues2[i], yvalues2[i]/yvalues1[-i-1]*scaler)
    graph3.SetLineColor(ROOT.kGreen)
    graph3.SetLineWidth(2)
    graph3.Draw("SAME")

    axis = ROOT.TGaxis(
        graph.GetXaxis().GetXmax(), 
        graph3.GetYaxis().GetXmin(),  
        graph.GetXaxis().GetXmax(),  
        graph3.GetYaxis().GetXmax(),  
        graph3.GetYaxis().GetXmin()/scaler,
        graph3.GetYaxis().GetXmax()/scaler,                
        510,                          
        "#0"                          
    )
    axis.SetLineColor(ROOT.kGreen)  
    axis.SetLabelColor(ROOT.kGreen)  
    axis.Draw()                   



    graph.GetXaxis().SetTitle("Higgs mass in GeV")
    graph.GetYaxis().SetTitle("Higgs decay width")

    legend = ROOT.TLegend(0, 0, 0, 0) 
    legend.AddEntry(graph, "HDecay", "l")  
    legend.AddEntry(graph2, "FeynHiggs", "l")  
    legend.AddEntry(graph3, "FeynHiggs/HDecay", "l")
    legend.Draw()



    canvas.Update()

    canvas.SaveAs("graph2.pdf")
    canvas.SaveAs("graph2.png")
    canvas.SaveAs("graph2.C")


if __name__ == "__main__":
    drawgraph()
