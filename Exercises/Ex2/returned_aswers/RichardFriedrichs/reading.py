import re
import os

totrecorder_finder_re = re.compile(r"\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\s+\|\s+\d+\.\d+\s+\|\s+(?P<totreco>\d+\.\d+)\s+\|")


dir = os.path.dirname(__file__)
file_path = os.path.join(dir, '../../../brilcalc.log')
file_path = os.path.normpath(file_path)

with open(file_path, 'r') as file:
    for line in file:
        match = totrecorder_finder_re.search(line)
        if match:
            arv = match.group("totreco")
            print(round(float(arv)/1000,1))