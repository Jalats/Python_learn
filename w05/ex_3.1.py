hrs = input("Enter Hours:")
rate = input("Enter Hours:")
h = float(hrs)
r = float(rate)
#print h, r
if h > 40:
	#print overtime
    reg = h * r
    opt= (h - 40.0) * (r * 0.5)
    #print reg + opt
    xp = reg + opt
else:
    #print("Regular")
    xp = h * r
print("Pay:", xp)
