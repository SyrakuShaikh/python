# Time-stamp: <2016-04-03 Sun 21:50:10 Shaikh>
# -*- coding: utf-8 -*-
# record the number of the whole procedures.
num_pro = 0


def print_pro(procedure, fr, to):
    global num_pro
    procedure[to].append(procedure[fr].pop())
    l = dn*3 + 1
    print("{0}.".format(num_pro).rjust(3),
          "{0}{1}".format(tA, procedure[tA]).ljust(l),
          "{0}{1}".format(tB, procedure[tB]).ljust(l - 3),
          "{0}{1}".format(tC, procedure[tC]))
    num_pro += 1                # No. of procedures +1


def move(n, A, B, C):
    if n <= 0:
        print("Move what!?")
        return
    elif n == 1:
        return print_pro(procedure, A, C)
    else:
        move(n - 1, A, C, B)
        print_pro(procedure, A, C)
        move(n - 1, B, A, C)

tA = input("Please input the first tower name: ")
tB = input("and the second tower name: ")
tC = input("finally, the last tower name: ")

dn = int(input("How many disks are there on the first tower: "))
# Initialize tower status
procedure = {tA: list(range(dn, 0, -1)), tB: [], tC: []}
print_pro(procedure, tA, tA)
print('-'*(len(tA) + len(tB) + len(tC) + dn*3))
move(dn, tA, tB, tC)
