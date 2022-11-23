import os #modulo nativo do python

if (os.name == 'posit'): # 'posit' - Linux e mac 'nt' - Windows
    print('Voçê esta utilizando o sistema Linux')
elif(os.name == 'nt'):
    print('Você esta utilizando o sistema Windows')
else:
    print('Não consegui identificar o seu sistema operacional')



