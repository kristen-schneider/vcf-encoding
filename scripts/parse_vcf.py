import one_hot_genotypes
import one_hot_genotypes
import packed_genotypes
import one_hot_alleles
import packed_alleles
import encoding5
import encoding6

def parse_file(in_file, m_file, p_file, o_file):
    vcf_f = open(in_file, 'r')
    m_f = open(m_file, 'wb')
    p_f = open(p_file, 'wb')
    o_f = open(o_file, 'wb')

    for sample in vcf_f:
        sample_genotype = b''
        sample_list = sample.strip().split()
        for phased_g in sample_list:
            # encoding1
            encoded_genotype = one_hot_genotypes.encode_genotype(phased_g)
            # encoding2
            # encoding3
            # encoding4
            # encoding5
            # encoding6

            # mg = phased_g.split('|')[0]
            # pg = phased_g.split('|')[1]
            #
            # m_encoded_g = encoding1.encode_genotype(mg)
            # p_encoded_g = encoding1.encode_genotype(pg)
            #
            # # individual m/p files
            # m_f.write(m_encoded_g)
            # p_f.write(p_encoded_g)

            # one out file
            # full_encoded_g =
            o_f.write(encoded_genotype+b'\n')

