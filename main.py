import math
def cal() :
    num1 = float(input("adad Aval ra vared kon: "))
    print("1 = jam\n2 = tafriq\n3 = zarb\n4 = taqsim\n5 = tavan\n6 = jazr")
    operation = input("Amaliat Mored Nazar? ")
    if operation != "6":
        num2 = float(input("adad Dovom ra vared kon: "))

    result = None

    match operation:
        case "1":
            result = num1 + num2
        case "2":
            result = num1 - num2
        case "3":
            result = num1 * num2
        case "4":
            if num2 == 0:
                print("taqsim bar sefr emkan pazir nist!")
            else:
                result = num1 / num2
        case "5":
            result = math.pow(num1, num2)
        case "6":
            if num1 < 0:
                print("jazr adad manfi dar r math emkan pazir nist!")
            else:
                result = math.sqrt(num1)
        case _:
            print("dobare talash kon!")

    print(f"javab = {result}")
    edame = input("Edame Midahid? (y/n) ")
    if edame == "y":
        cal()
    else:
        print("bedrod!")
cal()