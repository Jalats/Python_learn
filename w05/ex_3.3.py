inp = input("Enter Score: ")
try:
    score = float(inp)
except:
    print("If the score is between 0.0 and 1.0")
    quit()

if 0.9 <= score:
    print("A")
elif 0.8 <= score:
    print("B")
elif 0.7 <= score:
    print("C")
elif 0.6 <=score:
    print("D")
else:
    print("F")
