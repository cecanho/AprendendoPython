from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, endereco, cpf, telefone, celular, email, nConta, agencia):
        super().__init__(nome, endereco, cpf, telefone, celular, email)
        self._nConta = nConta
        self._agencia = agencia

    @property
    def nConta(self):
        return self._nConta

    @nConta.setter
    def nConta(self, nConta):
        self._nConta = nConta

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia