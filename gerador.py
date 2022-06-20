# MARIA EDUARDA CASSOL VELASCO DA SILVA CATANHOc
# Algoritmo para criptografar senha através do método de substituição 
# letras, símbolos e números pré-determinados fazem a substituição da palavra base recebida pelo input do usuário


chave = input("Digite a palavra base para sua senha: ")

senha = ''
for letra in chave:
    if letra in 'Aa':
        senha = senha + '10'
    elif letra in 'Bb':
        senha = senha + 'Fy' + '#'
    elif letra in 'Cc':
        senha = senha + '1' + '0!'
    elif letra in 'Dd':
        senha = senha + '@' + 'pPv'
    elif letra in 'Ee':
        senha = senha + '*' + '&!'
    elif letra in 'Ff':
        senha = senha + 'Y%'
    elif letra in 'Gg':
        senha = senha + 'HT74'
    elif letra in 'Hh':
        senha = senha + '3,14'
    elif letra in 'Ii':
        senha = senha + '+çQ'
    elif letra in 'Jj':
        senha = senha + 'Tx' + 'L<'
    elif letra in 'Kk':
        senha = senha + 'mEW'
    elif letra in 'Ll':
        senha = senha + '1*9#'
    elif letra in 'Mm':
        senha = senha + '+7' + 'J$'
    elif letra in 'Nn':
        senha = senha + '3%'
    elif letra in 'Oo':
        senha = senha + '_'
    elif letra in 'Pp':
        senha = senha + '&Ee'
    elif letra in 'Qq':
        senha = senha + 'F(x)'
    elif letra in 'Rr':
        senha = senha + ';'
    elif letra in 'Ss':
        senha = senha + '~.~'
    elif letra in 'Tt':
        senha = senha + 'b47'
    elif letra in 'Uu':
        senha = senha + 'Z' + '%J'
    elif letra in 'Vv':
        senha = senha + 'W'
    elif letra in 'Ww':
        senha = senha + '$'
    elif letra in 'Xx':
        senha = senha + '68' + '='
    elif letra in 'Yy':
        senha = senha + 'k#@'
    elif letra in 'Zz':
        senha = senha + 'Er%'
    else:
        senha = senha + letra
print(senha)