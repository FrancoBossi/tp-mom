import pika
import random
import string
from .middleware import (
    MessageMiddlewareCloseError,
    MessageMiddlewareDisconnectedError,
    MessageMiddlewareExchange,
    MessageMiddlewareMessageError,
    MessageMiddlewareQueue,
)
from pika.exceptions import (
    AMQPConnectionError,
    AMQPError,
    ConnectionWrongStateError,
    ChannelWrongStateError,
)

#funcion a usar para conectarse a rabbitMQ
def connection_parameters(host):
    return pika.ConnectionParameters(host=host)

#generador de nombres unicos para la cola de un subscriber
def random_queue_name(name):
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=16))
    return f"{name}_{suffix}"

#Convierte errores de Pika en las excepciones definidas por el middleware
def raise_message_error(error):
    if isinstance(
        error,
        (
            AMQPConnectionError,
            ConnectionWrongStateError,
            ChannelWrongStateError,
        ),
    ):
        raise MessageMiddlewareDisconnectedError() from error
    raise MessageMiddlewareMessageError() from error


class MessageMiddlewareQueueRabbitMQ(MessageMiddlewareQueue):

    def __init__(self, host, queue_name):
        pass

class MessageMiddlewareExchangeRabbitMQ(MessageMiddlewareExchange):
    
    def __init__(self, host, exchange_name, routing_keys):
        pass
