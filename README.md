## AFRODITE - Aprendizado Federado com Redução Ótima de Dados e Inclusão de Técnicas Eficientes


<div align="center">
     <a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"  height="40" width="45"/>
     <a href="https://www.tensorflow.org/?hl=pt-br" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg" alt="tensorflow"  height="40" width="40"/>
     <a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg" alt="numpy"  height="40" width="40"/>
     <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="pandas"  height="40" width="40"/>
       

<br>
<br>
</div>
Este repositório contém os arquivos necessários para a simulação de um aprendizado federado com agrupamento de clientes utilizando amostragem aleatoria dos dados no treinamento. As bibliotecas utilizadas nesse trabalho são: 

<br>
<br>

-  <i> numpy </i> : Utilizada para operações numéricas eficientes.
-  <i> pandas</i> : Utilizada para manipulação e análise de dados.
-  <i> scikit-learn</i>: Empregada pa técnicas tradicionais de aprendizado de máquina.ra
-  <i> tensorflow</i> e <i> keras</i>: Definição e treinamento o modelo no cliente.
-  <i> flower</i>: Configuração do ambiente de Aprendizado Federado.


### Instalação das dependências
``` 
python -m pip install --upgrade pip
pip3 install virtualenv
python -m venv venv
.\venv\Scripts\activate.bat
.\venv\Scripts\python -m pip install --upgrade pip
pip3 install -r requirements.txt
```
### Ativar máquina virtual
```
.\venv\Scripts\activate.bat
```
### Criar dataset com separação por classe

Criar os seguintes diretórios na raiz do projeto: 
``datasets\CIFAR-10\Non-IID-distribution``


Depois de criadas as pastas, rodar o seguinte código para criar arquivos class-index-test/train:
```
python src\dataset-process\generate_non_iid_shuffle.py
```
### Iniciar o treinamento original com o primeiro grupo de clientes (1 e 2)
```
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\server_update.py
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\client-1.py
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\client-2.py
```

### Iniciar o treinamento com amostragem de 325 dados no primeiro grupo de clientes (1 e 2)
```
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand325\server_update_reduced.py (subir o servidor)
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand325\client-1_rand.py
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand325\client-2_rand.py
```

### Iniciar o treinamento com amostragem de 1121 dados no primeiro grupo de clientes (1 e 2)
```
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand1121\server_update_reduced.py (subir o servidor)
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand1121\client-1_rand.py
python src\federated-learning-env\Non-IID-clients\Only-2-Classes\Reduced\Rand1121\client-2_rand.py
```

### Realizar o treinamento com demais grupos
Para realizar o treinamento com demais grupos, utilizar os arquivos nomeados com os clientes do respectivo grupo. Utilizar o mesmo servidor do primeiro grupo. Para utilizar amostragem aleatoria, rodar o experimento no diretorio correspondente da amostragem.


<i>Segundo Grupo</i>: client-3_rand.py / client-4_rand.py<br>
<i>Terceiro Grupo</i>: client-5_rand.py / client-6_rand.py<br>
<i>Quarto Grupo</i>: client-7_rand.py / client-8_rand.py<br>
<i>Quinto Grupo</i>: client-9_rand.py / client-10_rand.py<br>
