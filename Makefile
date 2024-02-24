DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
current_branch := latest
build:
	docker build -t pramodraob/hadoop-base:$(current_branch) ./base
	docker build -t pramodraob/hadoop-namenode:$(current_branch) ./namenode
	docker build -t pramodraob/hadoop-datanode:$(current_branch) ./datanode
	docker build -t pramodraob/hadoop-resourcemanager:$(current_branch) ./resourcemanager
	docker build -t pramodraob/hadoop-nodemanager:$(current_branch) ./nodemanager
	docker build -t pramodraob/hadoop-historyserver:$(current_branch) ./historyserver
	docker build -t pramodraob/hadoop-submit:$(current_branch) ./submit

wordcount:
	docker build -t hadoop-wordcount ./submit
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -mkdir -p /input/
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-wordcount
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -cat /output/*
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /output
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /input


q1:
	docker build -t hadoop-q1 ./q1
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -mkdir -p /input/
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-q1
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -cat /output/*
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /output
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /input


q2:
	docker build -t hadoop-q2 ./q2
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-q2
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -cat /user/root/out/combined.txt
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /user/root/in
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /user/root/out


q3:
	docker build -t hadoop-q3 ./q3
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-q3
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -cat /user/root/out/combined.txt
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /user/root/in
	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} pramodraob/hadoop-base:$(current_branch) hdfs dfs -rm -r /user/root/out
