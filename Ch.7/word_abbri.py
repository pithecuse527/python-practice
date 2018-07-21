table = {"B4" : "Before",
         "TX" : "Thanks",
         "BBL" : "Be Back Later",
         "BCNU" : "Be Seeing You",
         "HAND" : "Have A Nice Day"}
mes = input("메세지를 입력 : ")
mes_word = mes.split()
result = ""
for word in mes_word:
    if word in table:
        result += table[word] + " "
    else:
        result += word

print result
