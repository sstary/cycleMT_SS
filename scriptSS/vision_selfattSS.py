import numpy as np
import matplotlib.pyplot as plt
# # Encoder: 将权重文本按层切分
# E_emb = [n for n in range(0, 52)]
# E_tf1 = [n for n in range(52, 2 * 52)]
# E_tf2 = [n for n in range(2 * 52, 3 * 52)]
# E_tf3 = [n for n in range(3 * 52, 4 * 52)]
# E_tf4 = [n for n in range(4 * 52, 5 * 52)]
#
# with open('wei.txt', 'r') as fi, open('E_emb.txt', 'w') as fo:
#     lines = fi.readlines()
#     for i in E_emb:
#         fo.write(lines[i])
# fi.close()
# fo.close()
#
# for n in range(0, 4):
#     with open('wei.txt', 'r') as fi, open('E_tf' + str(n+1) + '.txt', 'w') as fo:
#         lines = fi.readlines()
#         if n == 0:
#             for i in E_tf1:
#                 fo.write(lines[i])
#         if n == 1:
#             for i in E_tf2:
#                 fo.write(lines[i])
#         if n == 2:
#             for i in E_tf3:
#                 fo.write(lines[i])
#         if n == 3:
#             for i in E_tf4:
#                 fo.write(lines[i])
#     fi.close()
#     fo.close()

# Encoder: 将权重文本按反应式切分
# r1 = [n for n in range(0, 26)]
# r1.extend([n for n in range(2 * 26, 3 * 26)])
# r1.extend([n for n in range(4 * 26, 5 * 26)])
# r1.extend([n for n in range(6 * 26, 7 * 26)])
# r1.extend([n for n in range(8 * 26, 9 * 26)])
#
# r2 = list([n for n in range(26, 2 * 26)])
# r2.extend([n for n in range(3 * 26, 4 * 26)])
# r2.extend([n for n in range(5 * 26, 6 * 26)])
# r2.extend([n for n in range(7 * 26, 8 * 26)])
# r2.extend([n for n in range(9 * 26, 10 * 26)])
#
# with open('wei.txt', 'r') as fi, open('r1.txt', 'w') as fo:
#     lines = fi.readlines()
#     for i in r1:
#         fo.write(lines[i])
# fi.close()
# fo.close()
#
# with open('wei.txt', 'r') as fi, open('r2.txt', 'w') as fo:
#     lines = fi.readlines()
#     for i in r2:
#         fo.write(lines[i])
# fi.close()
# fo.close()


it = 0
layer_len = 4
head_len = 8
r_len = 0
with open('attn-ft', 'r') as fi:
    lines = fi.readlines()
    total_len = len(lines)
    r_len = int(total_len / layer_len / head_len)
    array = np.ones([layer_len, head_len, r_len, r_len])
    for line in lines:
        if '\n' != line:
            line = line.replace('tensor(', '').replace(')', '').replace('[', '').replace(']', '').replace('\n', '').replace(' ','')
            weight = line.split(',')[0: 35]
            weight = list(map(float, weight))
            layer = int(it / (head_len * r_len))
            head = int((it % (head_len * r_len)) / r_len)
            elem = ((it % (head_len * r_len)) % r_len)
            array[layer][head][elem] = np.array(weight)
        it = it + 1
fi.close()

list = [n for n in range(0, r_len)]
cmap = 'YlOrRd'
for layer in range(layer_len):
    for head in range(head_len):
        image = array[layer][head]
        plt.imshow(image, cmap=plt.get_cmap(cmap))
        plt.gca().set_xticks(list)
        plt.gca().set_xticklabels(
            ['<RX_1>', 'C', 'O', 'C', '(', '=', 'O', ')', 'C', 'C', 'C', '(', '=', 'O', ')', 'c', '1', 'c', 'c', 'c',
             '(', 'O', 'C', '2', 'C', 'C', 'C', 'C', 'O', '2', ')', 'c', 'c', '1', 'O'])
        plt.gca().set_yticks(list)
        plt.gca().set_yticklabels(
            ['<RX_1>', 'C', 'O', 'C', '(', '=', 'O', ')', 'C', 'C', 'C', '(', '=', 'O', ')', 'c', '1', 'c', 'c', 'c',
             '(', 'O', 'C', '2', 'C', 'C', 'C', 'C', 'O', '2', ')', 'c', 'c', '1', 'O'])
        plt.savefig('L' + str(layer) + '_H' + str(head))
