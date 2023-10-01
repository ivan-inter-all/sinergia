import os
os.mkdir(r'222')
for i in range(10):
    tt = open(rf'222\aa{i}.txt', 'w')
    tt.write('Вася считает квадраты:\n')
    for j in range(10):
        tt.write(f'Вася {j**2}\n')
    tt.close()
