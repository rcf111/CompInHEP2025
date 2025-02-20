void drawgraph()
{
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("datatree");
    TH1F *hist = new TH1F("hist", "Data", 100, 5, 25);
    TCanvas *canvas = new TCanvas("canvas", "Histogram with Fit", 800, 600);
    tree->Draw("values>>hist");
    hist->SetFillColor(kYellow);
    hist->SetLineColor(kBlack);
    hist->SetLineWidth(3);
    hist->Draw();
    hist->GetXaxis()->SetTitle("Number");
    hist->GetYaxis()->SetTitle("Generated amount");
    hist->Fit("gaus");
    canvas->Update();
}
