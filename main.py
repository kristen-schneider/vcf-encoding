# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random

def main():
    vcf = open('./data/easy.vcf', 'w')

    num_samples = 3

    for s in range(num_samples):
        sample_genotype = generate_genotypes(10)
        for sg in sample_genotype:
            vcf.write(sg)
            vcf.write('\t')
        vcf.write('\n')
        print(sample_genotype)

def generate_genotypes(num_genotypes):
    # ref, primary alternate, secondary alternate, tertiary alternate, unknown
    options = [0, 1, 2, 3, '.']
    all_genotypes = []

    for g in range(num_genotypes):
        genotype = ''
        maternal_allele = random.choice(options)
        paternal_allele = random.choice(options)
        genotype = str(maternal_allele) + '|' + str(paternal_allele)
        all_genotypes.append(genotype)

    return all_genotypes


if __name__ == '__main__':
    main()
