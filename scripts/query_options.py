import bitwise_operations

def homozygous_ref(f_bit_array, num_samples, num_variants):

    # 2 and queries
    HOMOZYGOUS_MASK = b'00010001'
    num_bits = len(HOMOZYGOUS_MASK)
    fulL_mask = HOMOZYGOUS_MASK * (num_samples * num_variants)
    mask_and_full = bitwise_operations.and_bitstrings(f_bit_array, fulL_mask)
    print(mask_and_full)


def homo_alt_o(f, num_samples, num_variants):
    # 2 and queries, then and M/P together

    HOMO_ALT_O_MASK = b'00100010'

def het_alt_o(f, num_samples, num_variants):
    # 2 and queries, then or M/P together

    HET_O_MASK = b'00100010'

def het_alt_x(f, num_samples, num_variants):
    # 2 and queries, then or M/P together

    HET_X_MASK = b'01000100'
