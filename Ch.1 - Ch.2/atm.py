##
#   18.03.13
#   20152262  Hong Geun Ji
#
#   ATM
#

itemPrice = int(input("물건의 값? "))
nPaperMoney = int(input("1000원 지폐개수: "))
nCoin500 = int(input("500원 동전개수: "))
nCoin100 = int(input("100원 동전개수: "))

change = (nPaperMoney * 1000 + nCoin500 * 500 + nCoin100 * 100) - itemPrice

# Calculate how many the 500won of change is
nChange500 = change // 500
change = change % 500

# Calculate how many the 100won of change is
nChange100 = change // 100
change = change % 100

# Calculate how many the 10won of change is
nChange10 = change // 10
change = change % 10

# Calculate how many the 1won of change is
nChange1 = change

print("500원 =", nChange500, "/ 100원 =", nChange100, "/ 10원 =", nChange10, "/ 1원 =", nChange1)
