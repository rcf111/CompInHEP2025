INCLUDES = -I$(ROOTSYS)/include

LIBS = $(shell root-config --glibs)

CXX = g++
CXXFLAGS = -std=c++20 -Wall -O2 $(INCLUDES)
LDFLAGS = $(LIBS)

SRC1 = makegauss.cpp
SRC2 = drawgraph.cpp
OBJECTS1 = $(SRC1:.cpp=.o)
OBJECTS2 = $(SRC2:.cpp=.o)


EXEC1 = $(basename $(SRC1))
EXEC2 = $(basename $(SRC2))

all: $(EXEC1) $(EXEC2) 


$(EXEC1): $(SRC1)
	$(CXX) $(CXXFLAGS) $(SRC1) -o $(EXEC1) $(LDFLAGS)

$(EXEC2): $(SRC2)
	$(CXX) $(CXXFLAGS) $(SRC2) -o $(EXEC2) $(LDFLAGS)

%.o: %.cpp
	$(CC) -c $(CXXFLAGS) $< -o $@



GARBAGE = $(wildcard *.o *~  *.txt *.exe)
clean: $(GARBAGE)
	rm $(GARBAGE) $(EXEC1) $(EXEC2)

cleanAll: 
	$(MAKE) clean
	rm $(wildcard *.png *.root *.pdf *.C)

run: $(EXEC1) $(EXEC2) 
	./$(EXEC1)
	./$(EXEC2) 
