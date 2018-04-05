from argon2i import *

from test_vectors.argon2i_test_vectors import *
from sys import exit

def main(x:int) -> None:
    for i, vec in enumerate(argon2i_test_vectors):
        p = bytes.from_hex(vec['p'])
        s = bytes.from_hex(vec['s'])
        x = bytes.from_hex(vec['x'])
        k = bytes.from_hex(vec['k'])
        lanes = vec['lanes']
        t_len = vec['t_len']
        m = vec['m']
        iterations = vec['iterations']
        expected = bytes.from_hex(vec['output'])
        computed = argon2i(p,s,lanes,t_len,m,iterations,x,k)
        if computed == expected:
            print("Argon2i Test {} passed.".format(i+1))
        else:
            print("Argon2i Test {} failed.".format(i+1))
            print("expected hash:",expected)
            print("computed hash:",computed)
            exit(1)


if __name__ == "__main__":
    main(0)
