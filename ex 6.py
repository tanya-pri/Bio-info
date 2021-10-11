def addSequenceToFASTA(name, sequence):
    trueSymbols = ['A', 'T', 'C', 'G']
    upperSequence = sequence.upper()
    resultSequence = ''
    for i in upperSequence:
        if i in trueSymbols:
            resultSequence += i
    file = open(name+'.fasta', 'a')
    file.write('>'+name+'\n')
    file.write(resultSequence+'\n')
    file.close()


addSequenceToFASTA('ABC123', 'ATCGTACGATCGATCGATCGCTAGACGTATCG')
addSequenceToFASTA('DEF456', 'actgatcgacgatcgatcgatcacgact')
addSequenceToFASTA('HIJ789', 'ACTGAC-ACTGT--ACTGTA----CATGTG')