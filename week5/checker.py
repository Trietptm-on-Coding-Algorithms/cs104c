import sys

def main(infile, jout, outfile):
    fin = open(infile, 'r')
    fjout = open(jout, 'r')
    fout = open(outfile, 'r')

    T = int(fin.readline())

    correct = 0
    for _ in range(T):
        j_out = list(map(int, fjout.readline().split()))
        output = list(map(int, fout.readline().split()))

        if j_out == output:
            correct += 1
            continue

        # otherwise read in the input and make sure we have an euler tour
        nodes, edges = map(int, fin.readline().split())

        blah = set()
        for _ in range(edges):
            u, v = map(int, fin.readline().split())
            if u > v:
                u, v = v, u
            blah.add((u, v))

        valid = True
        n = len(output)
        for i in range(1, n):
            u, v = output[i - 1], output[i]
            if u > v:
                u, v = v, u
            if (u, v) not in blah:
                print('Edge {} {} not in graph'.format(u, v))
                valid = False
                break

            blah.remove((u, v))

        if blah:
            print('Missed edges', blah)
        if valid and not blah:
            print('Correct!')
            correct += 1


    print(correct, 'Correct')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('program input judge output')
        sys.exit(1)

    inp = sys.argv[1]
    judge = sys.argv[2]
    out = sys.argv[3]
    main(inp, judge, out)
