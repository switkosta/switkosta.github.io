from getpass import getpass


def maksimum(a = []):
    maxi = a[0]
    for i in range(0,len(a) - 1):
        if maxi > a[i+1]:
            maxi = maxi
        else:
            maxi = a[i + 1]
    print(maxi)



great = [77,4654,478,98,34]
maksimum(great)