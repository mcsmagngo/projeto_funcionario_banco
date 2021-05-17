import re


class Funcionario:
    def __init__(self, nome, cpf, salario, email):
        self.nome = nome
        self.cpf = cpf
        self.valida_cpf_funcionario()
        self._salario = salario
        self.email = email

    @property
    def nome_funcionario(self):
        return self.nome

    @property
    def get_cpf_funcionario(self):
        return self.cpf

    def valida_cpf_funcionario(self):
        padrao_cpf = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')
        match_cpf = padrao_cpf.match(self.cpf)
        if not match_cpf:
            raise ValueError('A URL não é válida.')


    def salario(self):
        return self._salario

    @property
    def get_email_funcionario(self):
        return self.email

    def __str__(self):
        return f'Funcionário: {self.nome}\nCPF: {self.cpf}\nSalário: {self._salario}\nE-mail: {self.email}'


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, email, senha, cargo='Gerente'):
        super().__init__(nome, cpf, salario, email)
        self._senha = senha
        self.valida_senha()
        self.cargo = cargo

    def __str__(self):
        return f'Funcionário: {self.nome}\nCPF: {self.cpf}\nSalário: R${self._salario}\nE-mail: {self.email}\nCargo: {self.cargo}'

    def valida_senha(self):
        other = re.compile('(2)(2)(3)(2)(0)(0)')
        match_senha = other.match(self._senha)
        if not match_senha:
            raise ValueError('A URL não é válida.')

    @property
    def get_senha(self):
        return self._senha


class Caixa(Funcionario):
    def __init__(self, nome, cpf, salario, email, senha, conta, cargo='Caixa'):
        super().__init__(nome, cpf, salario, email)
        self.senha = senha
        self.valida_senha()
        self.conta = conta
        self.cargo = cargo
        self.numero_de_contas()

    def __str__(self):
        return f'Funcionário: {self.nome}\nCPF: {self.cpf}\nSalário Base: R${self._salario}\nE-mail: {self.email}\nCargo: {self.cargo}\nContas abertas: {self.conta}\nSalário com comissão: R${self.numero_de_contas():.2f}'

    def valida_senha(self):
        other = re.compile('(7)(5)(5)(6)(6)(3)')
        match_senha = other.match(self.senha)
        if not match_senha:
            raise ValueError('A URL não é válida.')

    @property
    def get_senha(self):
        return self.senha

    def numero_de_contas(self):
        salario = self.salario()
        numero_de_conta = self.conta
        if numero_de_conta < 10:
            novo_salario = salario + (salario * 5/100)
            return novo_salario
        elif numero_de_conta > 10 and numero_de_conta < 20:
            novo_salario = salario + (salario * 10/100)
            return novo_salario



caixa = Caixa('Fulano', '843.306.199-04', 100.0,'maue@gmail.com', '855663', 12)
print(caixa)
