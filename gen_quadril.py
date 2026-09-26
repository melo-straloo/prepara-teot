# -*- coding: utf-8 -*-
import json

questoes = []

def add(tema, enunciado, alternativas, correta, comentario, dificuldade, referencia="Campbell's Operative Orthopaedics"):
    n = len(questoes) + 1
    questoes.append({
        "id": f"QUA-{n:03d}",
        "tema": tema,
        "enunciado": enunciado,
        "alternativas": alternativas,
        "correta": correta,
        "comentario": comentario,
        "referencia": referencia,
        "dificuldade": dificuldade,
    })

# ============================================================
# BLOCO 1 - IMPACTO FEMOROACETABULAR (15 questoes)
# ============================================================

add("Impacto femoroacetabular",
    "Homem de 28 anos, atleta amador de futebol, refere dor inguinal insidiosa que piora ao sentar por tempo prolongado e ao agachar. Ao exame, a flexão do quadril associada à rotação interna e adução reproduz a dor. Qual é o teste clínico descrito?",
    ["Teste de Thomas", "Teste de impacto anterior (FADIR)", "Teste de Trendelenburg", "Teste de Ober"],
    1,
    "O teste FADIR (flexão, adução e rotação interna) é o principal teste de rastreio para impacto femoroacetabular (IFA), reproduzindo a dor por compressão da junção cabeça-colo contra o lábio/rebordo acetabular anterior. Apesar de sensível, tem baixa especificidade, pois também é positivo em outras causas de dor intra-articular do quadril. O teste de Thomas avalia contratura em flexão do quadril, o Trendelenburg avalia insuficiência do glúteo médio e o teste de Ober avalia contratura do trato iliotibial.",
    "facil")

add("Impacto femoroacetafural",
    "Radiografia em incidência de Dunn modificada de um paciente com dor inguinal mostra perda do off-set entre a cabeça e o colo femoral, com aspecto de 'cabo de pistola' (pistol-grip deformity). Esse achado é característico de qual tipo de impacto femoroacetabular?",
    ["Impacto tipo pincer puro", "Impacto tipo CAM", "Displasia acetabular", "Protrusão acetabular"],
    1,
    "A deformidade em 'cabo de pistola' (pistol-grip) reflete um alfa-ângulo aumentado por perda da concavidade normal da junção cabeça-colo, achado clássico do impacto do tipo CAM. Esse excesso ósseo na região anterossuperior da cabeça-colo provoca lesão por cisalhamento no lábio e na cartilagem acetabular durante a flexão e rotação interna. O tipo pincer, ao contrário, decorre de sobrecobertura acetabular (ex.: retroversão acetabular ou coxa profunda). Muitos pacientes apresentam padrão misto CAM/pincer.",
    "media")

add("Impacto femoroacetabular",
    "No estudo radiográfico de bacia em AP de um paciente com suspeita de impacto tipo pincer por retroversão acetabular, qual sinal radiográfico indica cruzamento das paredes acetabulares anterior e posterior?",
    ["Sinal do cruzamento (crossover sign)", "Linha de Shenton interrompida", "Sinal da lágrima de Kohler", "Sinal do duplo contorno da cabeça femoral"],
    0,
    "O crossover sign (sinal do cruzamento) ocorre quando a linha da parede acetabular anterior cruza a linha da parede posterior antes de atingir o teto acetabular lateral, indicando retroversão acetabular relativa, um substrato para o impacto tipo pincer. A linha de Shenton avalia a congruência da articulação coxofemoral e é usada em displasia/fraturas. O sinal da lágrima é usado para medir a distância articular medial. O duplo contorno é observado em fraturas do teto acetabular.",
    "media")

add("Impacto femoroacetabular",
    "Qual exame de imagem é considerado o mais sensível para identificar lesões labrais e condrais associadas ao impacto femoroacetabular, permitindo ainda avaliar delaminação cartilaginosa?",
    ["Radiografia simples em AP de bacia", "Ressonância magnética com artrografia direta (artro-RM)", "Cintilografia óssea trifásica", "Ultrassonografia do quadril"],
    1,
    "A artro-RM (ressonância com contraste intra-articular) aumenta a sensibilidade para detectar rupturas labrais e lesões condrais precoces em comparação à RM convencional, pois o contraste distende a cápsula e delineia melhor o lábio e a superfície cartilaginosa. A radiografia simples é essencial para o diagnóstico morfológico (alfa-ângulo, cobertura acetabular), mas não avalia partes moles diretamente. Cintilografia e ultrassonografia têm papel limitado na avaliação de lábio/cartilagem intra-articular.",
    "media")

add("Impacto femoroacetabular",
    "Mulher de 32 anos com dor inguinal crônica e alfa-ângulo de 68° na incidência de Dunn a 45°. Foi submetida a tratamento conservador por 6 meses sem melhora. Qual é a conduta cirúrgica mais adequada para uma lesão CAM sintomática refratária, sem artrose avançada?",
    ["Artroplastia total do quadril", "Osteotomia periacetabular de Bernese", "Artroscopia do quadril com osteoplastia da junção cabeça-colo e reparo labral", "Artrodese do quadril"],
    2,
    "Na lesão CAM sintomática refratária ao tratamento conservador, sem artrose avançada (Tönnis 0-1), a artroscopia do quadril com osteoplastia da giba (correção do alfa-ângulo) associada ao reparo ou refixação labral é o tratamento de escolha, buscando eliminar o impacto mecânico e preservar a articulação nativa. A ATQ é reservada para artrose estabelecida. A osteotomia periacetabular trata displasia, não excesso de cobertura por CAM. A artrodese não tem indicação nesse contexto.",
    "media")

add("Impacto femoroacetabular",
    "Sobre o impacto tipo pincer, assinale a alternativa correta quanto à fisiopatologia da lesão labral associada.",
    ["A lesão labral tende a ser mais extensa e a cartilagem subjacente costuma estar preservada por mais tempo", "A cartilagem acetabular posteroinferior sofre lesão por contragolpe (contrecoup)", "O lábio sofre avulsão precoce da borda acetabular sem edema associado", "Não há relação entre pincer e degeneração labral"],
    1,
    "No impacto tipo pincer, o contato repetitivo entre o rebordo acetabular e a junção cabeça-colo gera alavancagem da cabeça femoral, produzindo lesão por contragolpe (contrecoup) na cartilagem posteroinferior, além de ossificação e espessamento do próprio lábio anterior. Isso contrasta com o CAM, em que a lesão condral anterossuperior é mais precoce e extensa, com lábio relativamente preservado inicialmente.",
    "dificil")

add("Impacto femoroacetabular",
    "Qual estrutura NÃO faz parte da tríade de estabilizadores estáticos habitualmente avaliada na investigação de instabilidade associada ao impacto femoroacetabular limítrofe (borderline dysplasia)?",
    ["Lábio acetabular", "Cápsula articular (ligamento iliofemoral)", "Ângulo de Wiberg (cobertura lateral)", "Trato iliotibial"],
    3,
    "O trato iliotibial é uma estrutura extra-articular relacionada à dor trocantérica lateral e ao ressalto externo, não sendo um estabilizador primário da articulação coxofemoral. Já o lábio, a cápsula (ligamento iliofemoral) e a cobertura óssea acetabular (ângulo de Wiberg) compõem os principais estabilizadores estáticos avaliados em quadris limítrofes entre impacto e displasia, situação clinicamente desafiadora pelo risco de piora da instabilidade com osteoplastia isolada.",
    "dificil")

add("Impacto femoroacetabular",
    "Na avaliação de um paciente jovem com dor no quadril, qual achado no exame físico é mais sugestivo de patologia intra-articular (como lesão labral) em vez de dor de origem extra-articular?",
    ["Dor à palpação da bursa trocantérica", "Sinal do 'C' (paciente aponta a dor formando um C com a mão sobre o trocanter e a virilha)", "Dor à palpação da tuberosidade isquiática", "Dor referida acompanhada de dormência posterior de coxa"],
    1,
    "O 'C-sign', em que o paciente coloca a mão em formato de C sobre o quadril lateral, abraçando a região trocantérica e a virilha, é classicamente associado a dor intra-articular do quadril, incluindo patologia labral. Dor localizada sobre a bursa trocantérica sugere síndrome da dor trocantérica maior (bursite/tendinopatia glútea), dor na tuberosidade isquiática sugere tendinopatia proximal dos isquiotibiais, e dormência posterior de coxa remete a comprometimento neurológico ou síndrome do piriforme.",
    "facil")

add("Impacto femoroacetabular",
    "Em relação ao alfa-ângulo utilizado no diagnóstico radiográfico do impacto tipo CAM, qual afirmação está correta?",
    ["É medido apenas na incidência em perfil de Lauenstein e valores acima de 30° já confirmam o diagnóstico clínico de IFA", "É o ângulo formado entre o eixo do colo femoral e uma linha do centro da cabeça até o ponto onde o contorno ultrapassa o raio de uma circunferência ideal; valores acima de 55-60° sugerem CAM", "Mede a inclinação do teto acetabular (ângulo de Tönnis)", "É utilizado exclusivamente para quantificar a versão acetabular"],
    1,
    "O alfa-ângulo quantifica a assimetria da junção cabeça-colo: traça-se um círculo que melhor se ajusta à cabeça femoral e mede-se o ângulo entre o eixo do colo e a linha que liga o centro da cabeça ao ponto em que o contorno ósseo ultrapassa esse círculo. Valores acima de 55-60° (a depender da incidência) sugerem deformidade tipo CAM, mas o diagnóstico de impacto é clínico-radiográfico, não apenas radiográfico isolado, já que a deformidade pode ser assintomática em parte da população.",
    "media")

add("Impacto femoroacetabular",
    "Homem de 24 anos, jogador de hóquei, com dor inguinal bilateral relacionada à atividade física. RM evidencia lesão labral anterossuperior bilateral e alfa-ângulo aumentado. Ele pergunta sobre o risco a longo prazo de não tratar a condição. Qual é a principal justificativa para tratar precocemente o impacto femoroacetabular sintomático?",
    ["O IFA não tratado está associado a maior risco de artrose precoce do quadril", "O IFA sempre evolui para necrose avascular da cabeça femoral", "O tratamento cirúrgico do IFA elimina o risco de artrose mesmo em fases tardias", "O IFA é uma condição autolimitada sem relação com degeneração articular"],
    0,
    "Evidências acumuladas relacionam o impacto femoroacetabular não tratado, especialmente a deformidade CAM, a lesão labral e condral progressiva e ao desenvolvimento de osteoartrose precoce do quadril, sobretudo em pacientes jovens e ativos. O IFA não causa necrose avascular por mecanismo direto. O tratamento cirúrgico visa reduzir a progressão da lesão condral, mas seu benefício é maior quando realizado antes de dano articular estabelecido, não revertendo artrose já instalada.",
    "facil")

add("Impacto femoroacetabular",
    "Qual das seguintes é uma complicação específica e temida da osteoplastia excessiva da junção cabeça-colo durante a artroscopia para tratamento de lesão CAM?",
    ["Fratura do colo femoral", "Osteonecrose da cabeça femoral por lesão da artéria retinacular", "Luxação anterior recidivante", "Paralisia do nervo femoral"],
    1,
    "A ressecção excessiva ou mal posicionada da giba óssea na junção cabeça-colo pode lesar os vasos retinaculares (ramos da artéria circunflexa femoral medial) que penetram na cápsula posterossuperior e nutrem a cabeça femoral, resultando em osteonecrose. Fratura do colo é uma complicação rara descrita quando a ressecção é muito profunda/extensa, mas o principal cuidado técnico visa preservar o suprimento vascular retinacular. Lesão do nervo femoral não é a complicação clássica associada a esse tempo cirúrgico.",
    "dificil")

add("Impacto femoroacetabular",
    "Sobre o tratamento conservador inicial do impacto femoroacetabular leve a moderado, qual conduta é adequada antes de indicar cirurgia?",
    ["Repouso absoluto por 6 meses associado a imobilização em órtese de quadril", "Fisioterapia com fortalecimento do core e da musculatura periarticular, modificação de atividades e anti-inflamatórios conforme necessário", "Infiltração intra-articular de corticoide semanal por tempo indeterminado", "Indicação imediata de artroscopia em todos os pacientes sintomáticos"],
    1,
    "O manejo inicial do IFA sintomático é conservador, incluindo fisioterapia orientada para fortalecimento do core e da musculatura estabilizadora do quadril, modificação de atividades que exacerbam os sintomas (agachamento profundo, rotação com carga) e uso criterioso de anti-inflamatórios. Infiltrações repetidas não são recomendadas pelo risco de efeitos deletérios sobre a cartilagem, e a cirurgia é reservada para casos refratários ao tratamento conservador adequado.",
    "facil")

add("Impacto femoroacetabular",
    "Em relação à via de acesso cirúrgica aberta clássica descrita por Ganz (luxação cirúrgica segura do quadril) para tratamento de IFA complexo, qual é o princípio fundamental que permite a preservação vascular da cabeça femoral?",
    ["Osteotomia trocantérica digástrica preservando o pedículo posterior (artéria circunflexa femoral medial) através do tendão do obturador externo", "Secção completa dos músculos rotadores externos curtos", "Abordagem anterior direta com capsulotomia extensa sem osteotomia trocantérica", "Ligadura proposital da artéria circunflexa femoral lateral"],
    0,
    "A técnica de luxação cirúrgica segura descrita por Ganz utiliza uma osteotomia trocantérica digástrica (flip osteotomy) que mantém a inserção dos músculos glúteo médio/mínimo e vasto lateral em continuidade, preservando o pedículo vascular posterior — a artéria circunflexa femoral medial — que trafega próximo ao tendão do obturador externo. Isso permite ampla exposição articular com baixo risco de osteonecrose, sendo referência histórica para o tratamento aberto de deformidades complexas de IFA.",
    "dificil")

add("Impacto femoroacetabular",
    "Paciente com impacto tipo CAM é submetido à artroscopia de quadril. No pós-operatório imediato, qual orientação de reabilitação é geralmente recomendada para proteger o reparo labral e a osteoplastia?",
    ["Carga total imediata e retorno ao esporte em 1 semana", "Uso de muletas com carga parcial protegida por algumas semanas e restrição de amplitude de rotação/flexão conforme protocolo, com retorno gradual ao esporte", "Imobilização gessada do quadril por 8 semanas", "Repouso absoluto no leito por 4 semanas sem mobilização"],
    1,
    "Após artroscopia de quadril com reparo labral e osteoplastia, o protocolo de reabilitação tipicamente inclui carga parcial protegida com muletas por algumas semanas, restrição temporária de amplitudes extremas (flexão profunda, rotação) para proteger o reparo labral e a cicatrização óssea, com progressão gradual de fortalecimento e retorno ao esporte em geral entre 4 e 6 meses. Imobilização gessada e repouso absoluto não são indicados, pois favorecem rigidez articular.",
    "media")

add("Impacto femoroacetabular",
    "Qual é a principal limitação da classificação de Tönnis na avaliação pré-operatória de pacientes com impacto femoroacetabular candidatos à preservação articular?",
    ["Ela avalia apenas a versão femoral", "Ela foi desenhada para graduar osteoartrose radiográfica geral e não é específica para quantificar lesão condral focal do IFA", "Ela só pode ser aplicada em crianças", "Ela substitui a necessidade de ressonância magnética em todos os casos"],
    1,
    "A classificação de Tönnis graduaa osteoartrose do quadril de forma global (0 a 3) com base em osteófitos, esclerose subcondral e redução do espaço articular, sendo útil para triagem de candidatos à cirurgia de preservação (idealmente grau 0-1), mas não descreve a localização ou extensão focal da lesão condral associada ao IFA, que exige avaliação artroscópica ou de imagem avançada (RM/artro-RM) complementar.",
    "dificil")

add("Impacto femoroacetabular",
    "Um homem de 35 anos com IFA tipo CAM leve e cobertura acetabular normal apresenta dor articular ocasional, sem limitação funcional significativa e sem sinais de artrose na radiografia. Qual é a conduta inicial mais apropriada?",
    ["Osteotomia periacetabular imediata", "Observação clínica com orientações de atividade e reavaliação, reservando cirurgia para sintomas persistentes ou progressivos", "Artroplastia total do quadril profilática", "Artrodese do quadril"],
    1,
    "Deformidades morfológicas tipo CAM são frequentes na população geral e podem ser assintomáticas ou minimamente sintomáticas. Em pacientes com sintomas leves, função preservada e sem evidência de dano articular estrutural, a conduta inicial é observação, orientação sobre atividades e reavaliação clínica, reservando-se o tratamento cirúrgico para casos com sintomas persistentes, progressivos ou limitantes, apesar de medidas conservadoras.",
    "media")

# ============================================================
# BLOCO 2 - DISPLASIA DO QUADRIL NO ADULTO (10 questoes)
# ============================================================

add("Displasia do quadril no adulto",
    "Mulher de 26 anos com dor inguinal e claudicação leve. Radiografia de bacia mostra ângulo centro-borda lateral de Wiberg de 12°. Esse achado é compatível com qual diagnóstico?",
    ["Impacto tipo pincer", "Displasia acetabular do adulto", "Coxa profunda", "Protrusão acetabular"],
    1,
    "O ângulo centro-borda (CE) de Wiberg avalia a cobertura lateral da cabeça femoral pelo acetábulo; valores abaixo de 20-25° indicam cobertura insuficiente, característica da displasia acetabular do adulto. Esse déficit de cobertura aumenta a sobrecarga no lábio e na cartilagem acetabular anterolateral, predispondo à degeneração precoce. Pincer e coxa profunda representam sobrecobertura acetabular, e protrusão acetabular refere-se à migração medial da cabeça femoral além da linha ilioisquiática, achados opostos ao descrito.",
    "facil")

add("Displasia do quadril no adulto",
    "Qual índice radiográfico avalia a inclinação do teto acetabular (obliquidade) e é utilizado tanto em crianças quanto, de forma adaptada, na avaliação de displasia residual do adulto?",
    ["Índice acetabular (ângulo de Tönnis/ângulo do teto acetabular)", "Índice de Böhler", "Ângulo de Baumann", "Ângulo de Cobb"],
    0,
    "O índice acetabular (ou ângulo do teto acetabular/ângulo de Tönnis) mede a obliquidade do teto acetabular em relação a uma linha horizontal de referência, sendo fundamental na avaliação da displasia do desenvolvimento do quadril e de sua repercussão residual no adulto. O índice de Böhler é usado no calcâneo, o ângulo de Baumann no cotovelo pediátrico e o ângulo de Cobb na avaliação de escoliose.",
    "media")

add("Displasia do quadril no adulto",
    "Mulher de 24 anos com displasia acetabular sintomática (CE lateral de 15°), sem artrose (Tönnis 0), com boa congruência articular e cartilagem preservada na RM. Qual é o tratamento cirúrgico de escolha para redirecionar a cobertura acetabular e preservar a articulação nativa?",
    ["Artroplastia total do quadril", "Osteotomia periacetabular de Bernese (Ganz)", "Osteotomia de Salter", "Artrodese do quadril"],
    1,
    "A osteotomia periacetabular de Bernese (PAO), descrita por Ganz, é o procedimento de escolha em adultos jovens com displasia sintomática e cartilagem preservada, pois permite reorientação tridimensional do fragmento acetabular mantendo a integridade da coluna posterior e a vascularização, sem violar o anel pélvico, corrigindo a cobertura da cabeça femoral e postergando/evitando a artroplastia. A osteotomia de Salter é técnica pediátrica. ATQ e artrodese não preservam a articulação nativa.",
    "media")

add("Displasia do quadril no adulto",
    "Qual é a principal vantagem da osteotomia periacetabular de Bernese em comparação a outras osteotomias pélvicas mais antigas no tratamento da displasia do adulto jovem?",
    ["Permite grande correção multiplanar mantendo a integridade da coluna posterior do acetábulo e possibilita parto vaginal futuro sem alteração relevante do canal do parto", "É tecnicamente mais simples e não exige controle radioscópico intraoperatório", "Elimina a necessidade de fisioterapia no pós-operatório", "Está indicada preferencialmente em pacientes com esqueleto imaturo"],
    0,
    "A PAO de Bernese preserva a integridade da coluna posterior do acetábulo (íntegra e vascularizada), permite correção tridimensional ampla da cobertura acetabular e mantém o anel pélvico praticamente intacto, o que possibilita evolução obstétrica sem grandes restrições ao canal de parto, ao contrário de osteotomias que alteram significativamente o diâmetro pélvico. É tecnicamente exigente e requer controle radioscópico rigoroso, sendo indicada em pacientes com cartilagem trirradiada fechada (esqueleto maduro).",
    "dificil")

add("Displasia do quadril no adulto",
    "Homem de 45 anos com displasia acetabular não tratada na infância evolui com dor crônica e radiografia mostrando Tönnis grau 3, com colapso articular avançado. Nesse estágio, qual é a conduta mais apropriada?",
    ["Osteotomia periacetabular isolada", "Artroplastia total do quadril", "Osteotomia de reorientação femoral isolada", "Observação clínica indefinida"],
    1,
    "Em displasia com artrose avançada (Tönnis 2-3) e colapso articular estabelecido, a osteotomia periacetabular perde a indicação, pois não reverte o dano condral já instalado; nesses casos, a artroplastia total do quadril é o tratamento definitivo. É importante lembrar que quadris displásicos frequentemente apresentam desafios técnicos na ATQ, como acetábulo raso, colo femoral anteversao aumentada e possível necessidade de enxerto ósseo ou implantes de menor tamanho.",
    "facil")

add("Displasia do quadril no adulto",
    "Durante o planejamento de uma artroplastia total do quadril em paciente com displasia de Crowe tipo IV (luxação alta), qual é uma preocupação técnica importante relacionada ao comprimento do membro e às estruturas neurovasculares?",
    ["Não há risco aumentado de lesão neurológica nesse cenário", "O alongamento excessivo do membro ao reduzir a cabeça femoral para o nível do verdadeiro acetábulo aumenta o risco de lesão do nervo isquiático, podendo exigir encurtamento femoral subtrocantérico", "A via de acesso posterior está contraindicada em todos os casos de Crowe IV", "O componente acetabular deve sempre ser posicionado no falso acetábulo para evitar tração neural"],
    1,
    "Em displasias graves com luxação alta (Crowe III-IV), reposicionar a cabeça femoral no acetábulo verdadeiro pode gerar alongamento significativo do membro, aumentando o risco de neuropraxia ou lesão permanente do nervo isquiático (e eventualmente femoral) por tração excessiva. Uma estratégia técnica para mitigar esse risco é o encurtamento femoral subtrocantérico associado à fixação com haste não cimentada, permitindo a redução segura sem sobrecarga neural.",
    "dificil")

add("Displasia do quadril no adulto",
    "Na classificação de Crowe para displasia do quadril no adulto, o grau é determinado principalmente por qual parâmetro?",
    ["Grau de esclerose subcondral do teto acetabular", "Percentual de subluxação/migração proximal da cabeça femoral em relação ao acetábulo verdadeiro, medido em radiografia AP de bacia", "Presença de cistos acetabulares", "Espessura do lábio acetabular na RM"],
    1,
    "A classificação de Crowe quantifica o grau de subluxação/luxação da cabeça femoral em relação ao acetábulo verdadeiro na radiografia AP de bacia, utilizando a proporção de migração proximal da cabeça em relação ao diâmetro da cabeça femoral (ou altura pélvica), variando de I (leve, <50%) a IV (luxação alta, >100%). É amplamente utilizada no planejamento pré-operatório de ATQ em displasia, pois orienta a necessidade de encurtamento femoral e o tamanho do componente acetabular.",
    "media")

add("Displasia do quadril no adulto",
    "Qual achado é característico do quadril displásico do adulto quando comparado ao quadril normal, relevante para o planejamento de componentes acetabulares na artroplastia?",
    ["Acetábulo profundo com excesso de cobertura posterior", "Acetábulo raso, com deficiência de cobertura anterolateral e frequente retroversão", "Ausência completa da cavidade acetabular", "Aumento do offset femoral e colo femoral em varo acentuado"],
    1,
    "O acetábulo displásico é tipicamente raso, com cobertura anterolateral deficiente e, em muitos casos, retrovertido, o que dificulta a obtenção de estabilidade primária de componentes não cimentados padrão, podendo exigir componentes de menor diâmetro, uso de parafusos suplementares, enxerto ósseo autólogo (da própria cabeça femoral) ou implantes específicos para displasia. O colo femoral na displasia tende a apresentar anteversão aumentada, e não varo acentuado.",
    "media")

add("Displasia do quadril no adulto",
    "Sobre a osteotomia periacetabular de Bernese, qual estrutura neurovascular está em risco durante a osteotomia isquiática e deve ser cuidadosamente protegida?",
    ["Nervo isquiático", "Nervo obturador e vasos obturatórios", "Nervo femoral", "Nervo pudendo"],
    1,
    "Durante a osteotomia isquiática (um dos quatro cortes da PAO), o nervo obturador e os vasos obturatórios, que cursam próximos à porção inferior do ísquio e ao forame obturador, estão em risco de lesão caso a osteotomia seja realizada sem proteção adequada ou com direção inadequada da lâmina/cinzel. O nervo isquiático está mais relacionado ao risco durante a osteotomia ilíaca posterior e a manipulação intraoperatória geral, mas o nervo obturador é a estrutura classicamente associada ao corte isquiático.",
    "dificil")

add("Displasia do quadril no adulto",
    "Mulher de 30 anos com displasia leve bilateral (CE de 18° à direita) é assintomática e realiza corrida recreativa. Radiografia sem sinais de artrose. Qual é a conduta mais adequada neste momento?",
    ["Indicar PAO bilateral profilática imediatamente", "Acompanhamento clínico-radiográfico periódico, orientação sobre sinais de alerta e atividades, reservando cirurgia para caso de sintomas ou evidência de progressão", "Indicar artroplastia total do quadril bilateral", "Prescrever infiltração intra-articular de corticoide bilateral profilática"],
    1,
    "Em displasia leve assintomática, sem evidência de dano articular, a conduta é o acompanhamento clínico e radiográfico periódico, pois nem todo quadril displásico evolui necessariamente para artrose sintomática precoce, e a cirurgia profilática em paciente assintomático não é consensual. A decisão cirúrgica (como PAO) deve ser individualizada, geralmente reservada a pacientes sintomáticos ou com evidência de progressão/risco alto de degeneração.",
    "media")

# ============================================================
# BLOCO 3 - OSTEONECROSE DA CABECA FEMORAL (12 questoes)
# ============================================================

add("Osteonecrose da cabeça femoral",
    "Qual das opções a seguir é o fator de risco mais classicamente associado à osteonecrose atraumática da cabeça femoral?",
    ["Uso crônico de corticosteroides e etilismo", "Hipotireoidismo leve", "Uso de anti-inflamatório não hormonal por curto período", "Diabetes mellitus tipo 2 bem controlado"],
    0,
    "O uso crônico/em altas doses de corticosteroides e o etilismo importante são os fatores de risco não traumáticos mais fortemente associados à osteonecrose da cabeça femoral, acreditando-se que ambos promovam alterações no metabolismo lipídico e microembolização gordurosa nos vasos subcondrais. Outras causas incluem doença falciforme, doença de Gaucher, barotrauma (doença descompressiva), lúpus e coagulopatias. Diabetes bem controlado e AINE em curto prazo não são fatores de risco clássicos.",
    "facil")

add("Osteonecrose da cabeça femoral",
    "Paciente com osteonecrose da cabeça femoral apresenta radiografia normal, porém RM evidencia lesão em banda subcondral com edema ósseo, sem colapso da cabeça femoral. Segundo a classificação de Ficat e Arlet modificada, esse estágio corresponde a:",
    ["Estágio 0", "Estágio I", "Estágio II", "Estágio III"],
    1,
    "No estágio I de Ficat e Arlet, a radiografia simples é normal ou apresenta discretas alterações, mas a RM já demonstra alterações características de osteonecrose (linha em banda subcondral, edema ósseo), sendo o método mais sensível para diagnóstico precoce. O estágio 0 corresponde a quadril assintomático com imagem normal (geralmente identificado por rastreio do quadril contralateral). O estágio II mostra alterações radiográficas (esclerose, cistos) sem colapso, e o estágio III mostra o sinal do crescente (colapso subcondral) sem achatamento significativo da cabeça.",
    "media")

add("Osteonecrose da cabeça femoral",
    "Qual achado radiográfico define o estágio III de Ficat e Arlet na osteonecrose da cabeça femoral?",
    ["Esclerose e cistos sem alteração do contorno da cabeça femoral", "Sinal do crescente (crescent sign) com colapso subcondral, mas sem achatamento significativo do contorno da cabeça", "Achatamento acentuado da cabeça femoral com diminuição do espaço articular e osteófitos", "Radiografia completamente normal"],
    1,
    "O estágio III é caracterizado pelo colapso subcondral, evidenciado radiograficamente pelo sinal do crescente (crescent sign — uma linha radiolucente subcondral curvilínea), representando fratura subcondral sem ainda haver achatamento acentuado da cabeça femoral. O estágio II apresenta apenas esclerose/cistos sem alteração de contorno, e o estágio IV apresenta achatamento da cabeça com estreitamento do espaço articular e alterações acetabulares secundárias (artrose secundária).",
    "media")

add("Osteonecrose da cabeça femoral",
    "Homem de 34 anos com osteonecrose bilateral da cabeça femoral, Ficat I-II, sem colapso, área de acometimento pequena a média (segundo classificação de extensão), com dor moderada. Qual é a opção terapêutica cirúrgica mais indicada nesse estágio para tentar preservar a articulação?",
    ["Artroplastia total do quadril bilateral imediata", "Descompressão do núcleo (core decompression), associada ou não a enxerto/fatores biológicos", "Artrodese bilateral do quadril", "Osteotomia periacetabular de Bernese"],
    1,
    "Nos estágios pré-colapso (Ficat 0-II/ARCO 0-II), a descompressão do núcleo (core decompression) é a intervenção cirúrgica mais utilizada para tentar preservar a cabeça femoral, aliviando a pressão intraóssea e estimulando revascularização; pode ser associada a enxerto ósseo, concentrado de medula óssea ou outros adjuvantes biológicos. Uma vez instalado colapso subcondral significativo (estágio III-IV), a descompressão perde eficácia, e a artroplastia total do quadril torna-se o tratamento de escolha.",
    "media")

add("Osteonecrose da cabeça femoral",
    "Qual é o principal determinante prognóstico relacionado ao risco de colapso da cabeça femoral na osteonecrose, além do estágio de Ficat/ARCO?",
    ["Idade cronológica do paciente exclusivamente", "Extensão/tamanho da lesão (percentual da superfície articular acometida) e sua localização (especialmente a porção de carga anterossuperior)", "Nível sérico de cálcio", "Cor da pele do paciente"],
    1,
    "Além do estágio evolutivo, a extensão da lesão necrótica (classicamente avaliada pelo percentual da superfície de carga acometida, com sistemas como o de Kerboul, que soma o arco de necrose nas incidências AP e perfil) e sua localização — sobretudo quando envolve a região anterossuperior de carga — são fortes preditores de colapso, sendo lesões pequenas e mediais associadas a melhor prognóstico e lesões grandes/laterais a maior risco de colapso precoce.",
    "dificil")

add("Osteonecrose da cabeça femoral",
    "Em relação à classificação ARCO (Association Research Circulation Osseous) para osteonecrose da cabeça femoral, qual é a principal diferença em relação à classificação de Ficat e Arlet original?",
    ["A ARCO não utiliza ressonância magnética em nenhum estágio", "A ARCO incorpora subdivisões quantitativas de extensão da lesão (percentual de acometimento) dentro de cada estágio, além de considerar achados de RM já no estágio inicial", "A ARCO elimina completamente o conceito de colapso subcondral", "A ARCO é aplicável apenas a osteonecrose do joelho"],
    1,
    "A classificação ARCO expandiu o sistema de Ficat e Arlet ao incorporar a RM como método diagnóstico já nos estágios mais precoces e ao adicionar subclassificações quantitativas (extensão da área acometida em percentual da superfície articular/volume da cabeça femoral) dentro de cada estágio, permitindo estratificação prognóstica mais refinada, além de manter o conceito central de colapso subcondral como marco evolutivo.",
    "dificil")

add("Osteonecrose da cabeça femoral",
    "Paciente com osteonecrose Ficat IV bilateral, com achatamento importante da cabeça femoral, estreitamento do espaço articular e dor incapacitante. Qual é o tratamento definitivo mais indicado?",
    ["Descompressão do núcleo isolada", "Artroplastia total do quadril", "Tratamento exclusivamente medicamentoso com bifosfonados", "Osteotomia rotacional transtrocantérica isolada sem prótese"],
    1,
    "No estágio IV (colapso acentuado com achatamento da cabeça femoral, incongruência articular e alterações acetabulares secundárias), a articulação já está irreversivelmente comprometida, e a artroplastia total do quadril é o tratamento de escolha para alívio da dor e restauração funcional. Técnicas de preservação como descompressão do núcleo ou osteotomias rotacionais perdem indicação nesse estágio avançado.",
    "facil")

add("Osteonecrose da cabeça femoral",
    "Qual doença hematológica é classicamente associada a maior risco de osteonecrose da cabeça femoral, frequentemente bilateral e em pacientes jovens?",
    ["Anemia ferropriva", "Doença falciforme (anemia falciforme)", "Talassemia minor isolada", "Deficiência de vitamina B12"],
    1,
    "A doença falciforme está fortemente associada à osteonecrose da cabeça femoral, decorrente de fenômenos vaso-oclusivos por falcização das hemácias nos pequenos vasos subcondrais, frequentemente acometendo pacientes jovens de forma bilateral. Outras condições hematológicas/sistêmicas associadas incluem doença de Gaucher, coagulopatias (trombofilias) e uso de corticosteroides em doenças hematológicas de base.",
    "facil")

add("Osteonecrose da cabeça femoral",
    "Sobre a fisiopatologia da osteonecrose induzida por corticosteroides, qual mecanismo é mais aceito atualmente?",
    ["Aumento da vascularização óssea com hiperperfusão da cabeça femoral", "Hipertrofia de adipócitos medulares e embolização gordurosa, associadas a aumento da pressão intraóssea e comprometimento da perfusão subcondral", "Ação direta bacteriana sobre o osso subcondral", "Estímulo direto da formação óssea trabecular sem alteração vascular"],
    1,
    "Acredita-se que os corticosteroides promovam hipertrofia e hiperplasia de adipócitos na medula óssea, associadas a alterações do metabolismo lipídico sistêmico (hiperlipidemia), favorecendo embolização gordurosa e aumento da pressão intraóssea dentro do compartimento rígido da cabeça femoral, o que compromete a perfusão capilar subcondral e leva à morte celular óssea (osteonecrose), especialmente na região de carga anterossuperior.",
    "media")

add("Osteonecrose da cabeça femoral",
    "Homem de 40 anos, mergulhador profissional, desenvolve osteonecrose bilateral da cabeça femoral. Qual é o mecanismo fisiopatológico mais provável relacionado à sua atividade?",
    ["Doença descompressiva com formação de êmbolos de nitrogênio nos vasos ósseos", "Trauma direto repetitivo no quadril", "Infecção bacteriana por exposição à água", "Deficiência nutricional de vitamina D relacionada ao mergulho"],
    0,
    "Mergulhadores profissionais e trabalhadores expostos a variações de pressão barométrica estão sob risco de doença descompressiva (mal dos caçambeiros), na qual bolhas de nitrogênio formadas durante a descompressão rápida podem embolizar a microcirculação óssea, incluindo os vasos subcondrais da cabeça femoral, resultando em osteonecrose, frequentemente bilateral, mesmo na ausência de trauma direto.",
    "media")

add("Osteonecrose da cabeça femoral",
    "Em relação à descompressão do núcleo (core decompression) para osteonecrose pré-colapso, qual afirmação está correta quanto aos resultados esperados?",
    ["Os resultados são uniformemente ruins independentemente da extensão da lesão", "Os melhores resultados ocorrem em lesões pequenas, no estágio pré-colapso (Ficat 0-I e parte do II), sendo os resultados piores quando já há colapso subcondral estabelecido", "O procedimento é indicado preferencialmente em estágios com achatamento acentuado da cabeça femoral (Ficat IV)", "A técnica exige acesso aberto extenso com osteotomia trocantérica obrigatória"],
    1,
    "A descompressão do núcleo apresenta os melhores resultados em lesões pequenas e nos estágios pré-colapso (Ficat 0, I e parte do II), quando a integridade estrutural subcondral ainda não foi comprometida. Uma vez presente colapso subcondral (estágio III em diante), a taxa de sucesso cai significativamente, sendo a artroplastia preferida nesses casos. O procedimento é minimamente invasivo, realizado por via percutânea com perfuração guiada por radioscopia, sem necessidade de osteotomia trocantérica.",
    "dificil")

add("Osteonecrose da cabeça femoral",
    "Paciente jovem com osteonecrose segmentar pequena, Ficat II, localizada na porção medial (não relacionada à área principal de carga), assintomática, descoberta em investigação de dor no quadril contralateral. Qual conduta é mais apropriada?",
    ["Artroplastia total do quadril profilática imediata", "Observação clínica com seguimento radiográfico/RM periódico, dado o baixo risco de progressão de lesões pequenas e mediais", "Descompressão do núcleo obrigatória mesmo sem sintomas", "Osteotomia rotacional transtrocantérica imediata"],
    1,
    "Lesões de osteonecrose pequenas, especialmente quando localizadas fora da área principal de carga (região medial), têm menor propensão ao colapso e podem ser acompanhadas clinicamente com exames de imagem seriados, reservando intervenção cirúrgica para casos que se tornem sintomáticos ou apresentem evidência de progressão. Tratamento cirúrgico profilático em lesão pequena assintomática não é a conduta padrão.",
    "media")

# ============================================================
# BLOCO 4 - ARTROSE DO QUADRIL (8 questoes)
# ============================================================

add("Artrose do quadril",
    "Qual é o achado radiográfico clássico de osteoartrose do quadril em incidência AP de bacia?",
    ["Alargamento uniforme do espaço articular", "Redução assimétrica do espaço articular, esclerose subcondral, osteófitos marginais e cistos subcondrais", "Ausência completa de alterações ósseas com apenas edema de partes moles", "Erosões marginais simétricas bilaterais características de artrite reumatoide"],
    1,
    "A osteoartrose do quadril caracteriza-se radiograficamente por redução (geralmente assimétrica, mais acentuada na região de carga superolateral) do espaço articular, esclerose do osso subcondral, formação de osteófitos marginais (na cabeça femoral e acetábulo) e, eventualmente, cistos subcondrais (geodos). Erosões marginais simétricas são mais típicas de artropatias inflamatórias como artrite reumatoide, não de osteoartrose primária.",
    "facil")

add("Artrose do quadril",
    "Homem de 58 anos com dor inguinal mecânica leve a moderada, rigidez matinal breve e radiografia com Kellgren-Lawrence grau 2. Qual é a conduta inicial mais adequada antes de considerar tratamento cirúrgico?",
    ["Artroplastia total do quadril imediata", "Medidas conservadoras: perda de peso quando indicada, fisioterapia, analgésicos/AINE conforme necessário e modificação de atividades", "Osteotomia periacetabular", "Artrodese do quadril"],
    1,
    "O tratamento inicial da osteoartrose leve a moderada do quadril é conservador, incluindo orientação para perda de peso (quando aplicável), fisioterapia para fortalecimento muscular e manutenção de amplitude de movimento, uso racional de analgésicos e anti-inflamatórios, além de adaptação de atividades. A cirurgia (artroplastia) é reservada para casos com dor refratária e limitação funcional significativa apesar do tratamento conservador adequado.",
    "facil")

add("Artrose do quadril",
    "Qual das seguintes opções NÃO é considerada uma medida de tratamento conservador estabelecida para osteoartrose do quadril sintomática?",
    ["Fisioterapia e exercícios de fortalecimento muscular", "Uso de bengala contralateral ao quadril acometido", "Infiltração intra-articular de células-tronco mesenquimais como tratamento de primeira linha comprovadamente eficaz", "Perda de peso em pacientes com sobrepeso/obesidade"],
    2,
    "Apesar do interesse crescente em terapias biológicas (células-tronco, plasma rico em plaquetas) para osteoartrose, essas modalidades carecem de evidência robusta de eficácia para justificar seu uso rotineiro como primeira linha, não fazendo parte do arsenal conservador estabelecido pelas diretrizes atuais. Já fisioterapia, uso correto de bengala contralateral (reduz força de reação articular) e perda de peso são medidas conservadoras bem estabelecidas.",
    "media")

add("Artrose do quadril",
    "Em qual escala é feita a graduação radiográfica clássica da osteoartrose, amplamente utilizada também no quadril?",
    ["Classificação de Kellgren-Lawrence", "Classificação de Garden", "Classificação de Neer", "Classificação de Salter-Harris"],
    0,
    "A classificação de Kellgren-Lawrence, originalmente descrita para osteoartrose de joelho, é amplamente empregada também para graduar radiograficamente a osteoartrose do quadril (e outras articulações), variando de grau 0 (sem alterações) a grau 4 (alterações graves com grande redução do espaço articular, esclerose e osteófitos volumosos). Garden é usada em fraturas do colo do fêmur, Neer em fraturas/lesões do ombro e Salter-Harris em fraturas fisárias.",
    "facil")

add("Artrose do quadril",
    "Mulher de 62 anos com osteoartrose secundária a displasia leve, dor moderada há 2 anos, sem resposta adequada a fisioterapia e analgésicos, mas ainda com função aceitável e Kellgren-Lawrence grau 2. Antes de indicar artroplastia, qual alternativa pode ser considerada para alívio temporário da dor?",
    ["Infiltração intra-articular guiada de corticoide", "Osteotomia de bacia reconstrutiva mesmo com artrose já estabelecida", "Artrodese definitiva do quadril", "Ressecção artroplástica tipo Girdlestone eletiva"],
    0,
    "A infiltração intra-articular guiada (por radioscopia ou ultrassom) de corticoide pode proporcionar alívio sintomático temporário em pacientes com osteoartrose moderada que não respondem plenamente a medidas conservadoras iniciais, sendo também utilizada com finalidade diagnóstica (confirmar origem intra-articular da dor). Osteotomias reconstrutivas não são indicadas quando já há artrose estabelecida, e artrodese/Girdlestone são procedimentos de exceção, reservados a situações específicas (infecção, falha de múltiplas revisões).",
    "media")

add("Artrose do quadril",
    "Sobre a diferenciação entre dor articular (intra-articular) e dor trocantérica lateral em pacientes idosos com queixa de dor no quadril, qual característica favorece origem intra-articular (artrose)?",
    ["Dor localizada exclusivamente sobre o trocanter maior, piora ao deitar sobre o lado afetado", "Dor inguinal profunda, que piora com rotação interna e carga, podendo irradiar para a face anterior da coxa e joelho", "Dor que piora exclusivamente à palpação da bursa trocantérica sem relação com o movimento articular", "Dor exclusivamente noturna sem relação com atividade física"],
    1,
    "A dor de origem intra-articular na osteoartrose do quadril classicamente localiza-se na região inguinal profunda, piora com a rotação interna do quadril e com a carga/deambulação, podendo irradiar-se para a face anterior da coxa e, por vezes, joelho (dor referida pelo nervo obturador). Já a dor trocantérica lateral, relacionada à síndrome da dor trocantérica maior, localiza-se lateralmente sobre o trocanter, piorando ao deitar sobre o lado afetado e à palpação direta da região.",
    "media")

add("Artrose do quadril",
    "Qual é o principal objetivo funcional da fisioterapia no manejo conservador da osteoartrose do quadril?",
    ["Aumentar a rigidez articular para reduzir a dor", "Fortalecer a musculatura periarticular (especialmente abdutores) e manter a amplitude de movimento, reduzindo sobrecarga articular", "Eliminar completamente a necessidade de qualquer atividade física", "Promover imobilização prolongada da articulação"],
    1,
    "A fisioterapia na osteoartrose do quadril visa fortalecer a musculatura periarticular, sobretudo os abdutores (glúteo médio), que ajudam a reduzir as forças de reação articular durante a marcha, além de preservar a amplitude de movimento e a função global do paciente, retardando a progressão da incapacidade. Imobilização prolongada e inatividade são contraproducentes, pois favorecem rigidez, atrofia muscular e piora funcional.",
    "facil")

add("Artrose do quadril",
    "Homem de 70 anos com osteoartrose grave do quadril (Kellgren-Lawrence grau 4), dor incapacitante em repouso e à noite, falha de tratamento conservador prolongado. Qual é a conduta mais apropriada?",
    ["Manter tratamento conservador indefinidamente, pois a cirurgia não traz benefício em idosos", "Indicar artroplastia total do quadril eletiva após avaliação clínica pré-operatória adequada", "Indicar apenas infiltrações seriadas de ácido hialurônico como tratamento definitivo", "Indicar osteotomia periacetabular"],
    1,
    "Em pacientes com osteoartrose avançada e dor incapacitante refratária ao tratamento conservador, a artroplastia total do quadril é o tratamento definitivo com excelentes resultados em alívio da dor e melhora funcional, sendo amplamente indicada mesmo em pacientes idosos após avaliação e otimização clínica pré-operatória adequada (avaliação de comorbidades, risco cirúrgico e anestésico). Infiltrações seriadas e osteotomias não têm papel curativo em artrose avançada estabelecida.",
    "facil")

# ============================================================
# BLOCO 5 - ARTROPLASTIA TOTAL DO QUADRIL: TECNICA (15 questoes)
# ============================================================

add("Artroplastia total do quadril - técnica",
    "Durante uma artroplastia total do quadril por via posterolateral (Moore/Southern), qual nervo está classicamente em maior risco de lesão?",
    ["Nervo femoral", "Nervo isquiático (particularmente seu componente fibular/peroneal comum)", "Nervo obturador", "Nervo pudendo"],
    1,
    "A via posterolateral (Moore) expõe diretamente o nervo isquiático na região posterior do quadril, tornando-o a estrutura neural mais vulnerável durante essa abordagem, seja por tração, compressão por afastadores ou lesão direta. Classicamente, o componente fibular (peroneal comum) do nervo isquiático é mais suscetível à lesão do que o componente tibial, por ser mais superficial e menos móvel. O nervo femoral está mais relacionado a vias anteriores, e o obturador/pudendo a riscos específicos de outras etapas cirúrgicas.",
    "facil")

add("Artroplastia total do quadril - técnica",
    "Qual nervo está em maior risco durante a via de acesso anterolateral direta (Watson-Jones/Hardinge) à ATQ, relacionado à dissecção do intervalo entre tensor da fáscia lata e glúteo médio?",
    ["Nervo glúteo superior", "Nervo isquiático", "Nervo obturador", "Nervo cutâneo femoral lateral"],
    0,
    "Na via anterolateral (Hardinge/Watson-Jones), a dissecção e o afastamento excessivo do glúteo médio, especialmente se a incisão se estender muito proximalmente ao longo do intervalo com o tensor da fáscia lata, colocam em risco o ramo do nervo glúteo superior que inerva o próprio glúteo médio/mínimo e o tensor da fáscia lata, podendo causar fraqueza abdutora (marcha de Trendelenburg) se lesado. O nervo isquiático é mais relacionado à via posterior, o obturador a manipulações mediais/pélvicas, e o cutâneo femoral lateral à via anterior direta.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Na via de acesso anterior direta (Smith-Petersen) para ATQ, qual estrutura nervosa sensitiva está mais frequentemente em risco de lesão ou neuropraxia?",
    ["Nervo cutâneo femoral lateral", "Nervo isquiático", "Nervo glúteo inferior", "Nervo safeno"],
    0,
    "A via anterior direta utiliza o intervalo entre o sartório/tensor da fáscia lata e o reto femoral/glúteo médio, região por onde passa o nervo cutâneo femoral lateral, um nervo puramente sensitivo que inerva a face anterolateral da coxa. Sua lesão ou tração excessiva pode causar meralgia parestésica (dor/parestesia na coxa anterolateral), uma das queixas pós-operatórias mais comuns dessa via, geralmente sem repercussão motora.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Qual das vias de acesso para ATQ é classicamente associada à maior taxa de luxação pós-operatória quando a cápsula posterior e os rotadores externos curtos não são reparados adequadamente?",
    ["Via anterior direta", "Via posterolateral", "Via anterolateral (Hardinge)", "Via transtrocantérica"],
    1,
    "A via posterolateral, por seccionar a cápsula posterior e os rotadores externos curtos (piriforme, gêmeos, obturador interno), historicamente apresentava maior taxa de luxação posterior em comparação a vias que preservam essas estruturas, especialmente antes da popularização do reparo capsular e dos rotadores ao final do procedimento. Estudos demonstraram que o reparo meticuloso dessas estruturas reduz significativamente essa taxa, aproximando-a de outras vias.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Sobre pares tribológicos em artroplastia total do quadril, qual combinação apresenta a menor taxa de desgaste linear e volumétrico em estudos in vitro, sendo frequentemente indicada em pacientes jovens e ativos, apesar do risco de ruído articular (squeaking)?",
    ["Metal-polietileno convencional", "Cerâmica-cerâmica", "Metal-metal", "Cerâmica-polietileno altamente reticulado (cross-linked)"],
    1,
    "O par cerâmica-cerâmica apresenta as menores taxas de desgaste linear e volumétrico entre os pares tribológicos disponíveis, devido à excelente molhabilidade, dureza e baixa rugosidade superficial da cerâmica, sendo frequentemente considerado para pacientes jovens e ativos com maior expectativa de uso do implante. Seu principal inconveniente é o risco (ainda que baixo) de fratura do componente cerâmico e de ruído articular (squeaking), além de custo mais elevado.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Qual é a principal vantagem do polietileno altamente reticulado (highly cross-linked polyethylene) em relação ao polietileno convencional em artroplastia total do quadril?",
    ["Maior resistência à fratura mecânica sem qualquer contrapartida", "Redução significativa da taxa de desgaste e, consequentemente, menor incidência de osteólise associada a partículas de desgaste", "Eliminação completa do risco de luxação protética", "Maior custo com nenhuma vantagem mecânica comprovada"],
    1,
    "O polietileno altamente reticulado é produzido por irradiação em altas doses seguida de tratamento térmico, o que aumenta a ligação cruzada entre as cadeias poliméricas e reduz substancialmente a geração de partículas de desgaste em comparação ao polietileno convencional. Isso diminui a resposta inflamatória macrofágica e a osteólise periprotética associada, um dos principais mecanismos de falha a longo prazo da ATQ. Uma contrapartida é a discreta redução da resistência mecânica à fratura/propagação de trincas, compensada pelo processamento com adição de vitamina E em gerações mais recentes.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Em relação à fixação de componentes na artroplastia total do quadril, qual afirmação está correta sobre a fixação cimentada versus não cimentada do componente femoral?",
    ["A fixação não cimentada depende do crescimento/ingresso ósseo (osteointegração) na superfície porosa/revestida do implante e é preferida em pacientes jovens com boa qualidade óssea", "A fixação cimentada é contraindicada em qualquer paciente idoso", "A fixação não cimentada é preferida em ossos osteoporóticos muito frágeis pela maior estabilidade imediata", "Não há diferença biomecânica relevante entre os dois métodos"],
    0,
    "A fixação não cimentada baseia-se na osteointegração (crescimento ósseo) na superfície porosa ou revestida (ex.: hidroxiapatita) do implante, exigindo boa qualidade óssea e estabilidade primária adequada ('press-fit'), sendo geralmente preferida em pacientes mais jovens e ativos com osso de boa qualidade. Já a fixação cimentada oferece estabilidade imediata mesmo em ossos osteoporóticos ou de má qualidade, sendo frequentemente preferida em pacientes idosos ou com osso frágil, ao contrário do afirmado na alternativa C.",
    "media")

add("Artroplastia total do quadril - técnica",
    "No planejamento pré-operatório radiográfico (templating) de uma ATQ primária, qual é um dos principais objetivos ao definir o tamanho e posicionamento dos componentes?",
    ["Maximizar o comprimento do colo femoral sem considerar o offset", "Restaurar o centro de rotação do quadril, o offset femoral e a igualdade do comprimento dos membros inferiores", "Posicionar o componente acetabular na maior verticalização possível", "Utilizar sempre o maior componente femoral disponível independentemente do canal medular"],
    1,
    "O planejamento pré-operatório (templating) busca restaurar a biomecânica do quadril: posicionamento adequado do centro de rotação (evitando lateralização/medialização excessiva), restauração do offset femoral (importante para tensão dos abdutores e estabilidade), e correção/equalização do comprimento dos membros inferiores, além de estimar o tamanho apropriado dos componentes acetabular e femoral compatíveis com a anatomia do canal medular e do acetábulo do paciente.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Qual é a posição-alvo classicamente recomendada (zona segura de Lewinnek) para inclinação (abdução) e anteversão do componente acetabular na ATQ, visando reduzir o risco de luxação e desgaste excessivo?",
    ["Inclinação de 70±10° e anteversão de 30±10°", "Inclinação de 40±10° e anteversão de 15±10°", "Inclinação de 90° e anteversão de 0°", "Inclinação de 10±5° e anteversão de 45±10°"],
    1,
    "A zona segura clássica descrita por Lewinnek recomenda inclinação (abdução) do componente acetabular de aproximadamente 40° (±10°) e anteversão de aproximadamente 15° (±10°), valores associados a menor risco de luxação, impacto (impingement) e desgaste excessivo do polietileno. Embora estudos mais recentes questionem a aplicabilidade universal dessa 'zona segura' (dado o conceito de equilíbrio espinopélvico), ela permanece uma referência histórica fundamental no posicionamento acetabular.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Homem de 68 anos será submetido à ATQ primária por osteoartrose. Possui espondilite anquilosante com fusão lombar e retroversão pélvica funcional ao sentar. Qual conceito biomecânico deve ser especialmente considerado no planejamento do posicionamento acetabular nesse paciente?",
    ["O equilíbrio espinopélvico (spinopelvic balance), já que alterações na mobilidade da coluna lombossacra modificam a versão pélvica funcional e, consequentemente, a anteversão funcional do componente acetabular", "A anatomia da coluna lombar não influencia em nada o posicionamento do componente acetabular", "Apenas o ângulo de inclinação deve ser ajustado, sem necessidade de considerar a anteversão", "O comprimento do colo femoral é o único parâmetro relevante nesse cenário"],
    0,
    "Pacientes com rigidez da coluna lombossacra (ex.: espondilite anquilosante, artrodese lombar prévia) apresentam alteração do equilíbrio espinopélvico, com variação anormal da versão pélvica entre a posição sentada e ortostática. Isso modifica a anteversão funcional do componente acetabular durante o movimento, aumentando o risco de impacto e luxação caso o posicionamento cirúrgico não considere essa condição, exigindo avaliação individualizada (frequentemente com radiografias funcionais sentado/em pé) e possível ajuste da anteversão-alvo.",
    "dificil")

add("Artroplastia total do quadril - técnica",
    "Qual é a principal razão para preferir hastes femorais não cimentadas de fixação metafisária/diafisária em pacientes jovens submetidos à ATQ primária?",
    ["Menor custo do implante em comparação ao cimentado", "Maior expectativa de sobrevida do implante ao permitir osteointegração duradoura, evitando as limitações de fadiga do manto de cimento a longo prazo", "Eliminação total do risco de afrouxamento asséptico", "Menor tempo cirúrgico em todos os casos"],
    1,
    "Em pacientes jovens, com expectativa de uso prolongado do implante e, geralmente, boa qualidade óssea, prefere-se a fixação não cimentada por osteointegração, pois evita as limitações de fadiga e possível fragmentação do manto de cimento ao longo de décadas de uso, além de facilitar eventual revisão futura. Embora reduza certos mecanismos de falha, não elimina totalmente o risco de afrouxamento asséptico, que pode ocorrer por outras vias (ex.: osteólise por partículas de desgaste, estabilidade primária inadequada).",
    "media")

add("Artroplastia total do quadril - técnica",
    "Durante a via posterolateral, além do nervo isquiático, qual outra estrutura relevante deve ser identificada e protegida durante a dissecção dos rotadores externos curtos, para evitar sangramento significativo?",
    ["Artéria femoral superficial", "Artéria circunflexa femoral medial (ramo posterior, próximo ao músculo quadrado femoral)", "Artéria glútea superior isoladamente sem relação com rotadores", "Veia safena magna"],
    1,
    "A artéria circunflexa femoral medial, principal responsável pela vascularização da cabeça e colo femoral, apresenta um ramo posterior que cursa próximo à borda superior do músculo quadrado femoral e inferior ao piriforme, podendo ser lesado durante a liberação dos rotadores externos curtos na via posterolateral, resultando em sangramento significativo caso não seja identificado e cauterizado/ligado adequadamente.",
    "dificil")

add("Artroplastia total do quadril - técnica",
    "Qual é uma vantagem frequentemente citada da via de acesso anterior direta (Smith-Petersen/DAA) em relação à via posterolateral, sobretudo no período pós-operatório precoce?",
    ["Menor tempo cirúrgico em 100% dos casos, independentemente da experiência do cirurgião", "Abordagem intermuscular/internervosa verdadeira, com potencial de recuperação funcional mais rápida e menor taxa de luxação relatada em algumas séries", "Ausência completa de risco de lesão nervosa", "Exposição femoral superior à via posterolateral em todos os biotipos"],
    1,
    "A via anterior direta utiliza um intervalo verdadeiramente intermuscular e internervoso (entre sartório/tensor da fáscia lata e reto femoral/glúteo médio), preservando a musculatura abdutora e os rotadores posteriores, o que é associado em diversos estudos a recuperação funcional mais rápida no pós-operatório precoce e, em algumas séries, menor taxa de luxação. Não está isenta de riscos específicos (ex.: neuropraxia do cutâneo femoral lateral, fratura intraoperatória do trocanter) e pode apresentar exposição femoral mais desafiadora em pacientes obesos ou com fêmures musculosos.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Em relação ao offset femoral na artroplastia total do quadril, qual é a consequência funcional de um offset insuficiente (menor que o nativo)?",
    ["Aumento da tensão dos abdutores e redução do risco de luxação", "Redução do braço de alavanca dos abdutores, podendo causar marcha claudicante (Trendelenburg) e aumento teórico do risco de luxação e desgaste do polietileno por maior força de reação articular", "Alongamento excessivo do membro operado", "Nenhuma repercussão clínica relevante"],
    1,
    "Um offset femoral insuficiente reduz o braço de alavanca da musculatura abdutora (glúteo médio/mínimo), diminuindo sua eficiência mecânica, o que pode se manifestar clinicamente como marcha claudicante tipo Trendelenburg, além de aumentar teoricamente a força de reação articular necessária para estabilizar a pelve durante a marcha, o que pode contribuir para maior desgaste do polietileno e risco de instabilidade/luxação por menor tensionamento de partes moles.",
    "media")

add("Artroplastia total do quadril - técnica",
    "Um paciente com fratura do colo do fêmur deslocada (Garden III) e 78 anos, previamente independente e ativo, sem demência, é candidato à artroplastia. Qual opção de tratamento cirúrgico é geralmente preferida em detrimento da osteossíntese, considerando o alto risco de complicações da fixação nessa faixa etária/deslocamento?",
    ["Fixação com parafusos canulados isoladamente", "Artroplastia (total ou parcial, conforme demanda funcional e comorbidades) do quadril", "Tração cutânea prolongada sem cirurgia", "Osteotomia valgizante isolada"],
    1,
    "Em pacientes idosos com fratura do colo femoral deslocada (Garden III-IV), o risco de complicações da osteossíntese (não união, osteonecrose) é elevado, e a artroplastia (parcial/hemiartroplastia em pacientes menos ativos ou com comorbidades, ou total em pacientes mais ativos e independentes, especialmente se houver artrose prévia) é preferida por oferecer recuperação funcional mais previsível e menor taxa de reoperação em comparação à fixação interna nessa população.",
    "facil")

add("Artroplastia total do quadril - técnica",
    "Sobre a via de acesso lateral direta (transglútea, Hardinge), qual é uma desvantagem funcional potencial relacionada à técnica de desinserção parcial do glúteo médio?",
    ["Aumento do risco de luxação posterior por lesão da cápsula posterior", "Possível fraqueza abdutora residual e claudicação tipo Trendelenburg caso a reinserção do glúteo médio não seja adequada", "Lesão obrigatória do nervo isquiático em todos os casos", "Impossibilidade de uso de componentes não cimentados"],
    1,
    "A via lateral direta envolve desinserção parcial (anterior) das fibras do glúteo médio e mínimo da região do trocanter maior para acesso à articulação. Uma reinserção inadequada ou falha de cicatrização dessa musculatura pode resultar em fraqueza abdutora residual e claudicação tipo Trendelenburg no pós-operatório, sendo uma desvantagem relativa dessa via em comparação a abordagens que preservam a inserção abdutora, embora ofereça baixa taxa de luxação por preservar estruturas posteriores.",
    "media")

# ============================================================
# BLOCO 6 - COMPLICACOES DA ATQ (20 questoes)
# ============================================================

add("Complicações da ATQ - luxação",
    "Qual é o fator de risco mais associado à luxação posterior após ATQ por via posterolateral sem reparo capsular?",
    ["Flexão excessiva do quadril associada à adução e rotação interna", "Extensão do quadril associada à rotação externa", "Abdução isolada do quadril", "Flexão isolada de joelho sem movimento de quadril"],
    0,
    "A combinação de flexão excessiva do quadril, adução e rotação interna (posição classicamente evitada após via posterolateral, como ao calçar sapatos ou cruzar as pernas) tensiona e pode luxar posteriormente uma prótese de quadril operada por essa via, especialmente quando a cápsula posterior e os rotadores externos não foram reparados. Por isso, orientações pós-operatórias específicas restringem essa combinação de movimentos nas primeiras semanas.",
    "facil")

add("Complicações da ATQ - luxação",
    "Paciente com luxação posterior recorrente após ATQ, na investigação identifica-se componente acetabular excessivamente vertical (inclinação de 65°). Qual é a conduta cirúrgica mais apropriada para tratar essa causa específica de instabilidade?",
    ["Aumentar apenas o tamanho da cabeça femoral sem corrigir a posição acetabular", "Revisão do componente acetabular para reposicioná-lo dentro de parâmetros adequados de inclinação/anteversão", "Artrodese imediata do quadril", "Observação clínica sem intervenção, pois a posição do componente não influencia luxação"],
    1,
    "Quando a instabilidade recorrente decorre de mau posicionamento identificável do componente acetabular (como inclinação excessivamente vertical, fora da zona segura), a revisão cirúrgica com reposicionamento adequado do componente é a conduta definitiva mais eficaz, corrigindo a causa mecânica primária da luxação. Apenas trocar a cabeça femoral por uma maior, sem corrigir a posição do componente mal posicionado, tende a resultar em falha recorrente.",
    "media")

add("Complicações da ATQ - luxação",
    "Em relação ao uso de cabeças femorais de maior diâmetro na ATQ, qual é o principal benefício relacionado à estabilidade?",
    ["Redução do arco de movimento até o impacto (impingement) e da luxação, por aumentar a razão cabeça/pescoço e a distância de salto (jump distance)", "Redução do desgaste volumétrico do polietileno em todas as situações", "Eliminação completa do risco de luxação independentemente do posicionamento dos componentes", "Diminuição do custo do implante"],
    0,
    "Cabeças femorais de maior diâmetro aumentam a razão cabeça/colo e a distância necessária para que a cabeça salte para fora do acetábulo (jump distance), retardando o contato entre o colo protético e o rebordo acetabular (impingement) e, consequentemente, reduzindo o risco de luxação. Por outro lado, cabeças maiores podem aumentar o desgaste volumétrico absoluto do polietileno convencional, sendo essa relação mais favorável com polietilenos altamente reticulados.",
    "media")

add("Complicações da ATQ - luxação",
    "Qual é a definição de luxação recorrente da ATQ que geralmente justifica investigação sistemática das possíveis causas (posicionamento de componentes, tensão de partes moles, impacto, causas neurológicas)?",
    ["Um único episódio de luxação tratado com sucesso por redução fechada", "Dois ou mais episódios de luxação da mesma prótese", "Qualquer dor no quadril após ATQ sem evidência de instabilidade", "Apenas luxações que ocorrem no intraoperatório"],
    1,
    "A ocorrência de dois ou mais episódios de luxação da mesma artroplastia é geralmente considerada luxação recorrente/instabilidade recorrente, justificando investigação sistemática e minuciosa das possíveis causas — posicionamento inadequado de componentes, deficiência de partes moles (abdutores), impacto (impingement) por osteófitos ou desenho do implante, causas neurológicas/cognitivas do paciente, e infecção — para definir o tratamento mais apropriado, que pode variar de conservador a revisão cirúrgica.",
    "facil")

add("Complicações da ATQ - luxação",
    "Homem de 75 anos apresenta luxação anterior recorrente após ATQ por via anterior direta, relacionada a movimentos de extensão e rotação externa do quadril. Qual é uma causa mecânica comum de luxação anterior nesse contexto?",
    ["Anteversão excessiva do componente acetabular ou femoral", "Retroversão acentuada do componente acetabular", "Insuficiência isolada do músculo iliopsoas", "Excesso de comprimento do colo femoral sem relação com versão"],
    0,
    "A luxação anterior está classicamente associada ao excesso de anteversão do componente acetabular e/ou femoral (anteversão combinada excessiva), que favorece o deslocamento anterior da cabeça femoral especialmente durante extensão e rotação externa do quadril. Já a retroversão acetabular está mais associada à luxação posterior. A avaliação da anteversão combinada (femoral + acetabular) é fundamental na investigação desse tipo de instabilidade.",
    "media")

add("Complicações da ATQ - infecção periprotética",
    "Segundo os critérios atuais (ICM/MSIS) para diagnóstico de infecção articular periprotética, qual dos seguintes é considerado um critério maior (definitivo) isoladamente suficiente para o diagnóstico?",
    ["PCR sérica elevada isoladamente", "Presença de duas culturas positivas para o mesmo organismo obtidas de amostras periprotéticas ou presença de fístula comunicante com a articulação", "Contagem de leucócitos no líquido sinovial levemente elevada", "VHS elevada isoladamente"],
    1,
    "Os critérios maiores (definitivos) para infecção articular periprotética incluem a presença de fístula (trajeto sinusal) comunicando-se com a articulação protética ou o isolamento do mesmo microrganismo em duas ou mais culturas independentes de tecido/líquido periprotético. Qualquer um desses achados, isoladamente, já confirma o diagnóstico. Marcadores séricos como PCR e VHS elevados, ou alterações leves no líquido sinovial, são critérios menores que, isoladamente, não fecham o diagnóstico, mas compõem um escore combinado.",
    "media")

add("Complicações da ATQ - infecção periprotética",
    "Paciente com infecção periprotética aguda pós-operatória precoce (menos de 4 semanas da cirurgia índice), implante bem fixado, sem trajeto fistuloso crônico. Qual é a estratégia cirúrgica mais indicada?",
    ["Revisão em dois tempos com retirada de todos os componentes", "Desbridamento cirúrgico com retenção do implante (DAIR) associado à troca dos componentes modulares (cabeça e inserto) e antibioticoterapia prolongada", "Amputação do membro", "Apenas antibioticoterapia oral prolongada sem qualquer intervenção cirúrgica"],
    1,
    "Em infecções agudas (seja pós-operatória precoce, geralmente até 4-6 semanas, ou hematogênica aguda) com implante estável/bem fixado e curta duração de sintomas, o desbridamento cirúrgico com retenção do implante (DAIR - debridement, antibiotics, and implant retention), associado à troca dos componentes modulares (cabeça femoral e inserto de polietileno) para permitir acesso completo e remoção de biofilme, seguido de antibioticoterapia prolongada, é a estratégia recomendada, com bons resultados quando os critérios de elegibilidade são respeitados.",
    "media")

add("Complicações da ATQ - infecção periprotética",
    "Em relação à revisão em dois tempos para infecção periprotética crônica, qual é a principal função do espaçador de cimento com antibiótico colocado no primeiro tempo cirúrgico?",
    ["Substituir definitivamente o implante retirado sem necessidade de segundo tempo", "Fornecer liberação local de antibiótico de alta concentração, manter o espaço articular/comprimento do membro e permitir alguma função temporária enquanto se trata a infecção", "Promover osteointegração definitiva do novo implante", "Aumentar propositalmente o risco de nova infecção para estimular resposta imune"],
    1,
    "O espaçador de cimento impregnado com antibiótico(s) tem múltiplas funções no protocolo de revisão em dois tempos: fornece concentrações locais elevadas de antibiótico diretamente no foco infeccioso (com menor toxicidade sistêmica), mantém o espaço articular e o comprimento relativo do membro, evitando contratura de partes moles, e permite alguma mobilidade/função temporária ao paciente entre os dois tempos cirúrgicos, até que a infecção seja considerada controlada e se proceda à reimplantação definitiva.",
    "media")

add("Complicações da ATQ - infecção periprotética",
    "Qual microrganismo é o mais frequentemente implicado nas infecções periprotéticas de quadril, segundo a literatura?",
    ["Staphylococcus aureus e estafilococos coagulase-negativos (S. epidermidis)", "Mycobacterium tuberculosis", "Candida albicans", "Pseudomonas aeruginosa exclusivamente"],
    0,
    "Staphylococcus aureus e os estafilococos coagulase-negativos (principalmente S. epidermidis) são os microrganismos mais comumente isolados em infecções periprotéticas de quadril, frequentemente formando biofilme sobre a superfície do implante, o que dificulta a erradicação apenas com antibioticoterapia isolada e reforça a necessidade de abordagem cirúrgica associada na maioria dos casos. Micobactérias, fungos e Pseudomonas são causas menos frequentes, mas relevantes em populações específicas (imunossuprimidos, usuários de drogas intravenosas).",
    "facil")

add("Complicações da ATQ - infecção periprotética",
    "Sobre a antibioticoprofilaxia cirúrgica na artroplastia total do quadril primária, qual é a prática recomendada?",
    ["Administração de antibiótico endovenoso de amplo espectro iniciado até 60 minutos antes da incisão cirúrgica, com dose adicional conforme peso/duração da cirurgia", "Iniciar antibiótico apenas após o fechamento da ferida operatória", "Utilizar antibioticoterapia oral prolongada por 4 semanas no pré-operatório", "Não há necessidade de profilaxia antibiótica em cirurgias eletivas de ATQ"],
    0,
    "A antibioticoprofilaxia cirúrgica na ATQ deve ser administrada por via endovenosa dentro de uma janela de tempo (geralmente até 60 minutos, ou até 120 minutos para vancomicina) antes da incisão, com redosagem intraoperatória conforme a meia-vida do fármaco e a duração da cirurgia/perda sanguínea, sendo uma medida fundamental, porém não isolada, na prevenção de infecção periprotética, que também depende de técnica asséptica rigorosa, controle glicêmico e outros fatores.",
    "facil")

add("Complicações da ATQ - fratura periprotética",
    "Paciente sofre queda simples 3 anos após ATQ primária não cimentada, evoluindo com dor e incapacidade de deambular. Radiografia mostra fratura periprotética no nível da metáfise femoral, com componente femoral estável (bem fixado). Segundo a classificação de Vancouver, esse tipo de fratura corresponde a:",
    ["Tipo A", "Tipo B1", "Tipo B2", "Tipo C"],
    1,
    "A classificação de Vancouver considera a localização da fratura e a estabilidade do componente femoral. O tipo B1 corresponde a fraturas ao redor ou logo abaixo da haste femoral, com o componente ainda bem fixado (estável). O tipo A acomete a região trocantérica, o tipo B2 apresenta o mesmo nível de fratura, mas com haste solta (instável) e estoque ósseo preservado, o tipo B3 associa afrouxamento a perda óssea significativa, e o tipo C corresponde a fraturas distantes da ponta da haste, sem interferência na estabilidade do implante.",
    "media")

add("Complicações da ATQ - fratura periprotética",
    "Qual é o tratamento mais apropriado para uma fratura periprotética de fêmur Vancouver B2 (componente femoral solto, estoque ósseo adequado)?",
    ["Tratamento conservador com imobilização gessada", "Revisão do componente femoral para uma haste de fixação mais distal (diafisária), com ou sem osteossíntese complementar", "Apenas osteossíntese com placa, mantendo a haste original solta no lugar", "Amputação do membro"],
    1,
    "Nas fraturas Vancouver B2, o componente femoral está solto, exigindo revisão para uma haste que obtenha fixação distal à fratura (geralmente hastes não cimentadas de fixação diafisária/cônica), frequentemente associada a osteossíntese complementar (cerclagens, placas) para auxiliar a consolidação da fratura, já que a simples fixação da fratura sem tratar o afrouxamento do implante (mantendo a haste solta) tende a falhar. Tratamento conservador não é adequado nesse contexto de instabilidade do implante associada a fratura.",
    "dificil")

add("Complicações da ATQ - fratura periprotética",
    "Qual é a conduta habitual para uma fratura periprotética Vancouver tipo A (região trocantérica) minimamente deslocada, com componente femoral estável?",
    ["Revisão obrigatória de todo o componente femoral", "Tratamento conservador (proteção de carga, eventual órtese) ou, se sintomática/deslocada, fixação com cabos/cerclagens, sem necessidade de revisão do componente estável", "Amputação do membro", "Artrodese do quadril"],
    1,
    "Fraturas Vancouver tipo A, localizadas na região trocantérica (subdividida em AG para o grande trocanter e AL para o pequeno trocanter), geralmente ocorrem com componente femoral estável. Quando minimamente deslocadas e o paciente tem sintomas leves, o tratamento pode ser conservador (proteção de carga). Se houver deslocamento significativo ou comprometimento funcional (ex.: grande trocanter com inserção abdutora, gerando risco de claudicação), realiza-se fixação com cabos/cerclagens ou placas específicas, sem necessidade de revisão do componente femoral que permanece estável.",
    "media")

add("Complicações da ATQ - fratura periprotética",
    "Sobre fraturas periprotéticas acetabulares após ATQ, qual fator é mais relevante na decisão entre tratamento conservador e cirúrgico?",
    ["Cor da pele do paciente", "Estabilidade do componente acetabular e a integridade do estoque ósseo de suporte", "Tipo de anestesia utilizada na cirurgia índice", "Marca comercial do implante utilizado"],
    1,
    "Na avaliação de fraturas periprotéticas acetabulares, o principal determinante da conduta é a estabilidade do componente acetabular (fixo ou solto) e a qualidade/integridade do estoque ósseo de suporte, uma vez que fraturas com componente estável e boa qualidade óssea podem, em casos selecionados, ser tratadas conservadoramente com restrição de carga, enquanto componentes instáveis ou grandes defeitos ósseos geralmente exigem revisão cirúrgica com reconstrução óssea e/ou fixação da fratura.",
    "dificil")

add("Complicações da ATQ - soltura/osteólise",
    "Qual é o principal mecanismo biológico implicado na osteólise periprotética associada à soltura asséptica tardia da ATQ?",
    ["Reação de corpo estranho e resposta inflamatória macrofágica mediada por partículas de desgaste (especialmente do polietileno), levando à ativação de osteoclastos", "Infecção bacteriana de baixa virulência sempre presente", "Reação alérgica sistêmica ao metal em todos os pacientes", "Deficiência isolada de vitamina D"],
    0,
    "A osteólise periprotética resulta principalmente da resposta inflamatória crônica desencadeada por partículas de desgaste (do polietileno, metal ou cimento) fagocitadas por macrófagos, que liberam citocinas pró-inflamatórias (como TNF-alfa, IL-1, IL-6) e ativam a via RANK/RANKL, estimulando a diferenciação e atividade osteoclástica, resultando em reabsorção óssea periprotética progressiva e, eventualmente, soltura asséptica dos componentes.",
    "media")

add("Complicações da ATQ - soltura/osteólise",
    "Radiografia de controle de paciente assintomático 8 anos após ATQ mostra linha radiolucente progressiva ao redor do componente acetabular não cimentado, com áreas focais de rarefação óssea compatíveis com cistos, sem migração do componente. Qual é a interpretação mais provável?",
    ["Infecção periprotética aguda", "Osteólise periprotética por partículas de desgaste, possivelmente relacionada a soltura asséptica em evolução", "Fratura periprotética oculta", "Alteração normal esperada em qualquer prótese não cimentada"],
    1,
    "Linhas radiolucentes progressivas associadas a áreas focais de rarefação óssea (cistos) ao redor de componentes protéticos, especialmente sem sinais clínicos agudos de infecção, são compatíveis com osteólise por partículas de desgaste, um processo insidioso que pode evoluir para soltura asséptica dos componentes se não identificado e monitorado adequadamente, podendo exigir revisão cirúrgica antes que ocorra perda óssea maciça ou fratura periprotética associada à fragilização do osso.",
    "media")

add("Complicações da ATQ - discrepância de membros",
    "Paciente refere sensação de perna operada mais longa após ATQ, com discrepância mensurada de 1,5 cm. Qual é a conduta inicial mais apropriada nas primeiras semanas de pós-operatório, na ausência de sintomas neurológicos?",
    ["Revisão cirúrgica imediata do componente femoral", "Orientação, uso de compensação (palmilha) se sintomático, e reavaliação, já que discrepâncias leves frequentemente são bem toleradas e podem melhorar com adaptação/fisioterapia", "Amputação parcial do membro contralateral", "Osteotomia de encurtamento femoral imediata"],
    1,
    "Discrepâncias leves de comprimento de membro (geralmente até 1-2 cm) após ATQ são relativamente comuns e frequentemente bem toleradas, podendo ser manejadas inicialmente com orientação, fisioterapia para alongamento de partes moles contraturadas e, se necessário, compensação com palmilha no calçado. A revisão cirúrgica é reservada para discrepâncias maiores, sintomáticas e refratárias a medidas conservadoras, especialmente quando há associação com desconforto significativo ou alterações compensatórias posturais.",
    "facil")

add("Complicações da ATQ - discrepância de membros",
    "Qual é a principal causa cirúrgica evitável de alongamento excessivo do membro operado durante uma ATQ primária?",
    ["Uso de haste femoral muito curta", "Posicionamento inadequado do nível de corte do colo femoral e/ou escolha inadequada do comprimento do colo protético/offset durante o planejamento e execução cirúrgica", "Uso de cabeça femoral cerâmica em vez de metálica", "Via de acesso anterior direta exclusivamente"],
    1,
    "O comprimento final do membro operado depende diretamente do nível do corte do colo femoral nativo e da escolha do comprimento do colo protético (curto, padrão, longo) e do tamanho da cabeça femoral, sendo o planejamento pré-operatório cuidadoso (templating) e a técnica intraoperatória (uso de referências anatômicas e, quando disponível, navegação ou métodos de aferição intraoperatória) fundamentais para minimizar alongamentos ou encurtamentos indesejados do membro.",
    "media")

add("Complicações da ATQ - lesão nervosa",
    "Paciente evolui no pós-operatório de ATQ com pé caído (dificuldade de dorsiflexão) e alteração de sensibilidade no dorso do pé, mantendo flexão plantar preservada. Qual estrutura nervosa provavelmente foi acometida?",
    ["Nervo tibial (componente do isquiático)", "Componente fibular (peroneal) comum do nervo isquiático", "Nervo femoral", "Nervo obturador"],
    1,
    "O quadro de pé caído (dificuldade de dorsiflexão do tornozelo/pé) com alteração sensitiva no dorso do pé, mantendo a flexão plantar preservada, é característico de lesão do componente fibular (peroneal comum) do nervo isquiático, que é mais superficial, menos móvel e mais suscetível a tração/compressão do que o componente tibial durante manipulações cirúrgicas do quadril, sobretudo em alongamentos do membro ou vias posterolaterais.",
    "media")

add("Complicações da ATQ - lesão nervosa",
    "Qual é o principal fator de risco relacionado ao alongamento do membro operado para lesão do nervo isquiático durante ATQ?",
    ["Alongamento do membro superior a 4 cm (ou excesso de tração combinada a outros fatores de risco)", "Uso de componente acetabular cimentado", "Idade do paciente inferior a 40 anos", "Uso de cabeça femoral cerâmica"],
    0,
    "O alongamento excessivo do membro operado (classicamente descrito como acima de aproximadamente 4 cm, embora o risco seja multifatorial e dependa também de fatores anatômicos individuais) é um dos principais fatores associados à lesão do nervo isquiático por tração durante ATQ, especialmente em revisões complexas ou correções de grandes discrepâncias prévias (como em displasia grave), sendo importante o monitoramento neurofisiológico intraoperatório em casos de alto risco.",
    "media")

add("Complicações da ATQ - lesão nervosa",
    "Paciente apresenta, após ATQ por via anterior direta, dor em queimação e parestesia na face anterolateral da coxa, sem déficit motor. Qual é o diagnóstico mais provável e a conduta inicial?",
    ["Lesão do nervo isquiático; indicação de exploração cirúrgica imediata", "Neuropraxia do nervo cutâneo femoral lateral (meralgia parestésica); conduta geralmente expectante, pois tende a melhorar espontaneamente ao longo de meses", "Síndrome compartimental da coxa; fasciotomia de urgência", "Trombose venosa profunda; anticoagulação plena imediata"],
    1,
    "A queixa de dor em queimação e parestesia na face anterolateral da coxa, sem déficit motor, após via anterior direta, é altamente sugestiva de neuropraxia do nervo cutâneo femoral lateral (meralgia parestésica), uma complicação relativamente comum dessa via de acesso, devido à proximidade do nervo ao intervalo de dissecção. A conduta inicial é geralmente expectante, pois a maioria dos casos melhora espontaneamente em semanas a poucos meses, sem necessidade de exploração cirúrgica.",
    "media")

add("Complicações da ATQ",
    "Qual é a complicação tromboembólica mais temida após ATQ, exigindo profilaxia farmacológica e mecânica de rotina no perioperatório?",
    ["Embolia gordurosa isolada", "Trombose venosa profunda (TVP) e tromboembolismo pulmonar (TEP)", "Embolia aérea maciça", "Embolia séptica"],
    1,
    "A artroplastia total do quadril é um procedimento de alto risco para eventos tromboembólicos venosos (TVP e TEP), justificando o uso rotineiro de profilaxia farmacológica (anticoagulantes como heparina de baixo peso molecular, inibidores do fator Xa, aspirina em pacientes de baixo risco, entre outros, conforme protocolo institucional) associada a medidas mecânicas (compressão pneumática intermitente, meias elásticas) e mobilização precoce, reduzindo significativamente a morbimortalidade associada a essa complicação.",
    "facil")

add("Complicações da ATQ",
    "Sobre ossificação heterotópica após ATQ, qual fator de risco é classicamente reconhecido?",
    ["Sexo feminino isoladamente", "História prévia de ossificação heterotópica, espondilite anquilosante e hiperostose esquelética idiopática difusa (DISH)", "Uso de via de acesso anterior direta exclusivamente", "Idade inferior a 30 anos"],
    1,
    "Pacientes com história prévia de ossificação heterotópica (em cirurgia anterior), espondilite anquilosante, hiperostose esquelética idiopática difusa (DISH) e certas condições com tendência à formação óssea ectópica apresentam maior risco de desenvolver ossificação heterotópica após ATQ. Medidas profiláticas nesses pacientes de alto risco podem incluir uso criterioso de anti-inflamatórios não hormonais no pós-operatório ou, em casos selecionados, radioterapia de baixa dose perioperatória.",
    "dificil")

# ============================================================
# BLOCO 7 - REVISAO DE ATQ / PAPROSKY (8 questoes)
# ============================================================

add("Revisão de ATQ - defeitos ósseos",
    "Na classificação de Paprosky para defeitos ósseos acetabulares em revisão de ATQ, qual característica define um defeito tipo I?",
    ["Perda óssea segmentar extensa com descontinuidade pélvica", "Estoque ósseo periacetabular íntegro/mínima perda óssea, com anel acetabular estrutural preservado e teto intacto", "Migração superolateral maior que 3 cm com destruição do teto acetabular", "Perda óssea circunferencial associada a defeito da coluna posterior"],
    1,
    "O defeito tipo I de Paprosky caracteriza-se por mínima perda óssea, com as colunas anterior e posterior, o teto acetabular e as paredes medial/lateral estruturalmente íntegros, permitindo geralmente a utilização de um componente acetabular de revisão padrão hemisférico não cimentado com boa fixação primária, sem necessidade de enxerto ósseo estrutural extenso.",
    "media")

add("Revisão de ATQ - defeitos ósseos",
    "Um defeito acetabular Paprosky tipo IIIB é caracterizado por qual achado, com implicação direta na escolha do implante de revisão?",
    ["Perda óssea segmentar/cavitária extensa (>50%) com possível descontinuidade pélvica, exigindo frequentemente componentes de suporte estrutural (cup-cage, componentes triflange customizados) e enxerto ósseo maciço", "Perda óssea mínima tratável com componente hemisférico padrão", "Apenas defeito cavitário leve na parede medial", "Ausência completa de necessidade de enxerto ósseo"],
    0,
    "O defeito Paprosky tipo IIIB representa perda óssea extensa (envolvendo mais de 50% do acetábulo), com possível migração superomedial significativa da cabeça femoral e risco de descontinuidade pélvica associada, exigindo estratégias reconstrutivas mais complexas, como construtos cup-cage, componentes triflange customizados, anéis de suporte (ex.: anel de Burch-Schneider) associados a enxerto ósseo estrutural/impactado, dada a incapacidade de obter fixação estável apenas com componente hemisférico padrão.",
    "dificil")

add("Revisão de ATQ - defeitos ósseos",
    "Na classificação de Paprosky para defeitos ósseos femorais, qual característica principal diferencia o tipo IIIA do tipo IIIB?",
    ["O tipo IIIA não apresenta nenhuma perda óssea diafisária", "No tipo IIIA há istmo femoral intacto com pelo menos 4 cm de osso diafisário disponível para fixação distal, enquanto no tipo IIIB há menos de 4 cm de osso diafisário íntegro para fixação", "O tipo IIIB é sempre tratado apenas com haste cimentada padrão", "Não há diferença relevante entre os subtipos"],
    1,
    "Na classificação de Paprosky para defeitos femorais, os tipos III e IV representam graus crescentes de perda óssea metafisária e diafisária. A distinção entre IIIA e IIIB baseia-se na quantidade de osso diafisário isquêmico/íntegro disponível distalmente para obter fixação estável com uma haste de revisão: no IIIA, pelo menos 4 cm de istmo estão preservados, permitindo fixação distal com hastes cônicas modulares; no IIIB, menos de 4 cm estão disponíveis, tornando a fixação mais desafiadora e por vezes exigindo hastes ainda mais longas ou estratégias alternativas.",
    "dificil")

add("Revisão de ATQ - defeitos ósseos",
    "Qual é a principal estratégia de reconstrução para um defeito femoral Paprosky tipo IV (perda óssea diafisária extensa, canal em 'tubo de chaminé' sem istmo funcional)?",
    ["Haste padrão de fixação metafisária curta cimentada", "Haste de revisão modular longa com fixação distal além do defeito, aloenxerto estrutural (técnica de aloenxerto-prótese composta) ou, em casos extremos, megaprótese", "Componente acetabular hemisférico padrão isolado", "Nenhum tratamento cirúrgico é possível, sendo indicada apenas amputação"],
    1,
    "No defeito femoral tipo IV de Paprosky, a perda óssea é tão extensa que o canal medular perde a configuração de istmo funcional, comprometendo a fixação de hastes convencionais. Estratégias incluem hastes de revisão longas com fixação distal (além da área comprometida), reconstrução com aloenxerto estrutural associado a prótese (aloenxerto-prótese composta) para restaurar estoque ósseo, ou, em casos extremos de perda segmentar maciça, o uso de megapróteses (endopróteses tumorais modificadas).",
    "dificil")

add("Revisão de ATQ - defeitos ósseos",
    "Qual é a principal indicação para o uso de anéis de suporte acetabular (como o anel de Burch-Schneider) ou construtos cup-cage em cirurgia de revisão?",
    ["Defeitos ósseos acetabulares mínimos (Paprosky I)", "Defeitos ósseos acetabulares extensos com comprometimento estrutural das colunas, especialmente na presença de descontinuidade pélvica", "Substituição rotineira em todas as ATQ primárias", "Tratamento de infecção periprotética aguda sem perda óssea"],
    1,
    "Os anéis de suporte acetabular e construtos cup-cage são indicados em defeitos ósseos acetabulares extensos, com comprometimento estrutural significativo das colunas acetabulares e, particularmente, na presença de descontinuidade pélvica (perda de continuidade entre o ílio e o ísquio/púbis), situações em que um componente hemisférico convencional não consegue obter fixação estável isoladamente, sendo esses implantes projetados para transferir carga das áreas deficientes para o osso ilíaco remanescente.",
    "media")

add("Revisão de ATQ",
    "Antes de indicar uma revisão de ATQ por suspeita de soltura asséptica, qual é a etapa fundamental de investigação que deve sempre ser realizada para excluir uma causa alternativa importante?",
    ["Ressonância magnética de rotina, sem exceção", "Investigação para excluir infecção periprotética (marcadores inflamatórios séricos, análise do líquido sinovial, eventualmente biópsia/cultura intraoperatória)", "Eletroneuromiografia de rotina", "Ecocardiograma transesofágico"],
    1,
    "Antes de qualquer revisão de ATQ motivada por suspeita de soltura asséptica, é fundamental excluir infecção periprotética crônica de baixa virulência como causa subjacente, já que o tratamento cirúrgico e a estratégia de revisão diferem drasticamente entre soltura verdadeiramente asséptica (revisão em um tempo, sem necessidade obrigatória de troca de todos os componentes ou tratamento antibiótico prolongado) e soltura séptica (que exige protocolo específico de tratamento de infecção, como DAIR ou revisão em um/dois tempos). Isso inclui, no mínimo, marcadores séricos (PCR, VHS) e, na maioria dos casos, aspiração articular para análise do líquido sinovial.",
    "media")

add("Revisão de ATQ",
    "Homem de 60 anos com soltura asséptica do componente femoral 12 anos após ATQ primária cimentada, sem sinais de infecção, com boa qualidade óssea remanescente e defeito ósseo femoral Paprosky tipo II. Qual estratégia de revisão é geralmente adequada?",
    ["Componente femoral de revisão não cimentado com fixação metafisária/diafisária proximal, já que o defeito é limitado e o osso remanescente permite boa fixação", "Amputação transfemoral", "Artrodese definitiva do quadril", "Manutenção do componente solto sem qualquer intervenção"],
    0,
    "Em defeitos femorais Paprosky tipo II (perda óssea metafisária moderada, mas com istmo diafisário preservado), geralmente é possível obter boa fixação com um componente femoral de revisão não cimentado que aproveite o osso metafisário/diafisário remanescente, sem necessidade de reconstruções complexas como aloenxerto estrutural ou hastes megaprotéticas, reservadas a defeitos mais extensos (tipo III-IV).",
    "media")

add("Revisão de ATQ",
    "Qual é uma das principais vantagens de utilizar hastes femorais modulares cônicas de fixação diafisária (tipo cone) em revisões de ATQ com defeitos ósseos proximais importantes?",
    ["Elas dependem exclusivamente da fixação metafisária proximal, sendo inúteis em defeitos diafisários", "Permitem obter fixação estável distalmente ao defeito ósseo proximal (na região diafisária íntegra), além de possibilitar ajuste independente de comprimento, offset e versão graças à modularidade", "Não podem ser combinadas com nenhum tipo de enxerto ósseo", "São indicadas exclusivamente em ATQ primária, nunca em revisão"],
    1,
    "As hastes cônicas modulares de fixação diafisária foram desenvolvidas justamente para contornar defeitos ósseos proximais/metafisários extensos, obtendo estabilidade rotacional e axial na porção diafisária íntegra distal ao defeito. A modularidade (segmentos proximais e distais intercambiáveis) permite ajuste independente de comprimento do membro, offset e versão, otimizando a reconstrução biomecânica mesmo em cenários de perda óssea proximal significativa, podendo ainda ser associadas a enxerto ósseo impactado ou estrutural quando necessário.",
    "dificil")

# ============================================================
# BLOCO 8 - DOR TROCANTERICA / GLUTEO MEDIO (6 questoes)
# ============================================================

add("Dor trocantérica e lesões do glúteo médio",
    "Mulher de 55 anos com dor lateral crônica no quadril, pior ao deitar sobre o lado afetado e ao subir escadas, com dor à palpação direta sobre o trocanter maior. Qual é o diagnóstico mais provável?",
    ["Osteoartrose do quadril", "Síndrome da dor trocantérica maior (bursite trocantérica/tendinopatia glútea)", "Fratura de estresse do colo femoral", "Hérnia inguinal"],
    1,
    "A síndrome da dor trocantérica maior, que engloba a bursite trocantérica e a tendinopatia/lesão dos tendões glúteo médio e mínimo em sua inserção no trocanter maior, é a causa mais comum de dor lateral crônica do quadril em mulheres de meia-idade, caracterizada por dor localizada lateralmente, piora ao deitar sobre o lado afetado, ao subir escadas e à palpação direta da região trocantérica, diferentemente da dor inguinal profunda típica de artrose intra-articular.",
    "facil")

add("Dor trocantérica e lesões do glúteo médio",
    "Qual exame de imagem é mais indicado para confirmar lesão/ruptura do tendão do glúteo médio em paciente com dor trocantérica refratária ao tratamento conservador?",
    ["Radiografia simples de bacia isoladamente", "Ressonância magnética do quadril", "Cintilografia óssea trifásica", "Radiografia com incidência em falso perfil de Lequesne"],
    1,
    "A ressonância magnética é o exame de escolha para avaliar lesões tendíneas do glúteo médio/mínimo (o chamado "manguito rotador do quadril"), permitindo identificar tendinopatia, rupturas parciais ou completas, além de avaliar a bursa trocantérica e excluir outras causas de dor lateral do quadril. A radiografia simples é útil para avaliar calcificações tendíneas e descartar patologia óssea associada, mas não avalia diretamente a integridade tendínea.",
    "media")

add("Dor trocantérica e lesões do glúteo médio",
    "Qual é o tratamento inicial recomendado para a síndrome da dor trocantérica maior sem ruptura tendínea completa?",
    ["Cirurgia de reparo tendíneo imediata em todos os casos", "Tratamento conservador: fisioterapia, modificação de atividades, anti-inflamatórios e, se necessário, infiltração local de corticoide guiada", "Artroplastia total do quadril", "Osteotomia do trocanter maior"],
    1,
    "O tratamento inicial da síndrome da dor trocantérica maior é conservador, incluindo fisioterapia (alongamento do trato iliotibial, fortalecimento dos abdutores), modificação de atividades desencadeantes, uso criterioso de anti-inflamatórios e, em casos refratários, infiltração local guiada de corticoide na bursa trocantérica, com boa resposta na maioria dos pacientes. Tratamento cirúrgico é reservado a casos refratários ao tratamento conservador prolongado ou rupturas tendíneas completas e sintomáticas.",
    "facil")

add("Dor trocantérica e lesões do glúteo médio",
    "Paciente com ruptura completa e retraída do tendão do glúteo médio, confirmada por RM, refratária a tratamento conservador por mais de 6 meses, com claudicação importante tipo Trendelenburg. Qual é a conduta cirúrgica mais apropriada?",
    ["Bursectomia isolada sem reparo tendíneo", "Reparo cirúrgico do tendão glúteo médio (aberto ou endoscópico), com reinserção transóssea", "Artrodese do quadril", "Infiltração seriada de corticoide como tratamento definitivo"],
    1,
    "Em casos de ruptura completa e sintomática do tendão do glúteo médio, refratária ao tratamento conservador prolongado, com repercussão funcional significativa (claudicação tipo Trendelenburg), o reparo cirúrgico do tendão (por técnica aberta ou endoscópica), geralmente com reinserção transóssea na região do trocanter maior, é indicado para restaurar a função abdutora e melhorar a marcha, sendo considerada a lesão análoga, no quadril, à ruptura do manguito rotador no ombro.",
    "media")

add("Dor trocantérica e lesões do glúteo médio",
    "Qual é um importante diagnóstico diferencial de dor trocantérica lateral crônica que deve ser sempre considerado antes de atribuir os sintomas apenas à bursite trocantérica?",
    ["Osteoartrose do joelho contralateral isoladamente", "Dor referida de origem lombar (radiculopatia L4-L5) ou patologia intra-articular do quadril concomitante", "Hérnia umbilical", "Tendinite do calcâneo"],
    1,
    "A dor trocantérica lateral pode ser mimetizada ou coexistir com dor referida de origem lombar (radiculopatia, especialmente L4-L5/L5-S1) e com patologia intra-articular do quadril (como osteoartrose ou impacto femoroacetabular), sendo fundamental uma avaliação clínica abrangente da coluna lombar e da articulação coxofemoral antes de atribuir isoladamente os sintomas à síndrome da dor trocantérica maior, para não postergar o diagnóstico e tratamento corretos.",
    "media")

add("Dor trocantérica e lesões do glúteo médio",
    "Qual é o mecanismo fisiopatológico proposto para a associação entre dor trocantérica lateral crônica e o trato iliotibial?",
    ["O trato iliotibial não possui qualquer relação anatômica com o trocanter maior", "O atrito repetitivo do trato iliotibial sobre o trocanter maior, associado a fatores biomecânicos (como fraqueza abdutora), contribui para irritação da bursa e sobrecarga da inserção do glúteo médio/mínimo", "O trato iliotibial causa exclusivamente dor no joelho, nunca no quadril", "A tensão do trato iliotibial reduz a pressão sobre a bursa trocantérica"],
    1,
    "O trato iliotibial cruza superficialmente a região do trocanter maior, e seu atrito repetitivo sobre essa proeminência óssea, especialmente na presença de fatores biomecânicos predisponentes como fraqueza da musculatura abdutora (glúteo médio) e alterações de marcha, contribui para irritação da bursa trocantérica subjacente e sobrecarga mecânica da inserção tendínea do glúteo médio/mínimo, compondo o espectro da síndrome da dor trocantérica maior.",
    "dificil")

# ============================================================
# BLOCO 9 - QUADRIL EM RESSALTO (3 questoes)
# ============================================================

add("Quadril em ressalto",
    "Mulher de 22 anos, bailarina, relata sensação de estalido audível e palpável na região lateral do quadril durante a marcha e ao levantar da cadeira, sem dor significativa. O exame reproduz o estalido com a flexão e extensão do quadril em posição neutra/adução. Qual é o diagnóstico mais provável?",
    ["Quadril em ressalto externo (trato iliotibial/tensor da fáscia lata sobre o trocanter maior)", "Quadril em ressalto interno (tendão iliopsoas sobre a eminência iliopectínea/cabeça femoral)", "Luxação recidivante do quadril", "Fratura de estresse do colo femoral"],
    0,
    "O quadril em ressalto externo, mais comum, ocorre pelo deslizamento da porção posterior do trato iliotibial ou do tensor da fáscia lata sobre a proeminência do trocanter maior durante a flexo-extensão do quadril, sendo tipicamente palpável e visível lateralmente, comum em atletas e bailarinos. O ressalto interno, por outro lado, relaciona-se ao tendão do iliopsoas deslizando sobre a eminência iliopectínea ou a cabeça femoral, geralmente percebido na região inguinal/anterior.",
    "facil")

add("Quadril em ressalto",
    "Sobre o quadril em ressalto interno (tendão do iliopsoas), qual manobra clínica classicamente reproduz o estalido?",
    ["Extensão isolada do joelho em decúbito dorsal", "Movimento do quadril da posição de flexão, abdução e rotação externa para extensão, adução e rotação interna", "Rotação externa isolada do ombro contralateral", "Dorsiflexão do tornozelo ipsilateral"],
    1,
    "O ressalto interno do iliopsoas é classicamente reproduzido ao mover o quadril da posição de flexão, abdução e rotação externa para extensão, adução e rotação interna, momento em que o tendão do iliopsoas desliza sobre a eminência iliopectínea (ou a cabeça femoral/cápsula anterior), gerando o estalido característico, frequentemente palpável na região inguinal.",
    "media")

add("Quadril em ressalto",
    "Paciente com quadril em ressalto externo sintomático (dor associada ao estalido, limitando atividades esportivas), refratário a tratamento conservador prolongado (fisioterapia com alongamento do trato iliotibial, fortalecimento e modificação de atividades). Qual é uma opção de tratamento cirúrgico descrita para casos refratários?",
    ["Artroplastia total do quadril", "Alongamento em Z (Z-plastia) ou liberação parcial do trato iliotibial/tensor da fáscia lata na região do trocanter maior", "Artrodese do quadril", "Osteotomia periacetabular"],
    1,
    "Nos raros casos de quadril em ressalto externo refratário ao tratamento conservador adequado e prolongado, técnicas cirúrgicas descritas incluem o alongamento em Z (Z-plastia) do trato iliotibial ou a liberação parcial das fibras posteriores tensas sobre o trocanter maior, visando reduzir o atrito mecânico responsável pelo estalido e pela dor associada, preservando a função abdutora global do membro.",
    "media")

# ============================================================
# BLOCO 10 - PIRIFORME / DOR GLUTEA PROFUNDA (3 questoes)
# ============================================================

add("Síndrome do piriforme e dor glútea profunda",
    "Mulher de 45 anos com dor glútea profunda irradiada para a face posterior da coxa, piora ao sentar prolongadamente, sem sinais de radiculopatia lombar ao exame e com RM de coluna lombar normal. Qual condição deve ser considerada no diagnóstico diferencial, relacionada ao aprisionamento do nervo isquiático na região glútea profunda?",
    ["Síndrome do piriforme (parte da síndrome da dor glútea profunda)", "Hérnia discal L4-L5 confirmada por RM", "Fratura de estresse do sacro isoladamente sem relação nervosa", "Estenose do canal medular lombar"],
    0,
    "A síndrome do piriforme, incluída no espectro mais amplo da síndrome da dor glútea profunda (deep gluteal syndrome), decorre do aprisionamento/irritação do nervo isquiático por estruturas na região glútea profunda, mais classicamente o músculo piriforme, mas também outras causas como bandas fibrosas, variações anatômicas do trajeto do nervo em relação ao piriforme, ou outras estruturas musculares adjacentes. Deve ser considerada quando há dor glútea profunda com irradiação ciática na ausência de compressão radicular lombar identificável na RM de coluna.",
    "facil")

add("Síndrome do piriforme e dor glútea profunda",
    "Qual manobra de exame físico é classicamente utilizada para sugerir síndrome do piriforme, ao reproduzir a dor glútea/ciática por tensionamento do músculo?",
    ["Teste de Lasègue exclusivamente", "Teste de FAIR (flexão, adução e rotação interna do quadril) ou teste de resistência à rotação externa/abdução ativa do quadril", "Teste de Phalen", "Teste de Finkelstein"],
    1,
    "O teste de FAIR (flexão, adução e rotação interna passiva do quadril) tensiona o músculo piriforme e pode comprimir o nervo isquiático subjacente, reproduzindo a dor glútea/ciática em pacientes com síndrome do piriforme; da mesma forma, testes de resistência ativa à rotação externa e abdução do quadril contra resistência também podem reproduzir os sintomas por contração do músculo. O teste de Lasègue é mais associado à radiculopatia lombar por hérnia discal, Phalen ao túnel do carpo, e Finkelstein à tenossinovite de De Quervain.",
    "media")

add("Síndrome do piriforme e dor glútea profunda",
    "Qual é a abordagem terapêutica inicial recomendada para a síndrome do piriforme antes de considerar tratamento cirúrgico (liberação/neurólise)?",
    ["Cirurgia de liberação do piriforme como primeira linha em todos os pacientes", "Tratamento conservador: fisioterapia com alongamento do piriforme e da musculatura rotadora, modificação de atividades, anti-inflamatórios e, em casos refratários, infiltração guiada (corticoide/toxina botulínica) no músculo piriforme", "Artroplastia total do quadril profilática", "Amputação do membro inferior"],
    1,
    "O tratamento inicial da síndrome do piriforme é conservador, incluindo fisioterapia direcionada ao alongamento do músculo piriforme e da musculatura rotadora do quadril, modificação de atividades desencadeantes (evitar posições prolongadas de sedestação, por exemplo), uso criterioso de anti-inflamatórios e, em casos refratários, infiltração guiada por imagem (ultrassom ou tomografia) com corticoide ou toxina botulínica no músculo piriforme. A liberação cirúrgica (endoscópica ou aberta) é reservada para casos refratários a tratamento conservador adequado e prolongado.",
    "media")

# ============================================================

print(f"Total de questoes geradas: {len(questoes)}")

data = {
    "area": "Quadril do Adulto",
    "slug": "quadril",
    "questoes": questoes,
}

with open("/home/dev/work/vamos-criar-um-programa-de-estudos-personalizado/teot-app/data/quadril.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Arquivo salvo.")
