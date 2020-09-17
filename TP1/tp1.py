AMINOACID_CODING_TABLE = {
        'A' : 'Ala',	
        'R' : 'Arg',	
        'N' : 'Asn',	
        'D' : 'Asp',	
        'C' : 'Cys',	
        'Q' : 'Gln',	
        'E' : 'Glu',	 
        'G' : 'Gly',	
        'H' : 'His',	
        'I' : 'Ile',	
        'L' : 'Leu',	
        'K' : 'Lys',	
        'M' : 'Met',	
        'F' : 'Phe',	
        'P' : 'Pro',	
        'S' : 'Ser',	
        'T' : 'Thr',	
        'W' : 'Trp',	
        'Y' : 'Tyr',	
        'V' : 'Val'
}

H = ['Glu', 'Ala', 'Leu', 'Met', 'Gin', 'Lys', 'Arg', 'His']
B = ['Val', 'Lle', 'Tyr', 'Cys', 'Trp', 'Phe', 'Thr']
L = ['Gly', 'Asn', 'Pro', 'Ser', 'Asp']



def predict_structure(aminoacid):

    try:
        code = AMINOACID_CODING_TABLE[aminoacid]
        if code in H:
            return 'H'
        elif code in B:
            return 'B'
        elif code in L:
            return 'L'
        else:
            raise Exception('Ivalid aminoacid: {}'.format(aminoacid))
    except Exception as e:
        return str(e)
