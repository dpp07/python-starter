# Python Assignments
import random

# Ex. 2 Answer 
def main():
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    length = float(input("Enter length: "))

    volume = width * height * length
    print("Volume is: " , volume)





# Ex. 3 Answer
def main():
    userInput = input("Enter list of numbers: ")
    myList = [int(elem) for elem in userInput.split(',')]
    if myList[0] == myList[-1]:
         print('true')

    else:
        print('false')



# Ex. 4 Answer
def main():
    counter = 0
    checker = "Python"
    text = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    stringlist = text.split(' ')

    for checker in stringlist:
        if checker == 'Python':
            counter+= 1

        
    print(counter)

# Ex. 5 Answer
def main():
    myList = [1,2,3]
    mySet = {3,4,5}

    mySet.update(myList)
    print(mySet)

# EX. 6 Answer
def main():
    arrayList = [11, 100, 101, 999, 1001]
    arrayList.reverse()
    print(arrayList)
  
# Number 7
def main():
    i = random.randint(0,100)
    print(i)
    if i < 10:
        print("You lose" )
    elif i > 10 and i < 50 :
        print("Try again")
    else:
        print("You Win!!!")

# Number 8 
def main():
    myList = [6,2,7,3,77,7,1]
    min1 = myList[0]
    for i in range(len(myList)):
        if myList[i] < min1:
            min1 = myList[i]
            
    print(min1)

# Number 9 
def main():
    userInput = input("Enter string in uppers or lowers: ")
    if userInput.isupper():
        print(True)
    else:
        print(False)

# Number 10 
def count_vowels_and_consonants(word):
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0

    for letter in word:
        if letter.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

    return vowels_count, consonants_count


def main():
    word = input("Enter a word: ")
    vowels_count, consonants_count = count_vowels_and_consonants(word)

    print(f"The word '{word}' has {vowels_count} vowels and {consonants_count} consonants.")


if __name__ == "__main__":
    main()