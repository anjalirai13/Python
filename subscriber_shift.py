alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cipher_shift(decoded_text, cipher_key):
    cipher_dict = {" ": " "}
    final_string = ""
    for i in range(len(cipher_key)):
        cipher_dict[cipher_key[i]] = alphabets[i]
    for j in decoded_text:
        final_string += cipher_dict[j]
    return final_string


decoded_string_arr = ["BWGTG PNGQG TGPGV GQBMD NGDNM RGTNGM", "WGUNU NNZMG ANWZY UQYZHHTE", "ZRQXY DRONX MMOEH QYYOE NFPQE UQGMEOYY",
                      "ZCZMR BVEKZ NTEAE MRCEQ VXURE EYXPZ GEKZN TQRXQGR", "BTOKM HIBTO XWWMI SKQYC DYNMS TGKIM TZTLM MISKZ LTEMIEK"]
key_arr = ["GHFDYSINMPRLQVEOZTBAUCWXJK", "AKMQECVGUIXTBFLYRJNWZPSDOH", "JNUAOCMRXFTHSGQPIEYDVLZBWK", "ZWNHRUSKYLTGCPXQJVEMBFDOAI",
           "TCEDKOAVIQGWSNYZULBMXJFRHP"]

for x in range(len(decoded_string_arr)):
    print(cipher_shift(decoded_string_arr[x], key_arr[x]))
