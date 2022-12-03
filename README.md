## SEL0337 - APLICAÇÕES DE MICROPROCESSADORES II

### Prática 6 - Introdução a interfaces de visão computacional, sistemas de versionamento de arquivos, e APIs públicas

O objetivo principal dessa prática é o desenvolvimento de uma aplicação em Python que acesse a API climática da *Oracle* e imprima as informações de tempo retornadas da requisição em uma imagem capturada pela câmera conectada à RaspberryPi.

Para isso, primeiramente, testes com o periférico foram efetuados a fim de garantir a familiarização com as operações da câmera. Todas as funções aplicadas a esse módulo foram administradas por meio da biblioteca `picamera`, importada para o *script* a partir da linha a seguir:

```python
from picamera import PiCamera
```

Então, o objeto da câmera foi instanciado e sua resolução foi estabelecida conforme o trecho a seguir:

```python
camera = PiCamera()
camera.resolution = (1024,768)
```

Depois, utilizou-se a função `camera.start_preview()` para habilitar a visualização prévia da imagem da câmera, mantida por dois segundos, por meio da função `time.sleep()` importada da biblioteca `time`.

Antes de capturar a imagem (nomeada "weatherpic.jpg") da câmera com a função `camera.capture()`, imprimem-se as informações desejadas por meio da função `camera.annotate_text = camText`.

Além disso, um vídeo de cinco segundos foi gravado por meio do trecho de código a seguir:

```python
camera.start_recording('rec.h264')
camera.wait_recording(5)
camera.stop_recording()
camera.stop_preview()
```

Esse trecho foi mantido comentado no código final a fim de que não fosse gravado um vídeo a cada rodada de teste do *script*, tendo em vista poupar a memória do computador e diminur o tempo de processamento.

Então, deu-se prosseguimento a etapa de requisição em API, definindo-se, para tal, uma string (`oracleURL`) com o endereço *http* com o ID 966583 fornecido pelo professor:

```python
oracleURL = "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583"
```

Por meio disso, foi feita a requisição do tipo `get` pelos itens do objeto `json` com as informações climáticas do endereço da API, impressas no terminal por meio do comando `pprint()`:

```python
weather = get(oracleURL).json()['items'][0]
pprint(weather)
```

Para isso foram utilizadas funções definidas nas bibliotecas `json`, `requests` e `pprint`, importadas para o código principal.

Dado que todas as informações retornadas da requisição são contidas no mesmo elemento da *array*, fez-se a requisição deste apenas, a fim de que as chaves do objeto pudessem ser acessadas. Isso tendo em vista que, na imagem capturada pela câmera, quer-se apenas que seja impressa a informação de temperatura correspondente à *key* `"ambient_temp"`. Assim, a *string* a ser impressa foi definida como:

```python
camText = f"NUSP: 11372782 \nTemperatura: {weather['ambient_temp']}\n"
```
