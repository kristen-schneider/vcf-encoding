def encode_genotype(genotype):
    one_hot_genotypes_dict = {'0|0':b'0000000000000000000000001',
    '1|1':b'0000000000000000000000010',
    '2|2':b'0000000000000000000000100',
    '3|3':b'0000000000000000000001000',
    '.|.':b'0000000000000000000010000',
    '0|1':b'0000000000000000000100000',
    '1|0':b'0000000000000000001000000',
    '0|2':b'0000000000000000010000000',
    '2|0':b'0000000000000000100000000',
    '0|3':b'0000000000000001000000000',
    '3|0':b'0000000000000010000000000',
    '0|.':b'0000000000000100000000000',
    '.|0':b'0000000000001000000000000',
    '1|2':b'0000000000010000000000000',
    '2|1':b'0000000000100000000000000',
    '1|3':b'0000000001000000000000000',
    '3|1':b'0000000010000000000000000',
    '1|.':b'0000000100000000000000000',
    '.|1':b'0000001000000000000000000',
    '2|3':b'0000010000000000000000000',
    '3|2':b'0000100000000000000000000',
    '2|.':b'0001000000000000000000000',
    '.|2':b'0010000000000000000000000',
    '3|.':b'0100000000000000000000000',
    '.|3':b'1000000000000000000000000',
    }
    try: return one_hot_genotypes_dict[genotype]
    except KeyError: return -1