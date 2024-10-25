def tower_of_hanoi(n, sumber, tujuan, bantuan):
    if n == 1:
        print("Move disk 1 from peg {} to peg {}".format(sumber, tujuan))
        return
    tower_of_hanoi(n - 1, sumber, bantuan, tujuan)
    print("Move disk {} from peg {} to peg {}".format(n, sumber, tujuan))
    tower_of_hanoi(n - 1, bantuan, tujuan, sumber)


tower_of_hanoi(3, 'A', 'C', 'B')
