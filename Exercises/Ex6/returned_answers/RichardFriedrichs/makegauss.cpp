#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <TMath.h>
#include <TRandom3.h>

void makegauss()
{
    Int_t amount = 1000;
    TFile *myfile = TFile::Open("data.root", "RECREATE");
    myfile->cd();
    TTree *datatree = new TTree("datatree", "Tree with gaussian data");
    Float_t value;
    datatree->Branch("values", &value, "values/F");
    TRandom3 RNG(123);
    for (int i = 0; i < amount; ++i)
    {
        value = RNG.Gaus(15,3);
        datatree->Fill();
    }

    datatree->Write();
    myfile->Close();
}

int main(){
    makegauss();
    return 0;
}