from z3 import Solver, BitVec, And, sat, Or


def check(solver, x):
    solver.add(x[9] ^ x[19] == 58)
    solver.add(x[4] ^ x[1] == 7)
    solver.add(x[6] ^ x[18] == 2)
    solver.add(x[4] ^ x[2] == 21)
    solver.add(x[19] ^ x[0] == 6)
    solver.add(x[1] ^ x[7] == 6)
    solver.add(x[18] ^ x[17] == 17)
    solver.add(x[15] ^ x[7] == 20)
    solver.add(x[6] ^ x[1] == 21)
    solver.add(x[4] ^ x[5] == 30)
    solver.add(x[4] ^ x[20] == 14)
    solver.add(x[12] ^ x[19] == 16)
    solver.add(x[11] ^ x[16] == 29)
    solver.add(x[2] ^ x[16] == 9)
    solver.add(x[6] ^ x[10] == 3)
    solver.add(x[4] ^ x[2] == 21)
    solver.add(x[17] ^ x[9] == 45)
    solver.add(x[4] ^ x[19] == 22)
    solver.add(x[13] ^ x[20] == 9)
    solver.add(x[11] ^ x[19] == 23)




def add_invalid(solver, array, values):
    cond = array[0] != values[0]
    for i, item in enumerate(array):
        if i == 0:
            continue
        cond = Or(cond, (item != values[i]))
    solver.add(cond)


x = [BitVec('x' + str(i), 8) for i in range(21)]
solver = Solver()
for x_ref in x:
    # lowercase
    solver.add(And(94 < x_ref, x_ref < 127))
solver.add(x[0] == ord("c"))
solver.add(x[1] == ord("t"))
solver.add(x[2] == ord("f"))
solver.add(x[3] == ord("{"))
solver.add(x[-1] == ord("}"))
check(solver, x)
while solver.check() == sat:
    model = solver.model()
    out = [model.eval(x[i]).as_long().real for i in range(21)]
    out_str = ""
    for val in out:
        out_str += chr(val)
    # print(solver.statistics())
    add_invalid(solver, x, out)
    print(out_str)
