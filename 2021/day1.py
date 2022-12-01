import numpy as np
import sys

def analyze_depth_report(report):
    report_size = np.size(report)
    count = int(0) 
    for i in range(0, report_size - 1):
        if report[i]<report[i+1] :
            count += 1
    return count



# Defining main function
def main():
    report_file = str(sys.argv[1])
    report = np.genfromtxt(report_file, int)
    analysis = analyze_depth_report(report)
    print("Report Analysis: ", analysis)


# main
if __name__=="__main__":
    main()