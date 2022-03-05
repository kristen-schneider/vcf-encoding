import generate_sample_major
import parse_vcf
import query_full

vcf_file = 'data/easy.txt'
num_samples = 3
num_variants = 10

m_file = 'out/maternal.txt'
p_file = 'out/paternal.txt'
o_file = 'out/out.txt'

def main():
    # generate quick file with sample major genotypes
    #generate_sample_major.write_genotypes(vcf_file, num_samples, num_variants)

    # parse vcf file and encode genotypes
    #parse_vcf.parse_file(vcf_file, m_file, p_file, o_file)

    # query
    query_full.homo_ref(o_file, num_samples, num_variants)



if __name__ == '__main__':
    main()
