# input , словарьб func reverse
def reverse(strand, complementary):
    reversedStrand = ''
    for value in strand:
        pair = complementary[value]
        reversedStrand += pair
    return reversedStrand[::-1]


complementary = {
    "A": "T",
    "G": "C",
    "T": "A",
    "C": "G"
}
strand = input()
result = reverse(strand, complementary)
print(result)