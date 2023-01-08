def cria_url(muda1, muda2, muda3, muda4):
    url = 'https://www25.{}.leg.br/{}/12427/{}/{}/2afcf536-a05c-42d7-a4bb-cd366e4ed8ad'
    return url.format(muda1, muda2, muda3, muda4)

print(cria_url('corruptos', 'trambiqueiros', 2023, 'corrupção'))



# onde no texto original foi apagado partes e colocado {} será preenchido pelas palavras no parmatro URL.FORMAT

# Url original
# https://www25.senado.leg.br/documents/12427/122050222/02%20-%20Relat%C3%B3rio%20de%20Fevereiro%20de%202022/2afcf536-a05c-42d7-a4bb-cd366e4ed8ad

# Url Modificada
# https://www25.corruptos.leg.br/trambiqueiros/12427/2023/corrupção/2afcf536-a05c-42d7-a4bb-cd366e4ed8ad