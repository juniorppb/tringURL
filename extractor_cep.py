endereco = "Rua Orinoco 46, quadra 4, Vale do Sol, Barueri, SP, 06437-090"

import re # Regula Expression -- RegEx

#5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)