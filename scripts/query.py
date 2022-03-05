import query_options

m_file = '../out/maternal.txt'
p_file = '../out/paternal.txt'
o_file = '../out/out.txt'
num_samples = 4
num_variants = 10

def main():
    full_bitarray = get_bit_array_from_file(o_file)
    maternal_bitarray = get_bit_array_from_file(m_file)
    paternal_bitarray = get_bit_array_from_file(p_file)

    query_options.homozygous_ref(full_bitarray, num_samples, num_variants)


def get_bit_array_from_file(f):
    with open(f, 'rb') as f_open:
        bitstring = f_open.read()
    return bitstring

if __name__ == '__main__':
    main()