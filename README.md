# **DebConfWeightScheduling** 

**Conteúdo da Disciplina**: Weight Interval Scheduling <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0078224  |  Thaís Rebouças de Araujo |


## Sobre 

Esse trabalho é uma evolução do ()

Todo ano em algum lugar do mundo acontece a DebConf, com vários dias de atividades e palestras.
Esse ano o evento aconteceu na Índia, e para facilitar a escolha de quais atividades participar, esse projeto irá ajudar a montar um cronograma de atividades de acordo com o dia que você gostaria de participar.
Diferente do trabalho anterior, esse leva em consideração não apenas o menor tempo de ócio entre as atividades do cronograma, mas especialmente o tipo de atividade que o usuário tem preferência. Elas podem ser de 5 tipos:

- **Long talk (45 minutes)**: São as palestras mais longas do evento.
- **Short talk (20 minutes)**: Palestras mais curtas.
- **BoF (45 minutes)**: Roda de conversa.
- **Workshop (2h)**: Atividades "mão na massa" guiadas por um ou mais mentores.
- **Other**: Outros

Os dados da agenda do evento foram retirados do [site oficial](https://debconf23.debconf.org) através de raspagem dos dados, com o objetivo de ter os dados atualizados sempre que for utilizado.

## Screenshots

Inicialmente o programa pede ao usuário selecionar suas atividades preferidas:
![image](https://github.com/Thais-ra/thais-ra/assets/35047444/78c4674a-1cdb-4073-8d2e-c366bb43fd6f)


Depois o dia:
![image](https://github.com/Thais-ra/thais-ra/assets/35047444/d91fc9d8-c56b-4b7c-959f-1a8c7caba632)

## Instalação 
**Linguagem**: python<br>

## Uso

Para instalar as dependências é recomendado utilizar uma venv.
Na pasta raiz instale as dependências utilizando o comando:

``` pip3 install -r requirements.txt```

Execute o shell script que fará a raspagem de dados:

```./script.sh```

Se tiver problema para executar, adicione a permissão de execução ao script:

```chmod +x script.sh```

Ao rodar o script, o programa fará a raspagem de dados para atualizar o arquivo "schedule.json".
Não é necessário rodá-lo sempre que for usar, só na primeira vez ou quando quiser atualizar a agenda.

Para executar o programa, basta executar o arquivo **main.py** na raíz:

```python3 main.py```
