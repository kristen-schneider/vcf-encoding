import generate_sample_major
import parse_vcf

vcf_file = 'data/homoRef.txt'
#vcf_file = 'data/hetRefAltX.txt'
# num_samples = 4
# num_variants = 10

m_file = 'out/maternal.txt'
p_file = 'out/paternal.txt'
# o_file = 'out/out.txt'

def main():
    # generate quick file with sample major genotypes
    #generate_sample_major.write_genotypes(vcf_file, num_samples, num_variants)

    # parse vcf file and encode genotypes
    parse_vcf.parse_file(vcf_file, 1, 'out/one-hot-genotypes.txt')
    parse_vcf.parse_file(vcf_file, 2, 'out/packed-genotypes.txt')
    parse_vcf.parse_file(vcf_file, 3, 'out/one-hot-allele-maternal.txt')
    parse_vcf.parse_file(vcf_file, 4, 'out/one-hot-allele-paternal.txt')
    parse_vcf.parse_file(vcf_file, 5, 'out/one-hot-allele-both.txt')
    parse_vcf.parse_file(vcf_file, 6, 'out/packed-allele-maternal.txt')
    parse_vcf.parse_file(vcf_file, 7, 'out/packed-allele-paternal.txt')
    parse_vcf.parse_file(vcf_file, 8, 'out/packed-allele-both.txt')



if __name__ == '__main__':
    main()
