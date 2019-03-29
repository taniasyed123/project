# example REST API with authentication
A Flask app that shows civilisations and the type of army they belong to in a game called The Age of Empires 2. Upon searching for a specific country, we can also find out the ID number of the team.
the API used to obtain the civilisations were from: 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations'
the API used to obtain the ID number of the team were from:
'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/1'
The API used to obtain the Army type were from:
'https://age-of-empires-2-api.herokuapp.com/api/v1/civilization/{name}'


# to enable the correct location, set zone london,uk
gcloud config set compute/zone europe-west6-c
# put project id value and export it 
export PROJECT_ID="$(gcloud config get-value project -q)"
# pull docker using cassandra 
docker pull cassandra:latest
# run cassandra
docker run -p 9042:9042 --name cassandra -d cassandra:latest
## if google container api not enabled
gcloud services enable container.googleapis.com
# otherwise, run cassandra in cqlsh
docker exec -it cassandra cqlsh

# To enable your database in cassandra:
# setup cassandra cluster
gcloud container clusters create cassandra --num-nodes=3 --machine-type "n1-standard-2"
# specify and download cassandra service by downloading the tiny urls
wget -O cassandra-peer-service.yml http://tinyurl.com/yyxnephy
wget -O cassandra-service.yml http://tinyurl.com/y65czz8e
wget -O cassandra-replication-controller.yml http://tinyurl.com/y2crfsl8
# run the cassandra in kubernetes
kubectl create -f cassandra-peer-service.yml
kubectl create -f cassandra-service.yml
kubectl create -f cassandra-replication-controller.yml
# check single container
kubectl get pods -l name=cassandra
# scale nodes
kubectl scale rc cassandra --replicas=3
# check ring formed, keep doing this until you can see three nodes running with fairly weighted percentages shared between the three
# cassandra-cx4gc would be changed to whatever the name of your cassandra may be
kubectl exec -it cassandra-cx4gc -- nodetool status 
# run cassandra cqlsh
docker exec -it cassandra cqlsh
CREATE KEYSPACE weathertable WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 2};

## build docker
docker build -t gcr.io/${PROJECT_ID}/mydata-app:v1 .
# push docker
gcloud auth configure-docker
docker push gcr.io/${PROJECT_ID}/mydata-app:v1
# test run locally
docker run --rm -p 8080:8080 gcr.io/${PROJECT_ID}/mydata-app:v1

## run kubernetes service
kubectl run mydata-app --image=gcr.io/${PROJECT_ID}/mydata-app:v1 --port 8000
# expose for internally
kubectl expose deployment mydata-app --target-port=8000 --type=NodePort
## check kubernetes
kubectl get services
## deploy ingress
kubectl apply -f basic-ingress.yaml
## check external ip
kubectl get ingress basic-ingress

# in order to avoid any billing charges, it is crucial to clean after completion of google cloud
----------cleaning------------
## kubernetes delete
kubectl delete --all replicationcontroller
kubectl delete --all services
kubectl delete service servicename
## delete container clusters
gcloud container clusters delete cassandra
## delete ingress
kubectl delete ingress basic-ingress
## delete static ip
gcloud compute addresses delete web-static-ip --global
## delete untagged docker images
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")

--------!!!!WARNING!!! DELETE ALL CONTAINERS AND IMAGES-------
# Delete all containers
docker rm -f $(docker ps -a -q)
# Delete all images
docker rmi -f $(docker images -q)
# delete all gcloud ontainer with all of the tags
./cleanup.sh gcr.io/${PROJECT_ID}/weather-app @UP-TO-DATE@

# This is added within your code to access the database from your app and run a query when it s ran externally
# -----create keyspace and table (put under connect and session code)------
KEYSPACE = "yourkeyspace"
TABLENAME = "yourtable"

# create keyspace if not exist
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS %s
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
    """ % KEYSPACE)
print ("{} has been created".format(KEYSPACE))
# create table if not exist
session.execute("""
    CREATE TABLE IF NOT EXISTS {}.{} (
        Column1 text PRIMARY KEY,
        Column2 int,
        Column3 boolean
    )""".format(KEYSPACE, TABLENAME))
print ("{} has been created".format(TABLENAME))



# ------------------CASSANDRA TABLES------------------------
Step 1: Navigate to /home/project

Step 2: docker pull cassandra:latest

Step 3: docker run --name cassandra-test -d cassandra:latest

Step 4: wget -O mydata.csv https://tinyurl.com/y3l384qg

Step 5: docker cp mydata.csv cassandra-test:/home/mydata.csv

Step 6: docker exec -it cassandra-test cqlsh

Step 7: CREATE KEYSPACE mydata WITH REPLICATION =
        {'class' : 'SimpleStrategy', 'replication_factor' : 1};

Step 8: CREATE TABLE mydata.stats (Name text, Army_Type text PRIMARY KEY);

Step 9: COPY mydata.stats(Name, Army_Type)
        FROM '/home/mydata.csv'
        WITH DELIMITER=',' AND HEADER=TRUE;

Step 10: select * from mydata.stats;

# ------------------KUBERNETES----------------------------------

Step 1: gcloud config set compute/zone europe-west2-b

Step 2: gcloud container clusters create cassandra --num-nodes=3 --machine-type "n1-standard-2"

Step 3: wget -O cassandra-peer-service.yml http://tinyurl.com/yyxnephy

Step 4: wget -O cassandra-service.yml http://tinyurl.com/y65czz8e

Step 5: wget -O cassandra-replication-controller.yml http://tinyurl.com/y2crfsl8

Step 6: kubectl create -f cassandra-peer-service.yml

Step 7: kubectl create -f cassandra-service.yml

Step 8: kubectl create -f cassandra-replication-controller.yml

Step 9: kubectl get pods -l name=cassandra

Step 10: kubectl scale rc cassandra --replicas=3

# replace this with the name of your cassandra
Step 11: kubectl exec -it cassandra-2ggnn -- nodetool status

Step 12: kubectl cp mydata.csv cassandra-2ggnn:/mydata.csv

Step 13: kubectl exec -it cassandra-2ggnn cqlsh

Step 14: CREATE KEYSPACE mydata WITH REPLICATION =
        {'class' : 'SimpleStrategy', 'replication_factor' : 2};

Step 15: CREATE TABLE mydata.stats (Name text, Army_Type text PRIMARY KEY);

Step 16: COPY mydata.stats(Name, Army_Type)
         FROM 'mydata.csv'
         WITH DELIMITER=',' AND HEADER=TRUE;

Step 17: select * from mydata.stats;
