def smi_tokenizer(smi):
    """
    Tokenize a SMILES molecule or reaction
    """
    import re
    pattern =  "(\[[^\]]+]|Br?|Cl?|N|O|S|P|F|I|b|c|n|o|s|p|\(|\)|\.|=|#|-|\+|\\\\|\/|:|~|@|\?|>|\*|\$|\%[0-9]{2}|[0-9])"
    regex = re.compile(pattern)
    # print(regex)
    print(regex.findall(smi))
    tokens = [token for token in regex.findall(smi)]
    # print(tokens)
    print(smi)
    print(''.join(tokens))
    tt = ''.join(tokens) + '\n'
    assert smi == tt
    return ' '.join(tokens)

# smi = 'Cc1cc(Cl)n(C)n1.O=[N+]([O-])O>O=S(=O)(O)O>Cc1nn(C)c(Cl)c1[N+](=O)[O-]'
# smi_t = smi_tokenizer(smi)
# print(smi_t)

list = ['train', 'val', 'test']
for x in list:
    with open('src-' + x + "0.txt", 'r') as f, open('src-' + x + ".txt", 'w') as fin:
        for line in f.readlines():
            r_token = smi_tokenizer(line)
            fin.write(r_token + '\n')
    f.close()
    with open('tgt-' + x + "0.txt", 'r') as f, open('tgt-' + x + ".txt", 'w') as fin:
        for line in f.readlines():
            r_token = smi_tokenizer(line)
            fin.write(r_token + '\n')
    f.close()