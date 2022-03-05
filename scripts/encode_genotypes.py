def encode_genotype(genotype):
    encoded_genotype = b''
    if genotype == str(0):
        encoded_genotype = b'0001'
    elif genotype == str(1):
        encoded_genotype = b'0010'
    elif genotype == str(2) or genotype == str(3):
        encoded_genotype = b'0100'
    elif genotype == '.':
        encoded_genotype = b'1000'
    else:
        return -1
    return encoded_genotype