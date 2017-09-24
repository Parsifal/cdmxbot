# cdmxbot
Bot para informacion sobre el sismo de cdmx

Actualmente (20-sept-17 3:10pm) tiene la siguiente funcionalidad:

Al mencionar al bot con el hashtag #buscoa seguido de un nombre o palabras clave, el bot regresa los últimos 5 tweets mencionando eso.

Ejemplos:
@cdmxbot #buscoa Carlos Herrera

@cdmxbot #buscoa cuenta bancaria

Obviamente se puede extender a:

-Usar distintas hashtags
-Guardar los tweets encontrados
-Guardar los tweets que se reciben, para análisis posterior

# Arquitectura
Pubsub:
- **Publisher**: recibe tweets por stream y los publica en la cola.
- **Subscriber**: consulta diferentes sources, unifica la respuesta y contesta el tweet.

# Desarrollo

Este proyecto tiene pocas dependencias visibles:
- `pipenv`
- `docker`

En un futuro cercano, la única dependencia será Docker.

## Configúralo
Usa el `pub.env.dist` para crear tu `pub.env` con los tokens de tu aplicación (que puedes generar/encontrar [acá](https://apps.twitter.com/)).

En `config.yml` puedes cambiar los temas que el bot va a seguir.

## Echándolo a andar
1. Levanta los dockers:
```bash
$ docker-compose up -d
```

2. Levanta el publisher (en una subshell):
```bash
$ (eval $(cat pub.env) python pub.py)
```
