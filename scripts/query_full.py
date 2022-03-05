from bitarray import bitarray

def get_bit_array_from_file(f):
    bit_arr = bitarray()
    with open(f, 'rb') as f_open:
        bit_arr.fromfile(f_open)
    return bit_arr
