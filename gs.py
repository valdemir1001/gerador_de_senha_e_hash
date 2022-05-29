import random,string

tamanho = int(input('Digite o tamanho da sua senha: '))
chars = string.ascii_letters + string.digits + 'ç!@#$%&Ç*()-_=+.<>'
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
