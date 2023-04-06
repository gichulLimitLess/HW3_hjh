def reverse_string(a):
    print("input : {0:s}".format(a))
    stringToList = a.split() #문자열을 리스트로 변환
    stringToList.reverse()
    result = " ".join(stringToList)
    print("output : {0:s}".format(result))

def main():
    string1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    string2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"

    #문자열 뒤집고 각각을 출력하는 함수 호출
    reverse_string(string1)
    reverse_string(string2)


if __name__ == '__main__':
    main()