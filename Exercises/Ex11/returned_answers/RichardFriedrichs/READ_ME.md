commands: 
make
g++ main.cpp -L. -lMyAnalysis $(root-config --cflags) $(root-config --glibs) -o my_program
./my_program

Beforehand make sure that all the files are in the same folder. The result should be a .png file.

The "dummydata.py" is what I used to create some dummy data for testing, since I couldn't get my hands on the real data. BEWARE! Running dummydata.py can override the real data, if you have it, since it "recreate"-s into a root file of the same name!
The picture included in the submission was created with the dummy data: A gauss(0,20) (rounded into integers) with a trigger of "true" for all values below 10. The trigger and data are in the corresponding branches like they would be for the real data file (although the values themselves are nonsensical).