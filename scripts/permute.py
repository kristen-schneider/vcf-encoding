f = '../data/vertical-allele-3.txt'

def main():
    score_rows(f)


def score_rows(f):
    f_o = open(f, 'r');
    for line in f_o:
        A = line.strip().split(' ')
        print(A)

if __name__ == "__main__":
    main()