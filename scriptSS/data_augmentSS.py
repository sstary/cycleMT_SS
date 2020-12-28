# tt = list()
# with open('train_r2-5', 'r') as fi, open('aug_2-5', 'w') as fo:
#     lines = fi.readlines()
#     for line in lines:
#         tt.append(line)
#         tt.append(str(int(line) + 409035))
#     tt = list(map(int, tt))
#     tt.sort()
#     tt = list(map(str, tt))
#     it = iter(tt)
#     for n in tt:
#         fo.write(n + '\n')
# fi.close()
# fo.close()


tt = list()

with open('aug_4-5', 'r') as f:
    lines = f.readlines()
    for n in lines:
        tt.append(int(n))

with open('src-train.txt', 'r') as fi, open('src-train45.txt', 'w') as fo:
    lines = fi.readlines()
    it = iter(tt)
    for n in it:
        fo.write(lines[n - 1])
fi.close()
fo.close()

with open('tgt-train.txt', 'r') as fi, open('tgt-train45.txt', 'w') as fo:
    lines = fi.readlines()
    it = iter(tt)
    for n in it:
        fo.write(lines[n - 1])
fi.close()
fo.close()
