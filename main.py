# RootBot 🌱 - Educação Ambiental em Escolas
class Item:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def __str__(self):
        return f"{self.titulo} - {self.descricao}"


class FaixaEtaria:
    def __init__(self, nome, idade_min, idade_max):
        self.nome = nome
        self.idade_min = idade_min
        self.idade_max = idade_max
        self.didaticas, self.temas = [], []

    def listar(self, lista):
        if not lista:
            print("⚠️ Nenhum item cadastrado ainda.")
            return
        for i, item in enumerate(lista, 1):
            print(f"[{i}] {item}")

    def crud(self, lista, tipo):
        while True:
            print(f"\n📂 {tipo} - Opções:")
            print("[1] Listar\n[2] Adicionar\n[3] Editar\n[4] Excluir\n[9] Voltar")
            op = input("Escolha: ")

            if op == "1":
                self.listar(lista)
            elif op == "2":
                t, d = input("Título: "), input("Descrição: ")
                lista.append(Item(t, d))
                print(f"✅ {tipo[:-1]} adicionada com sucesso!")
            elif op == "3":
                self.listar(lista)
                try:
                    i = int(input("Número: ")) - 1
                    if 0 <= i < len(lista):
                        lista[i].titulo = input("Novo título: ")
                        lista[i].descricao = input("Nova descrição: ")
                        print("✏️ Alterado com sucesso!")
                except ValueError:
                    print("⚠️ Entrada inválida.")
            elif op == "4":
                self.listar(lista)
                try:
                    i = int(input("Número: ")) - 1
                    if 0 <= i < len(lista):
                        removido = lista.pop(i)
                        print(f"🗑️ {removido.titulo} removido com sucesso!")
                except ValueError:
                    print("⚠️ Entrada inválida.")
            elif op == "9":
                break
            else:
                print("⚠️ Opção inválida.")


class Professor:
    def __init__(self, nome, escola, turma):
        self.nome = nome
        self.escola = escola
        self.turma = turma

    def __str__(self):
        return f"👩‍🏫 Professor: {self.nome} | Escola: {self.escola} | Turma: {self.turma}"


class Chatbot:
    def __init__(self, nome, professor):
        self.nome, self.professor, self.faixas = nome, professor, []

    def adicionar_faixa(self, faixa):
        self.faixas.append(faixa)

    def iniciar(self):
        while True:
            print(f"\n🌱 Olá, eu sou o {self.nome}.")
            print(f"Bem-vindo(a), {self.professor.nome}! 🎓")
            print(f"Turma: {self.professor.turma} | Escola: {self.professor.escola}")
            print("\nEscolha a faixa etária da sua turma:")
            for i, f in enumerate(self.faixas, 1):
                print(f"[{i}] {f.nome} ({f.idade_min}-{f.idade_max} anos)")
            print("[0] Sair")

            try:
                idx = int(input("Digite o número: "))
                if idx == 0:
                    print("👋 Até logo! Continue espalhando sustentabilidade!")
                    break
                elif 1 <= idx <= len(self.faixas):
                    resultado = self.menu(self.faixas[idx - 1])
                    if resultado == "sair":
                        print("👋 Até logo! Continue espalhando sustentabilidade!")
                        break
                else:
                    print("⚠️ Faixa etária inválida. Tente novamente.")
            except ValueError:
                print("⚠️ Entrada inválida. Digite apenas números.")

    def menu(self, faixa):
        while True:
            print(f"\n🎯 Faixa escolhida: {faixa.nome}")
            print("[1] Didáticas\n[2] Temas\n[9] Voltar\n[0] Sair")
            op = input("Escolha: ")
            if op == "1":
                faixa.crud(faixa.didaticas, "Didáticas")
            elif op == "2":
                faixa.crud(faixa.temas, "Temas")
            elif op == "9":
                return "voltar"
            elif op == "0":
                return "sair"
            else:
                print("⚠️ Opção inválida. Tente novamente.")


# -------- Programa Principal --------
if __name__ == "__main__":
    print("📌 Cadastro do Professor")
    nome = input("Digite seu nome: ")
    escola = input("Digite o nome da escola: ")
    turma = input("Digite a turma: ")

    prof = Professor(nome, escola, turma)

    rootbot = Chatbot("RootBot", prof)

    f1 = FaixaEtaria("Crianças", 6, 10)
    f1.didaticas.append(Item("Separação do lixo", "Atividade prática"))
    f1.temas.append(Item("Poluição dos rios", "Debate sobre descarte"))

    f2 = FaixaEtaria("Adolescentes", 11, 14)
    f2.didaticas.append(Item("Horta escolar", "Plantio de vegetais"))
    f2.temas.append(Item("Aquecimento global", "Palestra interativa"))

    f3 = FaixaEtaria("Jovens", 15, 18)
    f3.didaticas.append(Item("Energia solar", "Oficina sobre energia limpa"))
    f3.temas.append(Item("Consumo consciente", "Discussão sobre hábitos sustentáveis"))

    for f in (f1, f2, f3):
        rootbot.adicionar_faixa(f)

    rootbot.iniciar()
