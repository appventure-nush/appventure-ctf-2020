import random

from z3 import BitVec, Solver, sat, Or, And


def add_invalid(solver, array, values):
    cond = array[0] != values[0]
    for i, item in enumerate(array):
        if i == 0:
            continue
        cond = Or(cond, (item != values[i]))
    solver.add(cond)


flag = "ctf{smart_bruteforce}"

flag = [ord(x) for x in flag]
x = [BitVec('x' + str(i), 8) for i in range(len(flag))]
solver = Solver()
for x_ref in x:
    # lowercase
    solver.add(And(94 < x_ref, x_ref < 127))

solver.add(x[0] == ord("c"))
solver.add(x[1] == ord("t"))
solver.add(x[2] == ord("f"))
solver.add(x[3] == ord("{"))
solver.add(x[-1] == ord("}"))
tab = "    "
fn = "def check(string):\n"
fn += f"{tab}assert re.match('^ctf{{[a-z_]{{{len(flag)-5}}}}}$', string)\n{tab}return "
i = 0
while i < 20:
    a = random.randrange(0, len(flag))
    b = random.randrange(0, len(flag))
    if a == b:
        continue
    fn += f"string[{a}] ^ string[{b}] == {flag[a] ^ flag[b]} and \\\n{tab}"
    solver.add(x[a] ^ x[b] == flag[a] ^ flag[b])
    i += 1
print(fn)
possible = 30
while solver.check() == sat:
    model = solver.model()
    out = [model.eval(x[i]).as_long().real for i in range(len(flag))]
    out_str = ""
    for val in out:
        out_str += chr(val)
    # print(solver.statistics())
    add_invalid(solver, x, out)
    print(out_str)
    possible -= 1
    if possible < 0:
        print("More than 30")
        break
    # break
else:
    print("Die")
