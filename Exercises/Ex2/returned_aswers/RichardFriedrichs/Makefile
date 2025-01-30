CC = g++ 
CXXFLAGS = -std=c++20
SRC = $(wildcard *.cpp)
OBJECTS = $(SRC:.cpp=.o)


EXEC = runnable

all: $(EXEC) 


$(EXEC): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXEC)

%.o: %.cpp
	$(CC) -c $(CXXFLAGS) $< -o $@



GARBAGE = $(wildcard *.o *~  *.txt *.exe)
clean:
	rm $(GARBAGE)

run: $(EXEC) 
	./$(EXEC) 0

runAll:
	bash jobs.sh
	python jobs.py