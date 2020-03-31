def leap_year(year):
    if year%100==0:
        if year%400==0:
            print("True")
        else:
            print("False")
    elif year%4==0:
        print("True")
    else:
        print("False")


year=int(input())
leap_year(year);
