#include <TFile.h>
#include <TTree.h>
#include <iostream>
#include "MyAnalysis.h"
#include "MyAnalysis.C"

int main() {

    TFile *file = TFile::Open("DYJetsToLL.root");
    if (!file || file->IsZombie()) {
        std::cerr << "Failed to open file!" << std::endl;
        return 1;
    } else {
        std::cout << "File opened successfully!" << std::endl;
    }

    TTree *tree = (TTree*)file->Get("Events");
    if (!tree) {
        std::cerr << "Failed to retrieve tree 'Events'" << std::endl;
        return 1;
    } else {
        std::cout << "Tree 'Events' retrieved with " << tree->GetEntries() << " entries." << std::endl;
    }

    MyAnalysis *selector = new MyAnalysis();

 
    tree->Process(selector);


    delete selector;
    file->Close();

    return 0;
}
