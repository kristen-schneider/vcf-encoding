import vcf_genotypes

vcf_file = 'data/easy.txt'
num_samples = 3
num_genotypes = 10

def main():
    # generate quick file with sample major genotypes
    vcf_genotypes.write_genotypes(vcf_file, num_samples, num_genotypes)


if __name__ == '__main__':
    main()
