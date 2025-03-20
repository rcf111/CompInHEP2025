import ROOT

ROOT.gROOT.SetBatch(True)

def drawgraph():

    xvalues = []
    yvalues = []
    with open('br.sm2', 'r') as file:
        skip=0
        for line in file:
            skip+=1
            if skip  >=4:
                line = line.strip().split()
                xvalues.append(float(line[0]))
                yvalues.append(float(line[-1]))
                if xvalues[-1] == 125:
                    print("The decay width at 125 GeV is",yvalues[-1])

    n_points = len(xvalues)

    graph = ROOT.TGraph(n_points)

    for i in range(n_points):
        graph.SetPoint(i, xvalues[i], yvalues[i])

    canvas = ROOT.TCanvas("canvas", "Graph", 1200, 600)
    canvas.SetFillColor(ROOT.kWhite)
    graph.Draw("AP")

    graph.GetXaxis().SetTitle("Higgs mass in GeV")
    graph.GetYaxis().SetTitle("Higgs decay width")
    canvas.Update()

    canvas.SaveAs("graph1.pdf")
    canvas.SaveAs("graph1.png")
    canvas.SaveAs("graph1.C")


if __name__ == "__main__":
    drawgraph()
