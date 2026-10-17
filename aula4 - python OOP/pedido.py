class Pedido:
    def __init__(self, metodo_pagamento, finalizado, cliente, funcionario):
        self.metodo_pagamento = metodo_pagamento
        self.finalizado = finalizado # boolean
        self.cliente = cliente # pegar objeto cliente
        self.funcionario = funcionario # pegar objeto funcionario

    def finalizar_pedido(self):
        self.finalizado = True