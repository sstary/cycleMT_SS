# with open('tgt-test.txt', 'r') as f, open('test.txt',"w") as fin:
#     for line in f.readlines():
#         p = line.replace(' ', '')
#         fin.write(p)
# f.close()
# fin.close()

# list = [500000]
# for n in list:
#     with open('predictions_MIT_mixed_augm_model_step_' + str(n) + '.txt', 'r') as f, open('pre_no_space' + str(n) + '.txt', "w") as fin:
#         for line in f.readlines():
#             p = line.replace(' ', '')
#             fin.write(p)
#     f.close()
#     fin.close()
#
# it = 1
# for n in list:
#     hit = 0
#     with open('test.txt', 'r') as f1, open('pre_no_space' + str(n) + '.txt', 'r') as f2, open('no_hit50W', 'w') as f3:
#         truth = f1.readlines()
#         pre = f2.readlines()
#         for m in truth:
#             if m in pre:
#                 hit = hit + 1
#             else:
#                 f3.write(str(it) + '\n')
#             it = it + 1
#         print(len(pre))
#         print(str(n) + ' epoch Top-1 hit num: ' + str(hit) + ' ,hit rate ' + str(hit / len(pre) * 100))
#     f1.close()
#     f2.close()
#
# list = [150000]
# for n in list:
#     with open('predictions_MIT_mixed_augm_model_step_' + str(n) + '.txt', 'r') as f, open('pre_no_space' + str(n) + '.txt', "w") as fin:
#         for line in f.readlines():
#             p = line.replace(' ', '')
#             fin.write(p)
#     f.close()
#     fin.close()
#
# it = 1
# for n in list:
#     hit = 0
#     with open('test.txt', 'r') as f1, open('pre_no_space' + str(n) + '.txt', 'r') as f2, open('no_hit15W', 'w') as f3:
#         truth = f1.readlines()
#         pre = f2.readlines()
#         for m in truth:
#             if m in pre:
#                 hit = hit + 1
#             else:
#                 f3.write(str(it) + '\n')
#             it = it + 1
#         print(len(pre))
#         print(str(n) + ' epoch Top-1 hit num: ' + str(hit) + ' ,hit rate ' + str(hit / len(pre) * 100))
#     f1.close()
#     f2.close()

# cal hit rate of different num of reaction key-pair
list = [0, 1, 2, 3, 4, 5]
for n in list:
    hit = 0
    with open('no_hit50W', 'r') as f1, open('t' + str(n), 'r') as f2:
        truth = f1.readlines()
        pre = f2.readlines()
        for m in pre:
            if m in truth:
                hit = hit + 1
        print('no-hit num: ' + str(hit) + ' ,r length: ' + str(len(pre)) + ' ,hit rate ' + str((len(pre) - hit) / len(pre) * 100))
    f1.close()
    f2.close()

for n in list:
    hit = 0
    with open('no_hit15W', 'r') as f1, open('t' + str(n), 'r') as f2:
        truth = f1.readlines()
        pre = f2.readlines()
        for m in pre:
            if m in truth:
                hit = hit + 1
        print('no-hit num: ' + str(hit) + ' ,r length: ' + str(len(pre)) + ' ,hit rate ' + str((len(pre) - hit) / len(pre) * 100))
    f1.close()
    f2.close()


# hit = 0
# with open('50-tgt-test.txt', 'r') as f1, open('retro_test.txt', 'r') as f2:
#     truth = f1.readlines()
#     pre = f2.readlines()
#     for m in truth:
#         if m in pre:
#             hit = hit + 1
#     print(len(truth))
#     print('str(n) + ' 'epoch Top-1 hit num: ' + str(hit) + ' ,hit rate ' + str(hit / len(truth) * 100))
# f1.close()
# f2.close()