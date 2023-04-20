class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

#     Método GET
    def get_nome(self):
        return self._nome

#     Método SET
    def set_nome(self, nome):
        self._nome = nome