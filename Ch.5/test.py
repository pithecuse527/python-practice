def FtoC(temp_f) :
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c

for temp_f in range(212,-213,-1) :
    temp_c = FtoC(temp_f)
    if temp_f < temp_c :
        print(temp_c, "//", temp_f)
        break
