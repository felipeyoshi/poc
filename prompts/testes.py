PROMPT_TESTE_MAPA = """
Contexto: Esse é um teste de cognição social baseado na imagem do mapa brasileiro onde imagens de elementos típicos de cada estado da federação estão posicionados na localização do referente estado.

Sua tarefa é avaliar a transcrição abaixo, que é a resposta de um paciente que foi submetido a esse teste. Sua avaliação deverá levar em consideração os seguintes pontos:

- Reconhecer o mapa do Brasil.
- Fazer conexão dos elementos com a localização deles no mapa.
- Capacidade de entender o padrão existente entre os elementos na imagem, inclusive inferindo, assim, a que se referem algumas imagens dúbias, que poderiam ser nomeadas diferentemente se não fosse o contexto.

Transcrição: {}

Saída da resposta: Arquivo HTML com fonte Arial.

Formato: Deve seguir a estrutura abaixo.

<h1>Resultado do Teste de Cognição Social</h1>

<h3>Nome:</h3> 'Nome do Paciente'

<h3>Reconhecimento do mapa do Brasil:</h3> 'resposta'

<h3>Compreensão do padrão e inferência sobre elementos dúbios:</h3> 'resposta'
"""