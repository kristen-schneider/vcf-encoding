from bitarray import bitarray

def homo_ref(f, num_samples, num_variants):
    # 2 and queries, then and M/P together
    HOMO_MASK = b'00010001'
    num_bits = len(HOMO_MASK)

    bit_arr = bitarray()
    with open(f, 'rb') as f_open:
        bit_arr.fromfile(f_open)
    print(bit_arr)

    # start = 0
    # end = num_bits
    # for i in range(int(len(encoded_data)/num_bits)):
    #     curr_genotype = encoded_data[start:end]
    #
    #
    #     start = end
    #     end += num_bits




def homo_alt_o(f, num_samples, num_variants):
    # 2 and queries, then and M/P together

    HOMO_ALT_O_MASK = b'00100010'

def het_alt_o(f, num_samples, num_variants):
    # 2 and queries, then or M/P together

    HET_O_MASK = b'00100010'

def het_alt_x(f, num_samples, num_variants):
    # 2 and queries, then or M/P together

    HET_X_MASK = b'01000100'


def and_bitstrings(bs1, bs2):
    bs1_and_bs2 = b''
    return bs1_and_bs2

def or_bitstrings(bs1, bs2):
    bs1_or_bs2 = b''
    return bs1_or_bs2