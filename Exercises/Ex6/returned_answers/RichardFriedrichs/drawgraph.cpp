#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <TMath.h>
#include <TRandom3.h>
#include <iostream>

using namespace std;

void drawgraph()
{
    TFile *file = TFile::Open("data.root");
    TTree *tree = (TTree *)file->Get("datatree");
    TH1F *hist = new TH1F("hist", "Data", 100, 5, 25);
    TCanvas *canvas = new TCanvas("canvas", "Histogram with Fit", 800, 600);
    canvas->SetFillColor(kWhite);
    tree->Draw("values>>hist");
    hist->SetFillColor(kYellow);
    hist->SetLineColor(kBlack);
    hist->SetLineWidth(3);
    hist->Draw();
    hist->GetXaxis()->SetTitle("Number");
    hist->GetYaxis()->SetTitle("Generated amount");
    hist->Fit("gaus");
    canvas->Update();
    canvas->SaveAs("gaussian.pdf");
    canvas->SaveAs("gaussian.png");
    canvas->SaveAs("gaussian.C");
    file->Close();
}

int main(){
    drawgraph();
    return 0;
}