held = int(input().strip())
attended = int(input().strip())
percentage = (attended / held) * 100

if percentage >= 75:
    print(str(int(percentage)) + "% Allowed")
else:
    medical = input().strip()
    if medical.upper() == 'Y':
        print(str(int(percentage)) + "% Allowed")
    else:
        print(str(int(percentage)) + "% Not allowed")
