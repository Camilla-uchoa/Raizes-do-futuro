# Raizes-do-futuro
🌱 RootBot — Chatbot de Educação Ambiental
RootBot é um chatbot simples escrito em Python (POO) que ajuda professores a escolher e gerenciar didáticas (atividades) e temas de educação ambiental por faixa etária.
Não é IA mágica — é um assistente programado, obediente e honesto: o professor faz escolhas, o bot responde. Prático, testável e fácil de estender.

🔎 Visão rápida
Público: professores que querem material prático e escalável para aulas de sustentabilidade.
Modo de uso: terminal/linha de comando.
Principais funcionalidades: cadastro do professor, seleção de faixa etária, CRUD de didáticas e temas (Create, Read, Update, Delete).
Objetivo: facilitar a preparação de aulas e gerar sugestões de atividades adequadas por idade.

⭐ Funcionalidades principais

-Cadastro de Professor (nome, escola, turma).
-Seleção de FaixaEtaria (nome, idade_min, idade_max).
-Gerenciamento de Didáticas e Temas por faixa (listas de Item com título e descrição).
-Menu interativo estilo “chatbot” com tratamento de entradas inválidas.
-Fluxo consistente: 9 = voltar | 0 = sair (de qualquer menu).

🧱 Arquitetura / Classes (resumo)

O projeto é organizado em classes simples e coesas:

Item
-Atributos: titulo, descricao
-Uso: representa uma didática ou um tema.
-__str__ para exibição legível.

FaixaEtaria
-Atributos: nome, idade_min, idade_max, didaticas (list), temas (list)
-Métodos: listar(lista), crud(lista, tipo) — implementa menu CRUD para cada lista.

Professor
-Atributos: nome, escola, turma
-Serve para personalizar a sessão.

Chatbot
-Atributos: nome, professor, faixas
-Métodos: adicionar_faixa(), iniciar(), menu(faixa) — controla todo o fluxo de interação.
