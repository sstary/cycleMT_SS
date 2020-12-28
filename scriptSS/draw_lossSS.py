import matplotlib.pyplot as plt
import numpy as np

# with open("out", 'r') as f, open("acc", "w") as fin:
#     lines = f.readlines()
#     for line in lines:
#         if 'acc:' in line:
#             fin.write(line)
#
# f.close()
# fin.close()
#
fig_M = 355
fig_Word = np.zeros([fig_M])
fig_Topo = np.zeros([fig_M])
fig_Assm = np.zeros([fig_M])
it = 0

with open("acc", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace(';', '')
        acc = float(line.split(' ')[7])
        ppl = float(line.split(' ')[10])
        lr = float(line.split(' ')[14])

        fig_Word[it] = acc
        fig_Topo[it] = ppl
        fig_Assm[it] = lr

        it = it + 1
f.close()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax3 = ax1.twinx()

lns1 = ax1.plot(np.arange(fig_M), fig_Word, label="acc", color='r')
lns2 = ax2.plot(np.arange(fig_M), fig_Topo, label="ppl", color='b')
lns3 = ax3.plot(np.arange(fig_M), fig_Assm, label="lr")

ax1.set_xlabel('iteration')
ax1.set_ylabel('acc')
ax2.set_ylabel('ppl')
ax3.set_ylabel('lr')

lns = lns1 + lns2 + lns3
labels = ["acc", "ppl", "lr"]
plt.legend(lns, labels, loc=7)
plt.show()


# with open("out", 'r') as f, open("accuracy", "w") as fin:
#     lines = f.readlines()
#     for line in lines:
#         if 'accuracy:' in line:
#             fin.write(line)
#
# f.close()
# fin.close()
#
# fig_M = 35
# fig_Word = np.zeros([fig_M])
# it = 0
#
# with open("accuracy", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.replace('\n', '').split(' ')
#         acc = float(line[5])
#
#         fig_Word[it] = acc
#
#         it = it + 1
# f.close()
#
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax3 = ax1.twinx()
#
# lns1 = ax1.plot(np.arange(fig_M), fig_Word, label="acc", color='r')
#
# ax1.set_xlabel('iteration')
# ax1.set_ylabel('acc')
#
# lns = lns1
# labels = ["acc"]
# plt.legend(lns, labels, loc=7)
# plt.show()