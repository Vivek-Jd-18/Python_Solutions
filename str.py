# bytes
x = bytes('cöde', encoding='utf-8')

print(str(x, encoding='ascii', errors='ignore'))#result:  cde
print(str(x, encoding='UTF-8', errors='ignore'))#result: cöde
