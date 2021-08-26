def Anogram_check(string1, string2):
# Strings are sorted and verified
    if(sorted(string1)== sorted(string2)):
        print(sorted(string1))
        print("Both strings form a Anogram.")
        return True
    else:
        print("Both strings do not form as a Anogram.")
# driver code
string1 ="EARTH"
string2 ="HEART"
print( "String value1 : ", string1 )
print( "String value2 : ", string2 )
Anogram_check(string1, string2)
#end