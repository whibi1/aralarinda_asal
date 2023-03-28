import math
#Öncelikle math kütüphanesini çağırıyoruz.

a=int(input(f"lütfen birinci sayıyı girin\n"))
b=int(input(f"lütfen ikinci sayıyı girin\n"))
c=math.gcd(a,b)
#Daha sonrasında a,b değişkenlerinde  kullanıcıdan iki sayı isteyip bu değerleri c değişkeninde ebob metodu kullanarak karşılaştırıyoruz. 

if math.gcd(a,b)==1:
        print(f"{a} ve {b} sayıları aralarında asaldır.")

elif math.gcd(a,b)!=1:
        print(f"{a} ve {b} sayıları aralarında asal değildir. Ebobları {c} sayısıdır.")
# eğer sayıların ebobu 1 çıkarsa sayıların asal olduğunu, başka bir sayı çıkarsa sayıların ebobunu yazdıran bir kod ekliyoruz.
