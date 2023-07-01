class End_simples(object):

    def __init__(self, rua, num, bairro):
        self.rua = rua
        self.num = num
        self.bai = bairro
    def Endereco(self):
        return self.rua + ", " + self.num + "\ " + self.bai


class End_com(End_simples):

    def __init__(self, rua, num, bai, com):
        End_simples.__init__(self,rua, num, bai)
        self.com = com

    def Endereco(self):
        return super(End_com, self).Endereco() + ", " + self.com
        #return self.Endereco()+ ", " + self.com
        #return parent(End_com, self).Endereco() + ", " + self.com
        #return End_simples.Endereco() + ", " + self.comw
        #return self.parent.Endereco() + ", " + self.com


a = End_simples("Av Brasil", "243", "Floresta")

b = End_com("Av Miracema", "12", "Centro", "apto 3")

print(a.Endereco())

print(b.Endereco())

