def and_bitstrings(bs1, bs2):
    bs1_and_bs2 = b''
    if len(bs1) != len(bs2): return -1
    else:
        for bit_i in range(len(bs1)):
            if bs1[bit_i] == bs2[bit_i] == b'1':
                bs1_and_bs2 += b'1'
            else: bs1_and_bs2 += b'0'
        return bs1_and_bs2

def or_bitstrings(bs1, bs2):
    bs1_or_bs2 = b''
    if len(bs1) != len(bs2): return -1
    else:
        for bit_i in range(len(bs1)):
            if bs1[bit_i] == b'1' or bs2[bit_i] == b'1':
                bs1_or_bs2 += b'1'
            else: bs1_or_bs2 += b'0'
        return bs1_or_bs2