# ICE Exercise

This exercise involves running python application in kubernetes that uses a Rabbitmq service to send and receive messages 

## RabbitMQ Installation

Use helm to install RabbitMQ

```bash
helm install icerabbitmq helm_charts/rabbitmq/ 
```

## Python application Installation

```bash
kubectl apply -f iceexecise1.json
```

## View the logs: 

```bash
kubectl logs iceexercise1   -f

Pika version 1.1.0 connecting to ('10.96.152.142', 5672)
Socket connected: <socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('172.17.0.4', 40928), raddr=('10.96.152.142', 5672)>
Streaming transport linked up: (<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f0dcbe72ad0>, _StreamingProtocolShim: <SelectConnection PROTOCOL transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f0dcbe72ad0> params=<ConnectionParameters host=rabbitmq-1600877891 port=5672 virtual_host=/ ssl=False>>).
AMQPConnector - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f0dcbe72ad0> params=<ConnectionParameters host=rabbitmq-1600877891 port=5672 virtual_host=/ ssl=False>>
AMQPConnectionWorkflow - reporting success: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f0dcbe72ad0> params=<ConnectionParameters host=rabbitmq-1600877891 port=5672 virtual_host=/ ssl=False>>
Connection workflow succeeded: <SelectConnection OPEN transport=<pika.adapters.utils.io_services_utils._AsyncPlaintextTransport object at 0x7f0dcbe72ad0> params=<ConnectionParameters host=rabbitmq-1600877891 port=5672 virtual_host=/ ssl=False>>
Created channel=1
 [x] Sent 'Hello World!'
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello World!'


```

