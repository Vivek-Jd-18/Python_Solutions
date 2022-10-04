class Rollnums:
  a = 15
  b = -7
  c = 0

rno = Rollnums() 

print('a = ',rno.a)
print('b = ',rno.b)
print('c = ',rno.c)

delattr(Rollnums, 'c')

print('--After deleting c attribute--')
print('a = ',rno.a)
print('b = ',rno.b)
