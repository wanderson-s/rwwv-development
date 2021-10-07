# Como subir o projeto no Docker?

1 - Você precisa instalar às dependências do projeto.

Referência: 
- https://www.youtube.com/watch?v=oQ08ZaOAiGU
- https://www.youtube.com/watch?v=j6ioaes03oY

Dependências:
* Instale [WSL2](https://docs.microsoft.com/pt-br/windows/wsl/install-win10) se for windows.

* Instale o [Docker](https://www.docker.com/products/docker-desktop).

* Instale o [Docker-compose](https://docs.docker.com/compose/install/) - Caso você instale no windows ou mac, já vem por padrão quando instala o docker.

* Instale [Windows Terminal](https://www.microsoft.com/pt-br/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) - Caso seja o windows.

* Instale [kernel Ubuntu](https://www.microsoft.com/pt-br/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1&activetab=pivot:overviewtab)

* Verifique se todas às dependências estão instalados usando o windows terminal no linux ubuntu. 

``` shell
docker --version
docker-compose --version
```

### Após tudo instalado.
1 - Crie uma pasta no seu **LINUX** neste caminha usando o terminal.
``` shell
# cria a pasta
mkdir ~/Database/postgres/data
# mostra onde a pasta foi criada.
ls -l ~/Database/postgres/
```

2 - Dentro da pasta do backend, você precisa criar um arquivo .env-docker.
Neste arquivo você colocará às env de banco e da aplicação. 
Na dúvida me pergunte, que irei te enviar o arquivo.
``` shell 

POSTGRES_USER="..."
POSTGRES_PASSWORD="..."
POSTGRES_DB="..."
PGDATA="/var/lib/postgresql/data/"
DATABASE_URI="postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@db/rwwv"
JWT_SECRET="..."
```

3 - Entre na pasta backend onde está nosso projeto de OPE e execute o seguinte comando.
``` shell
docker-compose up --build --detach
# o que esse comando faz?

# docker-compose: é a ferramenta/aplicação que irá pegar nossas config do arquivo docker-compose.yml e executar cada processo.

# up: após o docker-compose validar as informações ele vai subir os container.

# --build: é uma instrução que informa que antes de sub o container ele precisa ser construido.

# --detach: é para quando ele construir e subir o container ele colocar a aplicação para executar em background, sendo assim vc pode fechar o terminal após executar.
```