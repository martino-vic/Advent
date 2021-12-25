"""Refactored version of Day 25 - MOVING SEA CUCUMBERS"""
from time import perf_counter

def move(field: 'list of str', cucumber: "'>' or 'v'") -> 'list of str':
    """move given cucumbers to the right, then flip rows and cols"""

    for i in range(len(field)):  # move cucmbers to the right
        # if current catches cucumber
        if field[i][0] == "." and field[i][-1] == cucumber:
            field[i] = list(field[i])
            # wash it on the other side
            field[i][0], field[i][-1] = cucumber, "."
            field[i] = "".join(field[i])
            field[i] = field[i][0] \
                + field[i][1:-1].replace(cucumber+".", "."+cucumber) \
                + field[i][-1]  # and move only others
            continue  # go to next line
        # only if no current is washing
        field[i] = field[i].replace(cucumber+".", "."+cucumber)

    # flip axes
    return ["".join(row[col] for row in field) for col in range(len(field[0]))]


def main(file: 'name of file') -> int:
    """move field until all cucumbers stuck, return how many rounds it took"""
    start_time = perf_counter()
    field = open(file).read().split("\n")
    stack = field
    field = move(move(field, ">"), "v")
    rounds = 1
    while stack != "".join(field):
        # if no string conversion, old stack overwritten at one point?!?!
        stack = "".join(field)
        field = move(move(field, ">"), "v")
        rounds += 1

    total_time = perf_counter() - start_time
    print(f"Cucumbers stop moving after {rounds} rounds.\
(took {total_time:.3f} seconds)")

    return rounds

if __name__ == "__main__":
    main("real")