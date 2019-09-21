from collections import Counter
def count_nucs(dna_string: str)->str:

    if isinstance(dna_string, list):
        raise TypeError

    if not isinstance(dna_string, str):
        raise TypeError


    cnt = Counter(dna_string.upper())
    if len([x for x in cnt.keys() if x not in ["A","C","G","T"]]) > 0:
        raise ValueError("only A C G and T are OK")
    l   = [cnt[x] for x in ["A","C","G","T"]]
    return " ".join(map(str,l))
