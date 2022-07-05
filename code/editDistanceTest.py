from editDistance import editDistance

def testcase(word1, word2):
    print("Edit distance between", word1, "and", word2, ":", editDistance(word1, word2))
    
testcase("snowy","sunny")
testcase("abcdefghijklmnop","bcdefghijklmnopq")
testcase("short","reallyreallylong")
testcase("","sunny")
testcase("","")
