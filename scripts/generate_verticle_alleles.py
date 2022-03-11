import random

def main():
    o_file = '../vertical-allele-data/E2-'
    num_samples = 6
    num_variants = 5
    all_genotypes = generate_genotypes(num_samples, num_variants)
    write_genotypes(all_genotypes, o_file, num_samples, num_variants)

def generate_genotypes(num_samples, num_variants):
    alleles = ['00', '01', '10', '11']

    full_file = []
    for v in range(num_variants):
        sample = []
        for s in range(num_samples * 2):
            two_bit_allele = [b for b in random.choice(alleles)]
            sample.append(two_bit_allele)
        full_file.append(sample)
    return full_file

def write_genotypes(all_genotypes, o_file, num_samples, num_variants):
    named_file = o_file + str(num_samples) + 'S-' + str(num_variants) + 'V.txt'
    o_file = open(named_file, 'w')

    for v in range(num_variants):
        for s in range(num_samples * 2):
            alleleA = all_genotypes[v][s][0]
            o_file.write(alleleA)
        o_file.write('\n')
        for s in range(num_samples * 2):
            alleleB = all_genotypes[v][s][1]
            o_file.write(alleleB)
        o_file.write('\n')


if __name__ == "__main__":
    main()