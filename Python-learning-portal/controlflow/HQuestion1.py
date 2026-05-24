held = int(input())
attended = int(input())
percentage = (attended / held) * 100
if percentage >= 75:
    print(str(int(percentage)) + "% Allowed")
else:
    medical = input()
    if medical == 'Y':
        print(str(int(percentage)) + "% Allowed")
    else:
        print(str(int(percentage)) + "% Not allowed")