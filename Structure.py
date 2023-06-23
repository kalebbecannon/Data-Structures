from studentGrades_dict import STUDENT_DICT_DATA

usersInput = str(input("Enter name to search: "))
for names_in_dict in STUDENT_DICT_DATA.keys():
    if names_in_dict == usersInput:
        TokensAndMore = (STUDENT_DICT_DATA[usersInput]["TokensAndMore"])
        HalloweenTown = (STUDENT_DICT_DATA[usersInput]["HalloweenTown"])
        BlanketsMakeMeWarm = (STUDENT_DICT_DATA[usersInput]["BlanketsMakeMeWarm"])
        Mean = (TokensAndMore + HalloweenTown + BlanketsMakeMeWarm) / 3
        
        print("The average grade for",usersInput, "is:",Mean)
if TokensAndMore > HalloweenTown and TokensAndMore > BlanketsMakeMeWarm:
    print("The highest grade for",usersInput,"is Tokens and More with a score of: ",TokensAndMore)
elif HalloweenTown > TokensAndMore and HalloweenTown > BlanketsMakeMeWarm:
    print("The highest grade for",usersInput,"is Halloween Town with a score of: ",HalloweenTown)

elif BlanketsMakeMeWarm > TokensAndMore and BlanketsMakeMeWarm > HalloweenTown:
    print("The highest grade for",usersInput,"is Blankets Make me Warm with a score of: ",BlanketsMakeMeWarm)

elif TokensAndMore == HalloweenTown or TokensAndMore == BlanketsMakeMeWarm or HalloweenTown == BlanketsMakeMeWarm:
    print("The smartest of two!")
