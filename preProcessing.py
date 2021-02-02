

STOPWORDS = ["da" "de", "ve" , "vs." , "ile" , "mi", "mu "]
def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


def main ():
    fileName = "C:\\Users\\samet\\Desktop\\raw_texts\\"
    #f = open("C:\\Users\\samet\\Desktop\\raw_texts\\ekonomi\\2.txt", "r")
    #print(remove_stopwords(f.read()))
    for i in range (5):
        fileTemp = fileName
        if i == 0:
            fileName += "ekonomi\\"
        elif i == 1:
            fileName += "magazin\\"
        elif i == 2:
            fileName += "saglik\\"
        elif i == 3:
            fileName += "siyasi\\"
        elif i == 4:
            fileName += "spor\\"

        counter = i * 150 + 1
        for j in range (150):
            temp = fileName
            fileName = fileName +  str(counter) + ".txt"
            f = open(fileName, "r")
            allText = f.read()
            allTextCopy = allText[:]
            f.close()
            allTextCopy = remove_stopwords(allTextCopy)
            file = open(fileName, "r+")
            file.truncate(0)
            file.write(allTextCopy)
            file.close()


            fileName = temp
            counter += 1

        fileName = fileTemp

if __name__ == '__main__':
    main()