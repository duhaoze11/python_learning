# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx

g1 = nx.Graph()
file_object = open('g2.txt', 'r')
write_file = open('g2out.txt', 'w+')
for line in file_object:
    temp = line.split(' ')
    p = int(temp[0])
    q = int(temp[1])
    g1.add_nodes_from([p, q])
    g1.add_edge(p, q)
nodes = g1.nodes()
edges = g1.edges()
edges.sort()
flag = list(range(10000))
used = list(range(10000))

def init() :
    for x in range(10000):
        xx = int(x)
        i = xx % 10
        if i >= 0 and i <= 3:
            flag[xx] = 1
            used[xx] = True
        elif i >= 4 and i <= 7:
            flag[xx] = 2
            used[xx] = True
        elif i >= 8 and i <= 9:
            flag[xx] = 0
            used[xx] = False

swp = 1  # 摇摆变量
A = 0  #votes to A
B = 0  #votes to B

def deci(pt) :
    global swp
    global A, B
    for i in range(10):  # iteration
        for j in nodes:  # process every non-determined nodes
            if used[j] == False :
                neighbors = g1.neighbors(j)
                A = 0
                B = 0
                for k in neighbors:
                    if flag[k] == 1:
                        A += 1
                    elif flag[k] == 2:
                        B += 1
                if A > B:
                    flag[j] = 1
                elif A < B:
                    flag[j] = 2
                elif A == B:
                    if swp == 1:
                        flag[j] = 1
                        swp = 2
                    elif swp == 2:
                        flag[j] = 2
                        swp = 1
    A = 0
    B = 0
    for i in nodes:
        if flag[i] == 1:
            A += 1
        elif flag[i] == 2:
            B += 1
    if A > B:
        write_file.write('candidate A wins and gets %d votes\n' % A)
    elif A < B:
        write_file.write('candidate B wins and gets %d votes\n' % B)


def proc1_2() :
    global A, B, A1_1
    log = [] #record the votes
    A = 0
    B = 0
    k = 1000
    while k <= 9000 :
        init()
        i = k
        pt = 3000
        while i >= 1000 :
            j = 0
            while j <= 9 :
                flag[pt] = 1
                used[pt] = True
                pt += 1
                j += 1
            i -= 1000
        deci(pt)
        log.append((k, A - A1_1))
        k += 1000
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([k for (k, A) in log], [A for (k, A) in log])
    ax.set_xscale('linear')
    ax.set_yscale('linear')
    ax.set_xlabel('Funds')
    ax.set_ylabel('Won Votes')
    plt.title("Project 1_2: With the influence of Ads")
    fig.savefig('Project 1_2g2.png')
    for i in log :
        write_file.write("%d %d\n" % (i[0], i[1]))

def proc1_3() :
    global A, B, A1_1
    log = [] #record the votes
    A = 0
    B = 0
    k = 1000
    D = g1.degree()
    while k <= 9000 :
        init()
        i = k
        tD = D
        maxD = 0
        maxDP = -1
        while i >= 1000 :
            for j in tD :
                temp = tD[j]
                if temp > maxD :
                    maxD = temp
                    maxDP = j
            flag[maxDP] = 1
            used[maxDP] = True
            tD[maxDP] = 0
            i -= 1000
        deci(0)
        log.append((k, A - A1_1))
        k += 1000
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([k for (k, A) in log], [A for (k, A) in log])
    ax.set_xscale('linear')
    ax.set_yscale('linear')
    ax.set_xlabel('Funds')
    ax.set_ylabel('Won Votes')
    plt.title("Project 1_3: With the influence of Diners")
    fig.savefig('Project 1_3g2.png')
    for i in log :
        write_file.write("%d %d\n" % (i[0], i[1]))

init()
deci(0)
print("1_2\n")
A1_1 = A

init()
proc1_2()
print("1_3\n")

init()
proc1_3()
write_file.close()
file_object.close()
