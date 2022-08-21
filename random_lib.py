from multi_libs import halo, mad, mario

import random


if __name__ == "__main__":
    m = random.choice([halo, mad, mario])
    m.madlib()
