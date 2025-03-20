br.input is supposed to be the input file for HDecay. It does the range 115 to 135 in increments of 0.2.
br.sm2 is the output of HDecay.
Make sure drawgraph.py has access to it, i.e. move br.sm2 to the same folder.

givefeyndata.cc needs access to FeynHiggs, i.e. move it to the Feynhiggs***/examples/ folder and run there. It will give output data.dat.
Make sure drawgraph2.py has access to both br.sm2 and data.dat, i.e. put them in the same folder.