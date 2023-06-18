# First question solution for Replacement Cipher using character frequency
# Code by: Subhodip Ghosal

from collections import Counter

def decrypt(encrypted):
    # Original frequency table
    # freqTable = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'o', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    freqTable = ['e', 't', 'a', 'n', 'o', 'i', 's', 'h', 'r', 'd', 'l', 'c', 'f', 'm', 'u', 'p', 'y', 'b', 'k', 'g', 'v', 'x', 'w', 'q', 'z', 'z']
    charFrequency = Counter(encrypted)
    decrypted = ""

    # ***normal list conversion on dictionary returning unarranged value
    charFrequency = list(sorted(charFrequency, key=charFrequency.get, reverse=True))

    # removing other characters
    charFrequencyList = []
    for char in charFrequency:
        if ord(char)>=97 and ord(char)<=122:
            charFrequencyList.append(char)

    print(charFrequencyList)

    for char in encrypted:
        if ord(char)>=97 and ord(char)<=122:
            index = charFrequencyList.index(char)
            decrypted += freqTable[index]
        else:
            decrypted += char
    
    return decrypted



if __name__ == '__main__':
    # encrypted = input("Enter encrypted code: ")
    # encrypted = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"

    with open("data/encrypted.txt") as encrypted:
        encrypted = encrypted.read().replace('\n', '')

        print(decrypt(encrypted))

    # count frequency program
    # string = input()
    # f = {}
    # for i in string:
    #     f[i] = f.get(i,0) + 1
    # print(f)
