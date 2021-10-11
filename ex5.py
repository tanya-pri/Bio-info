#создать фаста, что м меняются на Мб а символы и что-то кроме АТГЦ удаляется
def addSequenceToFASTA(name, sequence):
    trueSymbols = ['A', 'T', 'C', 'G']
    upperSequence = sequence.upper()
    resultSequence = ''
    for i in upperSequence:
        if i in trueSymbols:
            resultSequence += i
    file = open('file.txt', 'a')
    file.write('>'+name+'\n')
    file.write(resultSequence+'\n')
    file.close()


addSequenceToFASTA('ABC123', 'ATCGTACGATCGATCGATCGCTAGACGTATCG')
addSequenceToFASTA('DEF456', 'actgatcgacgatcgatcgatcacgact')
addSequenceToFASTA('HIJ789', 'ACTGAC-ACTGT--ACTGTA----CATGTG')