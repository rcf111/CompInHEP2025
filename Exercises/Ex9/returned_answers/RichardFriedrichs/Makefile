PYTHIA8_URL = https://pythia.org/download/pythia83/pythia8313.tgz
PYTHIA8_TGZ = $(notdir $(PYTHIA8_URL))
PYTHIA8_DIR = $(basename $(PYTHIA8_TGZ))

# pythia8*

GARBAGE = $(wildcard *~ *.o *.a *.so xsec *.job *.png *.pdf *.C *.dat *.exe *.tgz)

OPT = -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC
INC = -I$(PYTHIA8_DIR)/include
LIBS = -L$(PYTHIA8_DIR)/lib -lpythia8 -ldl

OBJ = $(addsuffix .o,$(basename $(wildcard *.cpp)))

all:
	$(MAKE) p8get
	$(MAKE) compile
	$(MAKE) makedata
	$(MAKE) job
	./test.job

p8get:
	wget $(PYTHIA8_URL) && tar xfvz $(PYTHIA8_TGZ) && cd $(PYTHIA8_DIR) && ./configure && make

.cpp.o:
	$(CXX) $(OPT) $(INC) -c $^ -o $@



compile: $(OBJ)


makedata:	$(OBJ)
	$(CXX) $(OPT) $(INC) $@.o $(LIBS) -o makedata

job:
	echo '#!'`which bash` > test.job 
	echo 'export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH):$(PYTHIA8_DIR)/lib' >> test.job
	echo 'export PYTHIA8DATA=$(PWD)/pythia8313/share/Pythia8/xmldoc' >> test.job
	echo './makedata' >> test.job
	echo 'python3 drawgraph.py' >> test.job
	chmod +x test.job

clean:
	rm -rf $(GARBAGE)

