def computepay(sh, sr):
    ih = float(sh)
    ir = float(sr)
    if ih > 40:
        pay = (ih - 40)*1.5*ir + 40 * ir
    else:
        pay = ih * ir
    print("Enter hours:", sh)
    print("Enter Rate:", sr)
    print("Pay:", pay)
        
def computegrade(scr):
    print(type(scr))
    try:
        scr = float(scr)
    except:
        print("Bad score")
        quit()
    if scr < 0 or scr > 1:
        print("Bad score")
    elif scr >= 0.9:
        grd = "A"
    elif scr >= 0.8:
        grd = "B"
    elif scr >= 0.7:
        grd = "C"
    elif scr >= 0.6:
        grd = "D"
    else:
        grd = "F"
    print("Grade:", grd)
