saldo=float(input('Insira o saldo médio '))
if saldo>=0 and saldo<=200:
    print('Crédito total de ',0.0*saldo,'. Saldo médio percentual foi de ',1.0*saldo)
if saldo>=201 and saldo<=400:
    print('Crédito total de ',0.2*saldo,'. Saldo médio percentual foi de ',1.2*saldo)
if saldo>=401 and saldo<=600:
    print('Crédito total de ',0.3*saldo,'. Saldo médio percentual foi de ',1.3*saldo)
if saldo>=601:
    print('Crédito total de ',0.4*saldo,'. Saldo médio percentual foi de ',1.4*saldo)