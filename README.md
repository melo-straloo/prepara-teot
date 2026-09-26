# Prepara TEOT 2027 · Straloo

Plataforma estática de preparação para o 56º TEOT (Título de Especialista em
Ortopedia e Traumatologia, SBOT): plano de estudos de 15 semanas, banco com
1.000 questões originais comentadas divididas em 10 blocos temáticos e
simulado no formato oficial (120 questões, 4 h, corte de 50%).

## Avisos

- **Material de estudo, não oficial.** As questões são originais, criadas com
  apoio de inteligência artificial a partir da bibliografia oficial do edital
  nº 2572 (AMB). Nenhuma questão oficial da SBOT é reproduzida. Recomenda-se
  revisão por especialista antes de uso além de demonstração.
- **Sem dados sensíveis.** A aplicação não tem backend nem coleta dados; o
  progresso do usuário fica em `localStorage` do navegador.

## Estrutura

- `index.html`, `css/`, `js/` — aplicação estática (sem build).
- `data/*.json` — blocos de questões (100 por bloco): `{area, slug, questoes[]}`,
  cada questão com `id`, `tema`, `enunciado`, `alternativas[4]`, `correta`,
  `comentario`, `referencia`, `dificuldade`.

## Desenvolvimento local

```bash
python3 -m http.server 8137
# http://localhost:8137
```

Publicado via GitHub Pages (branch `main`, raiz).
