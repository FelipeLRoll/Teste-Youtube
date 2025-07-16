[![author](https://img.shields.io/badge/author-feliperoll-purple.svg)](https://www.linkedin.com/in/felipe-roll/)

### :us: [English Version](https://github.com/FelipeLRoll/Teste-Youtube/blob/main/README.md)

# Projeto de Análise de Performance no YouTube

## Motivação

Entender o que faz um vídeo performar bem no YouTube é essencial para criadores de conteúdo que desejam crescer suas audiências, melhorar engajamento e monetização. Ao analisar dados históricos dos vídeos, é possível identificar padrões e fatores que influenciam visualizações, duração média de exibição e taxa de cliques.

## Objetivos

Este projeto tem como principal objetivo realizar uma análise de dados sobre a performance de vídeos em um canal do YouTube, utilizando técnicas de análise exploratória e visualização de dados para gerar insights que orientem decisões estratégicas.

- Investigar os fatores que influenciam o desempenho dos vídeos

- Identificar padrões

- Descobrir quais temas geram maior engajamento

## Etapas do Projeto

- Carregamento e análise inicial dos dados: Inspeção do dataset exportado do YouTube Studio

- Limpeza e tratamento dos dados: Conversão de colunas, tratamento de valores nulos, padronizações

- Engenharia de atributos: Criação de novas variáveis

- Análise exploratória (EDA): Avaliação estatística e identificação de tendências e outliers

- Visualização com gráficos: Criação de barplots, scatterplots e wordclouds para facilitar a interpretação dos dados

- Geração de insights: Com base nas análises, identificar ações que possam melhorar a performance do canal

# Dicionário de Dados - YouTube Analytics

## Descrição Geral

Este dataset contém dados de análise de performance de vídeos de um canal do YouTube, focado em conteúdo de Counter-Strike 2 (CS2), incluindo tutoriais de granadas e smokes para diferentes mapas.

## Estrutura dos Dados

### Informações Gerais

- **Fonte**: YouTube Analytics
- **Período**: 2013-2025
- **Número de registros**: 11 vídeos
- **Formato**: CSV

---

## Variáveis

| Variável | Tipo | Descrição | Exemplo | Observações |
|----------|------|-----------|---------|-------------|
| **Content** | String | ID único do vídeo no YouTube | `PU50erzKEjk` | Identificador único gerado pelo YouTube |
| **Video title** | String | Título do vídeo | `CS2 - Smokes Anubis` | Título público do vídeo |
| **Video publish time** | String | Data de publicação | `Feb 25, 2025` | Formato: MMM DD, YYYY |
| **Duration** | Integer | Duração do vídeo em segundos | `257` | Duração total do vídeo |
| **Average view duration** | String | Tempo médio de visualização | `0:00:42` | Formato: H:MM:SS |
| **Unique viewers** | Integer | Número de visualizadores únicos | - | Dados não disponíveis no dataset |
| **Stayed to watch (%)** | Float | Percentual de retenção | - | Dados não disponíveis no dataset |
| **Average views per viewer** | Float | Média de visualizações por pessoa | - | Dados não disponíveis no dataset |
| **New viewers** | Integer | Novos visualizadores | - | Dados não disponíveis no dataset |
| **Returning viewers** | Integer | Visualizadores recorrentes | - | Dados não disponíveis no dataset |
| **Views** | Integer | Total de visualizações | `52` | Número total de views |
| **Watch time (hours)** | Float | Tempo total assistido | `0.6107` | Soma de todo tempo assistido |
| **Subscribers** | Integer | Inscritos ganhos | `2` | Novos inscritos através do vídeo |
| **Impressions** | Integer | Impressões do vídeo | `1572` | Quantas vezes o vídeo foi mostrado |
| **Impressions click-through rate (%)** | Float | Taxa de cliques nas impressões | `1.15` | Percentual de cliques sobre impressões |

---

# Resultados

### **Análise Descritiva**

O que aconteceu?

- Foram analisados vídeos do meu canal do Youtube entre as datas 16/10/2013 até 21/03/2025
- Os vídeos tiveram uma mediana de 3 visualizações
- A mediana do tempo de duração dos vídeos é de 3 minutos e 55 segundos
- Vídeos com palavras como "CS2" e "Smokes" se saíram melhor na maioria das métricas
- Vídeos mais longos tendem a ter uma média maior de tempo de visualização
- Quanto mais pessoas assistem um vídeo, menor o tempo médio de visualização
- Vídeos com mais visualizações, tendem a ter mais impressões
- O número de visualizações e o número de inscritos ganhos ao longo do tempo seguem a mesma tendência
- Vídeos tiveram mais sucesso após o ano de 2023 
- Títulos com "Granadas" ao invés de "Smokes" geram menos visualizações
- Os dois vídeos do Mapa "Anubis" teve o maior número de visualizações no CS2 comparado ao vídeo do CS:GO ("Smokes Anubis")

---

### **Análise Diagnóstica**

Por que aconteceu?

- Vídeos com palavras-chave como "CS2" e "Smokes" obtiveram mais visualizações, provavelmente porque o jogo "CS2" lançou recentemente e muitos jogadores procuram vídeos de como fazer "Smokes" no jogo
- Mesmo motivo fez que os vídeos lançados após 2023 tiveram engajamento maior
- Vídeos com mais visualizações tendem a ter um CTR mais real, pois aparecem para um numero maior de pessoas e portanto, têm mais chances de serem clicados
- Quanto mais pessoas assistem um vídeo, menor o tempo médio de visualização, isso se dá devido ao fato que principalmente neste tipo de video, os usuários tendem a apenas assistir uma parte específica do video (uma "Smoke" específica), e não a todo o conteúdo
- A curva do número de visualizações e do número de inscritos ganhos ao longo do tempo seguem uma curva muito parecida pois quanto mais pessoas assistem um vídeo, maior a chance de ganhar inscritos 
- Mapa "Anubis" teve o maior número de visualizações pelo fato de ser um mapa relativamente novo, gerando um interesse maior. Principalmente os vídeos do CS2, que obtiveram um número de visualizações muito maior que a versão do CS:GO

---

### **Análise Preditiva**

O que vai acontecer?

- Provavelmente, se continuar postando vídeos com as palavras "CS2" e "Smokes", o canal continuará a crescer
- Mesma coisa para vídeos feitos entre 2023-2025, pois o jogo ainda é relevante e muitas pessoas procuram por este tipo de vídeo, porém, chegará um ponto onde isso não será mais tão relevante porque as pessoas assistiram este tipo de vídeo e já aprenderam o que precisam
- Continuar fazendo vídeos de mapas novos e relevantes poderá gerar um interesse maior nos vídeos

---

### **Análise Prescritiva**

O que devemos fazer?

- Postar vídeos com as palavras-chave que dão maior número de visualizações
- Postar vídeos com mapas novos lançados a fim de gerar interesse maior no vídeo pelo fato de muitos jogadores quererem aprender sobre o mapa o mais rápido possível
- Postar enquanto o CS2 estiver relevante

# Developed by: 

  * [Felipe Roll - Linkedin](https://www.linkedin.com/in/felipe-roll)
  * [Felipe Roll - Github](https://github.com/FelipeLRoll)
  * [Felipe Roll - Gmail](felipelroll@gmail.com)
  
