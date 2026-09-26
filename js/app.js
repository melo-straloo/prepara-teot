"use strict";

/* ============ Config ============ */
const BLOCOS = [
  { slug: "principios-trauma-pelve", area: "Princípios do Trauma, Politrauma e Pelve/Acetábulo" },
  { slug: "trauma-membro-superior", area: "Trauma do Adulto — Membro Superior" },
  { slug: "trauma-membro-inferior", area: "Trauma do Adulto — Membro Inferior" },
  { slug: "trauma-pediatrico", area: "Trauma Pediátrico" },
  { slug: "ortopedia-pediatrica", area: "Ortopedia Pediátrica" },
  { slug: "joelho", area: "Joelho e Medicina Esportiva" },
  { slug: "quadril", area: "Quadril do Adulto" },
  { slug: "ombro-cotovelo-mao", area: "Ombro, Cotovelo e Mão" },
  { slug: "coluna", area: "Coluna Vertebral" },
  { slug: "pe-onco-diversos", area: "Pé/Tornozelo, Oncologia, Infecção e Metabólicas" },
];
const DATA_TEORICA = new Date("2027-01-10T09:00:00-03:00");
const DATA_PRATICA = new Date("2027-02-26T08:00:00-03:00");
const FIM_INSCRICAO = new Date("2026-09-30T17:00:00-03:00");
const SIMULADO_TOTAL = 120;
const SIMULADO_DURACAO_MS = 4 * 60 * 60 * 1000;

/* ============ Estado ============ */
const bancos = {}; // slug -> {area, questoes} | null (indisponível)
let carregado = false;
let simulado = null; // estado do simulado em andamento

/* ============ Utilidades ============ */
const $ = (sel) => document.querySelector(sel);
const LETRAS = ["A", "B", "C", "D"];

function embaralhar(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function lerProgresso() {
  try { return JSON.parse(localStorage.getItem("teotProgresso") || "{}"); }
  catch { return {}; }
}
function gravarResposta(qid, correta) {
  const p = lerProgresso();
  if (!p[qid]) { p[qid] = { c: correta }; localStorage.setItem("teotProgresso", JSON.stringify(p)); }
}
function lerSimulados() {
  try { return JSON.parse(localStorage.getItem("teotSimulados") || "[]"); }
  catch { return []; }
}

function escaparHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

/* ============ Roteamento ============ */
const ROTAS = ["inicio", "plano", "questoes", "simulado", "recursos"];
function rota() {
  const h = location.hash.replace("#", "");
  return ROTAS.includes(h) ? h : "inicio";
}
function renderRota() {
  const r = rota();
  ROTAS.forEach((v) => { const el = $("#view-" + v); if (el) el.hidden = v !== r; });
  document.querySelectorAll("#nav a").forEach((a) => a.classList.toggle("active", a.dataset.route === r));
  if (r === "inicio") renderPainel();
  if (r === "questoes") renderAreas();
  if (r === "simulado") renderSimuladoHome();
  window.scrollTo(0, 0);
}
window.addEventListener("hashchange", renderRota);

/* ============ Contagem regressiva ============ */
function diasAte(data) {
  return Math.max(0, Math.ceil((data - Date.now()) / 86400000));
}
function renderContagens() {
  const t = $("#cd-teorica"), p = $("#cd-pratica");
  if (t) t.textContent = diasAte(DATA_TEORICA) + " dias";
  if (p) p.textContent = diasAte(DATA_PRATICA) + " dias";
  const alerta = $("#alerta-inscricao");
  if (alerta && Date.now() > FIM_INSCRICAO.getTime()) alerta.hidden = true;
}

/* ============ Carga dos bancos ============ */
async function carregarBancos() {
  await Promise.all(BLOCOS.map(async (b) => {
    try {
      const resp = await fetch("data/" + b.slug + ".json", { cache: "no-store" });
      if (!resp.ok) throw new Error(String(resp.status));
      const json = await resp.json();
      if (!Array.isArray(json.questoes) || json.questoes.length === 0) throw new Error("vazio");
      bancos[b.slug] = json;
    } catch {
      bancos[b.slug] = null;
    }
  }));
  carregado = true;
  renderRota();
}

function questoesDisponiveis() {
  return BLOCOS.flatMap((b) => (bancos[b.slug] ? bancos[b.slug].questoes.map((q) => ({ ...q, slug: b.slug, area: b.area })) : []));
}

/* ============ Painel de progresso (início) ============ */
function renderPainel() {
  const el = $("#painel-progresso");
  if (!el) return;
  if (!carregado) { el.innerHTML = '<div class="card"><p class="text-secondary">Carregando o banco de questões…</p></div>'; return; }
  const prog = lerProgresso();
  const todas = questoesDisponiveis();
  const respondidas = todas.filter((q) => prog[q.id]);
  const acertos = respondidas.filter((q) => prog[q.id].c).length;
  const sims = lerSimulados();
  const ultimo = sims[sims.length - 1];
  el.innerHTML = `
    <div class="card stat"><p class="stat-value">${respondidas.length} / ${todas.length}</p>
      <p class="stat-label">questões respondidas no banco.</p></div>
    <div class="card stat"><p class="stat-value">${respondidas.length ? Math.round((100 * acertos) / respondidas.length) + "%" : "—"}</p>
      <p class="stat-label">de acerto nas questões respondidas. A meta na reta final é 75%.</p></div>
    <div class="card stat"><p class="stat-value">${ultimo ? ultimo.acertos + " / " + ultimo.total : "—"}</p>
      <p class="stat-label">${ultimo ? "no seu último simulado (" + ultimo.data + ")." : "Você ainda não fez um simulado completo."}</p></div>`;
}

/* ============ Banco de questões ============ */
function renderAreas() {
  const lista = $("#lista-areas");
  $("#questoes-pratica").hidden = true;
  $("#questoes-home").hidden = false;
  if (!carregado) { lista.innerHTML = '<div class="card"><p class="text-secondary">Carregando os blocos…</p></div>'; return; }
  const prog = lerProgresso();
  lista.innerHTML = BLOCOS.map((b) => {
    const banco = bancos[b.slug];
    if (!banco) {
      return `<div class="card area-card"><h3>${escaparHtml(b.area)}</h3>
        <p class="area-meta">Bloco em preparação. Ele aparece aqui automaticamente assim que for publicado.</p></div>`;
    }
    const n = banco.questoes.length;
    const resp = banco.questoes.filter((q) => prog[q.id]);
    const acertos = resp.filter((q) => prog[q.id].c).length;
    const pct = resp.length ? Math.round((100 * acertos) / resp.length) : null;
    return `<div class="card area-card">
      <h3>${escaparHtml(banco.area)}</h3>
      <p class="area-meta">${n} questões · ${resp.length} respondidas${pct !== null ? " · " + pct + "% de acerto" : ""}</p>
      <div class="progressbar"><span class="${pct !== null && pct >= 70 ? "ok" : ""}" style="width:${Math.round((100 * resp.length) / n)}%"></span></div>
      <div><button class="btn btn-primary" data-praticar="${b.slug}">Praticar</button></div>
    </div>`;
  }).join("");
  lista.querySelectorAll("[data-praticar]").forEach((btn) =>
    btn.addEventListener("click", () => iniciarPratica(btn.dataset.praticar)));
}

let pratica = null;
function iniciarPratica(slug) {
  const banco = bancos[slug];
  if (!banco) return;
  const prog = lerProgresso();
  const naoRespondidas = banco.questoes.filter((q) => !prog[q.id]);
  const jaRespondidas = banco.questoes.filter((q) => prog[q.id]);
  pratica = { slug, area: banco.area, fila: embaralhar(naoRespondidas).concat(embaralhar(jaRespondidas)), i: 0, acertos: 0, feitas: 0 };
  $("#questoes-home").hidden = true;
  $("#questoes-pratica").hidden = false;
  renderQuestaoPratica();
}

function renderQuestaoPratica() {
  const el = $("#questoes-pratica");
  const q = pratica.fila[pratica.i];
  if (!q) {
    el.innerHTML = `<div class="card"><h3>Bloco concluído</h3>
      <p>Você respondeu ${pratica.feitas} questões nesta sessão, com ${pratica.acertos} acertos.</p>
      <button class="btn btn-primary" id="btn-voltar-areas">Voltar aos blocos</button></div>`;
    $("#btn-voltar-areas").addEventListener("click", renderAreas);
    return;
  }
  el.innerHTML = `
    <div class="pratica-toolbar">
      <button class="btn btn-secondary" id="btn-voltar-areas">Voltar aos blocos</button>
      <p class="pratica-score">${escaparHtml(pratica.area)} · questão ${pratica.i + 1} de ${pratica.fila.length} · sessão: ${pratica.acertos}/${pratica.feitas} acertos</p>
    </div>
    <div class="card questao-card">
      <div class="questao-header">
        <div><span class="badge badge-tema">${escaparHtml(q.tema || "")}</span>
        <span class="badge badge-${q.dificuldade}">${q.dificuldade === "facil" ? "fácil" : q.dificuldade === "media" ? "média" : "difícil"}</span></div>
        <span class="text-secondary">${escaparHtml(q.id)}</span>
      </div>
      <p class="enunciado">${escaparHtml(q.enunciado)}</p>
      <div class="alternativas">${q.alternativas.map((a, idx) =>
        `<button class="alternativa" data-alt="${idx}"><span class="letra">${LETRAS[idx]}</span>${escaparHtml(a)}</button>`).join("")}</div>
      <div id="area-comentario"></div>
    </div>`;
  $("#btn-voltar-areas").addEventListener("click", renderAreas);
  el.querySelectorAll(".alternativa").forEach((btn) =>
    btn.addEventListener("click", () => responderPratica(parseInt(btn.dataset.alt, 10))));
}

function responderPratica(escolha) {
  const q = pratica.fila[pratica.i];
  const certo = escolha === q.correta;
  pratica.feitas++;
  if (certo) pratica.acertos++;
  gravarResposta(q.id, certo);
  document.querySelectorAll("#questoes-pratica .alternativa").forEach((btn, idx) => {
    btn.disabled = true;
    if (idx === q.correta) btn.classList.add("correta");
    else if (idx === escolha) btn.classList.add("errada");
  });
  $("#area-comentario").innerHTML = `
    <div class="comentario">
      <div class="alert ${certo ? "alert-success" : "alert-error"}">${certo ? "Você acertou." : "Resposta correta: " + LETRAS[q.correta] + "."}</div>
      <p>${escaparHtml(q.comentario)}</p>
      <p class="referencia">Referência: ${escaparHtml(q.referencia || "bibliografia oficial do edital")}</p>
      <button class="btn btn-primary" id="btn-proxima">Próxima questão</button>
    </div>`;
  $("#btn-proxima").addEventListener("click", () => { pratica.i++; renderQuestaoPratica(); });
  $("#btn-proxima").focus();
}

/* ============ Simulado ============ */
function montarProvaSimulado() {
  const porBloco = Math.floor(SIMULADO_TOTAL / BLOCOS.length);
  let prova = [];
  BLOCOS.forEach((b) => {
    const banco = bancos[b.slug];
    if (banco) prova = prova.concat(embaralhar(banco.questoes).slice(0, porBloco).map((q) => ({ ...q, area: b.area })));
  });
  const faltam = SIMULADO_TOTAL - prova.length;
  if (faltam > 0) {
    const usadas = new Set(prova.map((q) => q.id));
    const extras = embaralhar(questoesDisponiveis().filter((q) => !usadas.has(q.id))).slice(0, faltam);
    prova = prova.concat(extras);
  }
  return embaralhar(prova);
}

function renderSimuladoHome() {
  $("#simulado-prova").hidden = simulado === null;
  $("#simulado-home").hidden = simulado !== null;
  $("#simulado-resultado").hidden = true;
  const status = $("#simulado-status");
  if (status) {
    const n = questoesDisponiveis().length;
    status.textContent = !carregado ? "Carregando o banco de questões…"
      : n >= SIMULADO_TOTAL ? "" : n > 0 ? `Por enquanto há ${n} questões publicadas — o simulado usa todas as disponíveis.` : "O banco de questões ainda está sendo publicado. Volte em alguns minutos.";
    $("#btn-iniciar-simulado").disabled = !carregado || n === 0;
  }
  const hist = $("#historico-simulados");
  const sims = lerSimulados();
  if (hist) {
    hist.innerHTML = sims.length === 0 ? "" : `<h2>Seus simulados</h2>
      <table><thead><tr><th>Data</th><th>Resultado</th><th>Percentual</th><th>Situação (corte de 50%)</th></tr></thead><tbody>
      ${sims.map((s) => `<tr><td>${s.data}</td><td>${s.acertos} / ${s.total}</td><td>${Math.round((100 * s.acertos) / s.total)}%</td>
        <td>${s.acertos >= Math.ceil(s.total / 2) ? "Aprovado na 1ª fase" : "Abaixo do corte"}</td></tr>`).join("")}
      </tbody></table>`;
  }
  if (simulado) renderQuestaoSimulado();
}

function iniciarSimulado() {
  const prova = montarProvaSimulado();
  if (prova.length === 0) return;
  simulado = { prova, respostas: new Array(prova.length).fill(null), i: 0, fim: Date.now() + SIMULADO_DURACAO_MS, timer: null };
  simulado.timer = setInterval(atualizarTimer, 1000);
  renderSimuladoHome();
}

function atualizarTimer() {
  if (!simulado) return;
  const el = $("#sim-timer");
  const resta = simulado.fim - Date.now();
  if (resta <= 0) { entregarSimulado(); return; }
  if (el) {
    const h = Math.floor(resta / 3600000), m = Math.floor((resta % 3600000) / 60000), s = Math.floor((resta % 60000) / 1000);
    el.textContent = `${h}:${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
    el.classList.toggle("acabando", resta < 15 * 60000);
  }
}

function renderQuestaoSimulado() {
  const el = $("#simulado-prova");
  const q = simulado.prova[simulado.i];
  const respondidas = simulado.respostas.filter((r) => r !== null).length;
  el.innerHTML = `
    <div class="sim-toolbar">
      <span>Questão ${simulado.i + 1} de ${simulado.prova.length} · ${respondidas} respondidas</span>
      <span class="sim-timer" id="sim-timer">—</span>
      <button class="btn btn-primary" id="btn-entregar">Entregar prova</button>
    </div>
    <div class="sim-grid">${simulado.prova.map((_, idx) =>
      `<button data-ir="${idx}" class="${simulado.respostas[idx] !== null ? "respondida" : ""} ${idx === simulado.i ? "atual" : ""}">${idx + 1}</button>`).join("")}</div>
    <div class="card questao-card">
      <div class="questao-header">
        <span class="badge badge-tema">${escaparHtml(q.area)}</span>
        <span class="text-secondary">${escaparHtml(q.id)}</span>
      </div>
      <p class="enunciado">${escaparHtml(q.enunciado)}</p>
      <div class="alternativas">${q.alternativas.map((a, idx) =>
        `<button class="alternativa ${simulado.respostas[simulado.i] === idx ? "selecionada" : ""}" data-alt="${idx}">
          <span class="letra">${LETRAS[idx]}</span>${escaparHtml(a)}</button>`).join("")}</div>
      <div class="pratica-toolbar">
        <button class="btn btn-secondary" id="btn-ant" ${simulado.i === 0 ? "disabled" : ""}>Anterior</button>
        <button class="btn btn-secondary" id="btn-prox" ${simulado.i === simulado.prova.length - 1 ? "disabled" : ""}>Próxima</button>
      </div>
    </div>`;
  atualizarTimer();
  el.querySelectorAll(".alternativa").forEach((btn) => btn.addEventListener("click", () => {
    simulado.respostas[simulado.i] = parseInt(btn.dataset.alt, 10);
    if (simulado.i < simulado.prova.length - 1) simulado.i++;
    renderQuestaoSimulado();
  }));
  el.querySelectorAll("[data-ir]").forEach((btn) => btn.addEventListener("click", () => { simulado.i = parseInt(btn.dataset.ir, 10); renderQuestaoSimulado(); }));
  $("#btn-ant").addEventListener("click", () => { simulado.i--; renderQuestaoSimulado(); });
  $("#btn-prox").addEventListener("click", () => { simulado.i++; renderQuestaoSimulado(); });
  $("#btn-entregar").addEventListener("click", () => {
    const semResposta = simulado.respostas.filter((r) => r === null).length;
    const msg = semResposta > 0 ? `Você ainda tem ${semResposta} questões sem resposta. Entregar mesmo assim?` : "Entregar a prova e ver o resultado?";
    if (confirm(msg)) entregarSimulado();
  });
}

function entregarSimulado() {
  clearInterval(simulado.timer);
  const { prova, respostas } = simulado;
  const porArea = {};
  let acertos = 0;
  const erradas = [];
  prova.forEach((q, idx) => {
    const certo = respostas[idx] === q.correta;
    if (certo) acertos++;
    else erradas.push({ q, marcada: respostas[idx] });
    porArea[q.area] = porArea[q.area] || { total: 0, acertos: 0 };
    porArea[q.area].total++;
    if (certo) porArea[q.area].acertos++;
  });
  const total = prova.length;
  const corte = Math.ceil(total / 2);
  const sims = lerSimulados();
  sims.push({ data: new Date().toLocaleDateString("pt-BR"), acertos, total });
  localStorage.setItem("teotSimulados", JSON.stringify(sims));
  simulado = null;
  $("#simulado-prova").hidden = true;
  $("#simulado-home").hidden = true;
  const res = $("#simulado-resultado");
  res.hidden = false;
  res.innerHTML = `
    <h1>Resultado do simulado</h1>
    <div class="alert ${acertos >= corte ? "alert-success" : "alert-error"}">
      <strong>${acertos} acertos em ${total} questões (${Math.round((100 * acertos) / total)}%).</strong>
      ${acertos >= corte ? "Acima do corte de 50% da prova teórica." : `Abaixo do corte de 50% (${corte} acertos). Use o desempenho por área abaixo para redirecionar a semana de estudos.`}
    </div>
    <h2>Desempenho por área</h2>
    <table><thead><tr><th>Área</th><th>Acertos</th><th>Percentual</th></tr></thead><tbody>
      ${Object.entries(porArea).sort((a, b) => (a[1].acertos / a[1].total) - (b[1].acertos / b[1].total)).map(([area, d]) =>
        `<tr><td>${escaparHtml(area)}</td><td>${d.acertos} / ${d.total}</td><td>${Math.round((100 * d.acertos) / d.total)}%</td></tr>`).join("")}
    </tbody></table>
    ${erradas.length ? `<h2>Questões para revisar (${erradas.length})</h2>` : ""}
    ${erradas.map(({ q, marcada }) => `
      <div class="card">
        <div class="questao-header"><span class="badge badge-tema">${escaparHtml(q.area)}</span><span class="text-secondary">${escaparHtml(q.id)}</span></div>
        <p class="enunciado">${escaparHtml(q.enunciado)}</p>
        <p><strong>Correta: ${LETRAS[q.correta]}</strong> — ${escaparHtml(q.alternativas[q.correta])}<br>
        ${marcada !== null ? `Você marcou: ${LETRAS[marcada]}` : "Você deixou em branco"}</p>
        <p>${escaparHtml(q.comentario)}</p>
        <p class="text-secondary">Referência: ${escaparHtml(q.referencia || "bibliografia oficial do edital")}</p>
      </div>`).join("")}
    <button class="btn btn-primary" id="btn-novo-simulado">Voltar</button>`;
  $("#btn-novo-simulado").addEventListener("click", () => { res.hidden = true; renderSimuladoHome(); });
  window.scrollTo(0, 0);
}

/* ============ Inicialização ============ */
document.addEventListener("DOMContentLoaded", () => {
  renderContagens();
  setInterval(renderContagens, 60000);
  $("#btn-iniciar-simulado").addEventListener("click", iniciarSimulado);
  renderRota();
  carregarBancos();
});
