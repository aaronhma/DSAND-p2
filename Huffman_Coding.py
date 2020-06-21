import sys


def huffman_encoding(data):
    huff_data = {}

    for i in data:
        huff_data[i] = huff_data.get(i, 0) + 1

    my_Tree = {}

    value = '1'
    for i in sorted(huff_data.items(), key=lambda i: i[1]):
        my_Tree[i[0]] = value
        value = '0' + value

    encoded_data = ""
    for i in data:
        encoded_data += my_Tree[i]

    return encoded_data, my_Tree


def huffman_decoding(data, tree):
    huff_data = {}

    for i in tree:
        huff_data[tree[i]] = i

    value = ""
    decoded = ""

    for i in data:
        if i == '1':
            decoded += huff_data[value + i]
            value = ''
        else:
            value += i

    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
