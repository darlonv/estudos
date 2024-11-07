# Watchtower

O [**Watchtower**](https://github.com/containrrr/watchtower) é um sistema utilizado para verificar se um *container* em execução teve sua imagem atualizada. Caso a imagem no dockerhub seja atualizada, para o *container*, e cria um novo a partir da imagem atualizada.

Executa dentro de um *container*, e pode ser incluído no `compose.yaml`. 


Parâmetros:
- `--interval 30` : Tempo de intervalo. *Default*: 24 horas. 
- `--cleanup` : remove a imagem anterior
- `<id>` nome do *container* observado.


## Exemplo

1. Crie/atualize a imagem e suba no docker hub  
`make build`  
ou  
`docker build --push -t darlon/teste .`

2. execute um *container* a partir da imagem, junto com o watchtower  
`docker compose up`  
deixe este terminal executando o *container*.

3. atualize o arquivo `script.sh`, modificando a mensagem mostrada

4. em outro terminal, atualize a imagem.  
`make build`


## Referências
- [DigitalOcean. How to Automatically Update Docker Container Images with Watchtower on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-automatically-update-docker-container-images-with-watchtower-on-ubuntu-22-04?utm_source=pocket_shared)  

