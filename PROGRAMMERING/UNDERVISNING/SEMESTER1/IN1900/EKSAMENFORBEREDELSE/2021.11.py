def read_DNA(filename):
    dna=""
    with open(filename) as infile:
        for line in infile:
            words = line.split()
            dna += words[-1]
    return dna

def find_CG(dna):
    cg = []
    for i in range(len(dna)-1):
        if dna[i:i+2] == "CG":
            cg.append(i)
    return cg

def test_find_cg():
    dna = "TATACG"
    expected = [4]
    computed = find_CG(dna)
    assert expected == computed
    dna = "CGCGCG"
    expected = [0,2,4]
    computed = find_CG(dna)
    assert expected == computed
test_find_cg()

def longest(dna):
    pos = find_CG(dna)
    res = count = 1
    for i in range(1,len(pos)):
        if pos[i] == pos[i-1]+2:
            count += 1
            res = max(count,res)
        else:
            count = 1
    return res
