import one_hot_genotypes
import packed_genotypes
import one_hot_alleles
import packed_alleles


def parse_file(in_file, encoding_type, o_file):
    vcf_f = open(in_file, 'r')
    o_f = open(o_file, 'wb')

    for sample in vcf_f:
        sample_genotype = b''
        sample_list = sample.strip().split()
        for phased_g in sample_list:
            # encoding1
            if(encoding_type == 1):
                encoded_genotype = one_hot_genotypes.encode_genotype(phased_g)
                o_f.write(encoded_genotype+b'\n')
            elif(encoding_type == 2):
                encoded_genotype = packed_genotypes.encode_genotype(phased_g)
                o_f.write(encoded_genotype + b'\n')
            elif (encoding_type == 3):
                m = phased_g.split('|')[0]
                encoded_genotype = one_hot_alleles.encode_genotype(m)
                o_f.write(encoded_genotype + b'\n')
            elif (encoding_type == 4):
                p = phased_g.split('|')[1]
                encoded_genotype = one_hot_alleles.encode_genotype(p)
                o_f.write(encoded_genotype + b'\n')
            elif (encoding_type == 5):
                m = phased_g.split('|')[0]
                p = phased_g.split('|')[1]
                encoded_genotype_m = one_hot_alleles.encode_genotype(m)
                encoded_genotype_p = one_hot_alleles.encode_genotype(p)
                o_f.write(encoded_genotype_m + encoded_genotype_p + b'\n')
            elif (encoding_type == 6):
                m = phased_g.split('|')[0]
                encoded_genotype = packed_alleles.encode_genotype(m)
                o_f.write(encoded_genotype + b'\n')
            elif (encoding_type == 7):
                p = phased_g.split('|')[1]
                encoded_genotype = packed_alleles.encode_genotype(p)
                o_f.write(encoded_genotype + b'\n')
            elif (encoding_type == 8):
                m = phased_g.split('|')[0]
                p = phased_g.split('|')[1]
                encoded_genotype_m = packed_alleles.encode_genotype(m)
                encoded_genotype_p = packed_alleles.encode_genotype(p)
                o_f.write(encoded_genotype_m + encoded_genotype_p + b'\n')




