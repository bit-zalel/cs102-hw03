import sys
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

  

    f = open(input_file_path,"r")
    values = value = f.read()
    values = values.split("\n")

    for val in values:
        strvals = val.split(",")
        numvals = []
        for nv in strvals:
            if nv.isnumeric():
                numvals.append(float(nv))
        if numvals != []:
            print(mean(numvals))




    value.split("\n")


if __name__ == "__main__":
    main()
