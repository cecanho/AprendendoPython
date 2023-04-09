# 1. Nosso banco precisa tributar dinheiro de alguns bens que nossos clientes possuem.
# Para isso vamos criar uma classe Tributavel com um método que devolve o imposto sobre a conta.
# 2. Transforme a classe Tributavel em um mix-in
# 3. Faça a classe ContaCorrente herdar da classe TributavelMixIn e implemente o método
# "exigido" pelo MixIn
# 4. Crie a classe SeguroDeVida que vai herdar de TributavelMixIn . Crie seus respectivos atributos
# e implemente o método do MixIn
# 5. Vamos criar a classe ManipuladorDeTributaveis em um arquivo chamado manipulador.py. Essa
# classe deve ter um método chamado calcula_impostos() que recebe uma lista de tributáveis e
# retorna o total de impostos cobrados
# 6. Ainda no arquivo manipulador.py , vamos testar o código. Crie alguns objetos de
# ContaCorrente e de SeguroDeVida . Em seguida, crie uma lista de tributáveis e insira seus
# objetos nela. Instancie um ManipuladorDeTributaveis e chame o método calcula_impostos()
# passando a lista de tributáveis criada e imprima o valor total dos impostos

# from conta import Conta

# c = Conta('123-4', 'José', 5000.0, 0)

from contaCorrente import CC
from contaPoupanca import CP

cc = CC('123-4', 'PF', 'José', 1000.0)
cp = CP('124-4', 'PJ', 'Manuel', 1000.0)
