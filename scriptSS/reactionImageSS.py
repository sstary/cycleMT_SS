# from rdkit import Chem
# from rdkit.Chem import  Draw, AllChem
# from rdkit.Chem.Draw import IPythonConsole #Needed to show molecules
# from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions #Only needed if modifying defaults

# for i in range(1,2):
#     opts =  DrawingOptions()
#     opts.includeAtomNumbers=True
#     opts.bondLineWidth=1.0
#     with open('train278.txt','r') as f:
#         t1 = f.readlines()
#         j = 0
#         for x in range(len(t1)):
#             j =  j + 1
#             print("Index " + str(j))
#             rxn_s=str(t1[x]).replace('\n','')
#             reaction = AllChem.ReactionFromSmarts(rxn_s.split(' ')[0])
#             rimage = Draw.ReactionToImage(reaction, subImgSize=(600, 600))
#             rimage.save('reaction'+ str(j) + '.png')
#
#     f.close()


# oldf = open('train278.txt', 'r')
# train = open('train.txt', 'w')
# test = open('test.txt', 'w')
# val = open('val.txt', 'w')
#
# valList = [n for n in range(3, 278, 7)]
# testList = [n for n in range(1, 278, 7)]
# trainList = [n for n in range(0, 278)]
#
# for n in (testList):
#   if n in trainList:
#     trainList.remove(n)
#
# for n in (valList):
#   if n in trainList:
#     trainList.remove(n)
#
# print(len(trainList))
# print(len(valList))
# print(len(testList))
# print(trainList)
# print(valList)
# print(testList)
#
# lines = oldf.readlines()
# for i in trainList:
#     train.write(lines[i])
# for i in testList:
#     test.write(lines[i])
# for i in valList:
#     val.write(lines[i])
# oldf.close()
# train.close()
# test.close()
# val.close()

# it = 1
# with open("train.txt", 'r') as f, open("src-train.txt", 'w') as fin1, open("tgt-train.txt", "w") as fin2:
#     for line in f.readlines():
#         print(it)
#         r = line.split('>>')[0]
#         p = line.split('>>')[1]
#         fin1.write(r + '\n')
#         fin2.write(p)
#         it = it + 1
#
# f.close()
# fin1.close()
# fin2.close()
#
# it = 1
# with open("val.txt", 'r') as f, open("src-val.txt", 'w') as fin1, open("tgt-val.txt", "w") as fin2:
#     for line in f.readlines():
#         print(it)
#         r = line.split('>>')[0]
#         p = line.split('>>')[1]
#         fin1.write(r + '\n')
#         fin2.write(p)
#         it = it + 1
#
# f.close()
# fin1.close()
# fin2.close()
#
# it = 1
# with open("test.txt", 'r') as f, open("src-test.txt", 'w') as fin1, open("tgt-test.txt", "w") as fin2:
#     for line in f.readlines():
#         print(it)
#         r = line.split('>>')[0]
#         p = line.split('>>')[1]
#         fin1.write(r + '\n')
#         fin2.write(p)
#         it = it + 1
#
# f.close()
# fin1.close()
# fin2.close()


# from rdkit import Chem
# smi = 'CC2=CC=C(C(C)=C)C=C2'
# random_equivalent_smiles = Chem.MolToSmiles(Chem.MolFromSmiles(smi), doRandom=True)
# print(random_equivalent_smiles)



#------------augm----------------------------------

from rdkit import Chem

it = 1
out1 = []
out2 = []
with open("train.txt", 'r') as f, open("src-train0.txt", 'w') as fin1, open("tgt-train0.txt", "w") as fin2:
    for line in f.readlines():
        print(it)
        r = line.split('>>')[0]
        r1 = r.split('.')[0]
        r1 = Chem.MolToSmiles(Chem.MolFromSmiles(r1), doRandom=True)

        r2 = r.split('.')[1]
        r2 = Chem.MolToSmiles(Chem.MolFromSmiles(r2), doRandom=True)
        r12 = r1 + '.' + r2 + '\n'
        out1.append(r12)


        p = line.split('>>')[1]
        out2.append(Chem.MolToSmiles(Chem.MolFromSmiles(p), doRandom=True) + '\n')

        fin1.write(r + '\n')
        fin2.write(p)
        it = it + 1
    fin1.writelines(out1)
    fin2.writelines(out2)

f.close()
fin1.close()
fin2.close()
out1.clear()
out2.clear()

with open("val.txt", 'r') as f, open("src-val0.txt", 'w') as fin1, open("tgt-val0.txt", "w") as fin2:
    for line in f.readlines():
        print(it)
        r = line.split('>>')[0]
        p = line.split('>>')[1]

        fin1.write(r + '\n')
        fin2.write(p)
        it = it + 1

f.close()
fin1.close()
fin2.close()

with open("test.txt", 'r') as f, open("src-test0.txt", 'w') as fin1, open("tgt-test0.txt", "w") as fin2:
    for line in f.readlines():
        print(it)
        r = line.split('>>')[0]
        p = line.split('>>')[1]

        fin1.write(r + '\n')
        fin2.write(p)
        it = it + 1


f.close()
fin1.close()
fin2.close()

