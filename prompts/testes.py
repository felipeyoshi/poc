PROMPT_TESTE_MAPA = """
Contexto: Esse é um teste de cognição social baseado na imagem do mapa brasileiro onde imagens que possuem como característica em comum serem elementos típicos de cada região, como pontos turísticos, frutas típicas e elementos culturais, estando cada imagem posicionada na localização da sua referente região.

Sua tarefa é avaliar a transcrição abaixo, que é a resposta de um paciente que foi submetido a esse teste. Sua avaliação deverá levar em consideração os seguintes pontos:

- O objetivo é que o paciente seja capaz de conectar os elementos vistos, inferindo o padrão existente, a característica em comum entre as imagens, qual o link entre elas.
- Se o paciente conseguir reconhecer o Brasil, isso mostra algum conhecimento geral.

Transcrição: tem uva, índio, um casal dançando... vários desenhos no Brasil.

Saída da resposta: Arquivo HTML com fonte Arial.

Formato: Deve seguir a estrutura abaixo.

<h1>Resultado do Teste de Cognição Social</h1>

<h3>Nome:</h3> 'Nome do Paciente'

<h3>Reconhecimento do mapa do Brasil:</h3> 'resposta'

<h3>Inferência sobre qual a característica em comum entre os elementos da imagem:</h3> 'resposta'

<h3>Conclusão Final:</h3> 'resposta'
"""