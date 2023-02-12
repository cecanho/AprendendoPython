import datetime


class Data_Abertura:

    def __init__(self):
        self.data_abertura = datetime.date.today()

    def abertura_de_conta(self):
        return str(self.data_abertura)