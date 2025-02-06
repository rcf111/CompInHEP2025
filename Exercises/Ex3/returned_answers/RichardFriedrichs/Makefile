SRCS = $(wildcard src/*.cpp)
OBJS = $(SRCS:.cpp=.o)

OPT = -O -Wall -fPIC
INC = -Iinc
LIBS = -L. -lMyLib  

all: test

test: test.cpp libMyLib.so
	$(CXX) test.cpp $(INC) -L. -lMyLib -o test

libMyLib.so: $(OBJS)
	$(CXX) -shared -O $(OBJS) -o libMyLib.so

.cpp.o:
	$(CXX) -c $(OPT) $(INC) $< -o $@

clean:
	rm -f *~ $(OBJS)

cleanAll: clean
	rm -f test libMyLib.so
