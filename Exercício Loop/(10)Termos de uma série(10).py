"""serie A x+2/n+1 até 99/50 ; Serie B x/x² até 10/100; Serie C 1/(x+2)**3  (20 termos)"""
# Serie A
s1 = s2 = soma = 1
div = s1 / s2

while s1 < 99:
    s1 += 2
    s2 += 1
    div = s1 / s2
    soma += div
    # print(f'{div:.6f}', end='....')
    # print(f'a soma dos termos é {soma:.5f}')
# Série B
t1 = t2 = soma2 = div2 = 1

while t1 <= 10:
    if t1 == 1:
        print(f'O {t1}º termo é {div2:.5f} e a soma é {soma2:.5f}')
    elif t1 % 2 == 0:
        soma2 -= div2
        print(f'O {t1}º termo é -{div2:.5f} e a soma é {soma2:.5f}')
    else:
        soma2 += div2
        print(f"O {t1}º termo é {div2:.5f} e a soma é {soma2:.5f}")
    t1 += 1
    t2 = t1 ** 2
    div2 = t1 / t2
# Serie C
x1 = soma3 = termo = 1
# print(f'O termo {termo} é {1/x1**3} e a sua soma é igual a {soma3}')
for c in range(1, 20):
    x1 += 2
    if c % 2 == 0:
        soma3 += 1 / x1 ** 3
        # print(f'O termo {termo} é {1 / x1 ** 3:.6f} e a soma é igual a {soma3:.6f}')
    else:
        soma3 -= 1 / x1 ** 3
        # print(f'O termo {termo} é -{1 / x1 ** 3:.6f} e a soma é igual a {soma3:.6f}')
    termo += 1
