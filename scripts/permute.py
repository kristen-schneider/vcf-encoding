import matplotlib.pyplot as plt

def main():
    f = '../vertical-allele-data/E2-100S-1000V.txt'
    n_samples = 100
    n_vars = 1000

    row_scores = score_rows(f)
    col_scores = score_cols(f, n_vars, n_samples)
    plot_distribution(row_scores, col_scores)

def score_rows(f):
    row_scores = []
    f_o = open(f, 'r');
    for line in f_o:
        A = line.strip().replace(' ', '')
        num_ones_in_row = count_ones(A)
        score = num_ones_in_row/len(A)
        row_scores.append(score)
    return row_scores


def score_cols(f, n_vars, n_samples):
    col_counts = [0] * (n_samples * 2)
    f_o = open(f, 'r');
    for line in f_o:
        A = line.strip().replace(' ', '')
        A_list = [i for i in A]
        for i in range(len(A)):
            if ( A_list[i] == '1'): col_counts[i] += 1

    col_scores = [round(i/(n_vars*2), 6) for i in col_counts]
    return col_scores


def count_ones(row):
    count = 0
    for i in row:
        if ( i == '1'): count += 1
    return count

def plot_distribution(row_scores, col_scores):
    plt.hist(row_scores, bins=10, color='blue')
    plt.hist(col_scores, bins=10, color='red')
    plt.savefig('../plots/row_scores.png')


if __name__ == "__main__":
    main()