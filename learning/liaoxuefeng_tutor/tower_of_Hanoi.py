# Time-stamp: <2016-03-31 Thu 22:54:27 Shaikh>
# -*- coding: utf-8 -*-

# record the number of the whole procedures.
num_pro = 1


def print_pro(result, fr, to):
    global num_pro
    # spaces used for alignment.
    space = {tA: 0, tB: 0, tC: 0}
    if len(result[fr]) == 1:
        fr_v = 1
    else:
        fr_v = 3
    if len(result[to]) == 0:
        space[to] = 1
    else:
        space[to] = 3
    # print 'from' status
    print("{2}.From {0}{1}".format(tA, result[tA], num_pro),
          ' '*(space[tA]) + "{0}{1}".format(tB, result[tB]),
          ' '*(space[tB]) + "{0}{1}".format(tC, result[tC]),
          ' '*(space[tC]))
    # make the move!
    result[to].append(result[fr].pop())
    num_pro += 1                # No. of procedures +1
    space[to] = 0
    space[fr] = fr_v
    print(' '*(len(str(num_pro)) + 3) +
          "To {0}{1}".format(tA, result[tA]),
          ' '*(space[tA]) + "{0}{1}".format(tB, result[tB]),
          ' '*(space[tB]) + "{0}{1}".format(tC, result[tC]))
    print('-'*(8 + 3*4 + dn*3))
    return result


def move(n, A, B, C):
    if n <= 0:
        print("Move what!?")
        return
    elif n == 1:
        return print_pro(result, A, C)
    else:
        move(n - 1, A, C, B)
        print_pro(result, A, C)
        move(n - 1, B, A, C)

tA = input("Please input the first tower name: ")
tB = input("and the second tower name: ")
tC = input("finally, the last tower name: ")

dn = int(input("How many disks are there on the first tower: "))
# Initialize tower status
result = {tA: list(range(dn, 0, -1)), tB: [], tC: []}
move(dn, tA, tB, tC)
