import math
a=int(input(f"lütfen birinci sayıyı girin\n"))
b=int(input(f"lütfen ikinci sayıyı girin\n"))
c=math.gcd(a,b)

if math.gcd(a,b)==1:
        print(f"{a} ve {b} sayıları aralarında asaldır.")

elif math.gcd(a,b)!=1:
        print(f"{a} ve {b} sayıları aralarında asal değildir. Ebobları {c} sayısıdır.")