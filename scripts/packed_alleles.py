def encode_genotype(genotype):
    encoded_genotype = b''
    if genotype == str(0):
        encoded_genotype = b'001'
    elif genotype == str(1):
        encoded_genotype = b'010'
    elif genotype == str(2):
        encoded_genotype = b'011'
    elif genotype == str(3):
        encoded_genotype = b'100'
    elif genotype == '.':
        encoded_genotype = b'101'
    else:
        return -1
    return encoded_genotype