https://hellokube.dev/posts/three-ways-zookeepeerless-kafka/

https://github.com/marcosschroh/dataclasses-avroschema

https://kafka-python.readthedocs.io/en/master/apidoc/KafkaClient.html

### Debezium Mongo Connector

```
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{
    "name": "inventory-connector",
    "config": {
        "connector.class" : "io.debezium.connector.mongodb.MongoDbConnector",
        "tasks.max" : "1",
        "mongodb.hosts" : "rs0/mongodb:27017",
        "mongodb.name" : "dbserver1",
        "database.include.list" : "inventory",
        "database.history.kafka.bootstrap.servers" : "kafka:9092"
    }
}'
```

Command for replicaset

```
docker ps 
```

```
docker exec -it <container-id-of-mongo-service> /bin/bash
```

```
mongo
```

```
rs.initiate();
```

```
use inventory
```

```
db.createCollection("warehouse");
```

```
db.warehouse.insertOne({"name": "pan", "quantity":1});
```