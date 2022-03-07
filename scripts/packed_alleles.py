def encode_genotype(genotype):
    encoded_genotype = b''
    if genotype == str(0):
        encoded_genotype = b'00001'
    elif genotype == str(1):
        encoded_genotype = b'00010'
    elif genotype == str(2):
        encoded_genotype = b'00100'
    elif genotype == str(3):
        encoded_genotype = b'01000'
    elif genotype == '.':
        encoded_genotype = b'10000'
    else:
        return -1
    return encoded_genotype