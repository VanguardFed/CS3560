#--------------------------#
#                          #
#      Trent Thompson      #
#    CS3560 Spring 2017    #
#      Due: 2-16-2017      #
#                          #
#--------------------------#

def translate(text):
    translated=""
    consonants=['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for i in text:
        if i.lower() in consonants:
            to_insert=i+'o'+i.lower()
        else:
            to_insert=i
        translated+=to_insert
    return translated
    #COMPLETE
def sum(num_list):
    total=0
    for num in num_list:
        total+=num
    return total
    #COMPLETE
def multiply(num_list):
    total=1
    if 0 in num_list or len(num_list)==0:
        return 0
    for num in num_list:
        total=total*num
    return total
    #COMPLETE
def reverse(text):
    reversed=""
    for i in range (len(text)):
        j=-1*(i-len(text))-1
        #print j
        reversed+=text[j]
    return reversed
    #COMPLETE
def is_palindrome(text):
    return True if text==reverse(text) else False
    #COMPLETE
def overlapping(list1, list2):
    for i in range(0,len(list1)):
        if list1[i]==list2[i]:
            return True
    return False
    #COMPLETE
def histogram(num_list):
    for i in range (len(num_list)):
        print '*'*num_list[i]
    return None
    #COMPLETE
def find_longest_word(word_list):
    longest=""
    for i in range(0,len(word_list)):
        if len(word_list[i])>len(longest):
            longest=word_list[i]
    return longest
    #COMPLETE
def filter_long_words(word_list,len_limit):
    counter=0
    long_list=[]
    for i in range(0,len(word_list)):
        if len(word_list[i])>len_limit:
            long_list.append(word_list[i])
    return long_list
    #COMPLETE
def is_palindrome_sentence(phrase):
    return is_palindrome(filter(str.isalpha,phrase.lower()))
    #COMPLETE
def is_pangram(phrase):
    all_letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,len(all_letters)):
        if all_letters[i] not in phrase.lower():
            return False
    return True
    #COMPLETE


#------------#
# TEST CALLS #
#------------#



# Translate tests
print "translate test 1                passed." if translate("this is a test")=="tothohisos isos a totesostot" else "translate test                 failed."
print "translate test 2                passed." if translate("test with all vowels yep")=="totesostot wowitothoh alollol vovowowelolsos yepop" else "translate test 2                failed."
print "translate test 3                passed." if translate("Testing. Symbols and caps?")=="Totesostotinongog. Sosymombobololsos anondod cocapopsos?" else "translate test 3                failed."
print
# Sum tests
print "sum test 1                      passed." if sum([3,6,4])==13 else "sum test 1                      failed."
print "sum test 2                      passed." if sum([8,24,36,89])==157 else "sum test 2                      failed."
print "sum test 3                      passed." if sum([1])==1 else "sum test 3                      failed."
print
# Multiply tests
print "multiply test 1                 passed." if multiply([3,4,2])==24 else "multiply test 1                 failed."
print "multiply test 2                 passed." if multiply([6,0])==0 else "multiply test 2                 failed."
print "multiply test 3                 passed." if multiply([])==0 else "multiply test 3                 failed."
print
# Reverse tests
print "reverse test 1                  passed." if reverse("this is a test")=="tset a si siht" else "reverse test 1                  failed"
print "reverse test 2                  passed." if reverse("How do caps?")=="?spac od woH" else "reverse test 2                  failed"
print "reverse test 3                  passed." if reverse("car")=="rac" else "reverse test 3                  failed"
print
# Palindrome tests
print "is_palindrome test 1            passed." if is_palindrome("not a palindrome")==False else "is_palindrome test 1            failed."
print "is_palindrome test 2            passed." if is_palindrome("racecar")==True else "is_palindrome test 2            failed."
print "is_palindrome test 3            passed." if is_palindrome("redivider")==True else "is_palindrome test 3            failed."
print
# Overlapping tests
print "overlapping test 1              passed." if overlapping([5,9,4,6],[8,6,2,1])==False else "overlapping test 1              failed."
print "overlapping test 2              passed." if overlapping([2,6],[5,6,8,9])==True else "overlapping test 2              failed."
print "overlapping test 3              passed." if overlapping([8,4,7,5,1],[2,8,7])==True else "overlapping test 3              failed."
print
# Histogram tests
print "histogram test 1  [5,7,8,2,6,4]"
histogram([5,7,8,2,6,4])
print "histogram test 2  [3,5,7]"
histogram([3,5,7])
print "histogram test 3  [17]"
histogram([17])
print
# Longest word tests
print "find_longest_word test 1        passed." if find_longest_word(["dog","cat","frog"])=="frog" else "find_longest_word test 1        failed."
print "find_longest_word test 2        passed." if find_longest_word(["python","programming","cs3560"])=="programming" else "find_longest_word test 2        failed."
print "find_longest_word test 3        passed." if find_longest_word(["test"])=="test" else "find_longest_word test 3        failed."
print
# Filter tests
print "filter_long_words test 1        passed." if filter_long_words(["test","dog","eating","walk","walking","make"],4)==["eating","walking"] else "filter_long_words test 1        failed."
print "filter_long_words test 1        passed." if filter_long_words(["palindrome","magical","","tricks"],6)==["palindrome","magical"] else "filter_long_words test 1        failed."
print "filter_long_words test 1        passed." if filter_long_words(["","zero",""],0)==["zero"] else "filter_long_words test 1        failed."
print
# Palindrome sentence tests
print "is_palindrome_sentence test 1   passed." if is_palindrome_sentence("Rise to vote sir.")==True else "is_palindrome_sentence test 1   failed."
print "is_palindrome_sentence test 2   passed." if is_palindrome_sentence("This is not a palindrome")==False else "is_palindrome_sentence test 2   failed."
print "is_palindrome_sentence test 3   passed." if is_palindrome_sentence("Was it a rat I saw?")==True else "is_palindrome_sentence test 3   failed."
print
# Pangram tests
print "is_pangram test 1               passed." if is_pangram("The quick brown fox jumps over the lazy dog")==True else "is_pangram test 1               failed."
print "is_pangram test 2               passed." if is_pangram("This is not a pangram.")==False else "is_pangram test 2               failed."
print "is_pangram test 3               passed." if is_pangram("How quickly daft jumping zebras vex.")==True else "is_pangram test 3               failed."
print
