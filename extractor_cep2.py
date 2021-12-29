endereco = "Rua Orinoco 46, quadra 4, Vale do Sol, Barueri, SP, 06437-090"

import re # Regula Expression -- RegEx

#5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)