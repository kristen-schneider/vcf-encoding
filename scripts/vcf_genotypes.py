import random

def write_genotypes(vcf_file, num_samples, num_genotypes):
    vcf = open(vcf_file, 'w')

    for s in range(num_samples):
        sample_genotype = generate_genotypes(num_genotypes)
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