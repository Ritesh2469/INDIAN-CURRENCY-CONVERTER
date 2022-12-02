def indian__dollar(amount):
       return amount * 0.012
def  indian__pound(amount):
       return amount * 0.010
def indian__euros(amount):
        return amount * 0.012
def indian__canadiandollar(amount):
        return amount * 0.016
def indian__chineseyuan(amount):
        return amount * 0.74
def indian__russianrubal(amount):
        return amount * 0.74
def dollar__indian(amount):
         return amount * 81.73
def pound__indian(amount):
        return amount * 98.84
def euros__indian(amount):
        return amount * 84.92
def canadiandollar__indian(amount):
        return amount *61.14
def chineseyuan__indian(amount):
        return amount * 11.40
def russianrubal__indian(amount):
        return amount * 0.74

print(''''''' Welcome to Indian Currency converter''''''')
print('euros')
print('dollar')
print('pound')
print('canadiandollar')
print('chineseyuan')
print('russianrubal')
currency_from=input("currency to be converted in:")
currency_to=input("currency to be converted to:")
amount=int(input("amount given:"))

if currency_from=='indian'and currency_to=='dollar':
    print("amount after conversion:",indian__dollar(amount))
elif currency_from=='indian'and currency_to=='pound':
    print("Amout after conversion:", indian__pound(amount))
elif currency_from=='indian'and currency_to=='euros':
    print("Amout after conversion:", indian__euros(amount))
elif currency_from=='indian'and currency_to=='canadiandollar':
    print("Amout after conversion:", indian__canadiandollar(amount))
elif currency_from=='indian'and currency_to=='russianrubal':
    print("Amout after conversion:", indian__russianrubal(amount))
elif currency_from=='indian'and currency_to=='chineseyuan':
    print("Amout after conversion:", indian__chineseyuan(amount))
if currency_from=='dollar'and currency_to=='indian':
    print("Amout after conversion:", dollar__indian(amount))
elif currency_from=='pound'and currency_to=='indian':
    print("Amout after conversion:", pound__indian(amount))
elif currency_from=='euros'and currency_to=='indian':
    print("Amout after conversion:", euros__indian(amount))
elif currency_from=='canadiandollar'and currency_to=='indian':
    print("Amout after conversion:", canadiandollar__indian(amount))
elif currency_from=='russianrubal'and currency_to=='indian':
    print("Amout after conversion:", russianrubal__indian(amount))
elif currency_from=='chineseyuan'and currency_to=='indian':
    print("Amout after conversion:", chineseyuan__indian(amount))


