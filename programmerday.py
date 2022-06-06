with open("input.txt") as fin, open("output.txt", "w") as fout:
    year = int(fin.read())
    if year % 4 == 0 | (year % 400 & year % 100 != 0):
        fout.write("13/09/")
    else:
        fout.write("12/09/")
    fout.write(str(year).zfill(4))