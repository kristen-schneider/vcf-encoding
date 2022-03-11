def main():
    f = '../vertical-allele-data/E2-6S-5V.txt'
    n_vars = 5
    n_samples = 6

    row_scores = score_rows(f)
    col_scores = score_cols(f, n_vars, n_samples)
    print(row_scores, '\n', col_scores)


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
    col_counts = [0] * (n_vars*2)
    f_o = open(f, 'r');
    for line in f_o:
        A = line.strip().replace(' ', '')
        A_list = [i for i in A]
        for i in range(len(A)):
            if ( A_list[i] == '1'): col_counts[i] += 1

    col_scores = [round(i/(n_samples*2), 2) for i in col_counts]
    return col_scores


def count_ones(row):
    count = 0
    for i in row:
        if ( i == '1'): count += 1
    return count


if __name__ == "__main__":
    main()