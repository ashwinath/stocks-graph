.PHONY: proto
proto:
	protoc -I . \
		--python_out=generated \
		--mypy_out=generated \
		proto/*.proto

.PHONY: questdb
questdb:
	docker run -d \
		--name questdb \
		-p 9000:9000 \
		-p 8812:8812 \
		-v /etc/questdb:/root/.questdb/db \
		questdb/questdb:5.0.6.2-linux-amd64

.PHONY: connectdb
connectdb:
	docker run --rm -ti -e POSTGRES_PASSWORD=mysecretpassword -e PGPASSWORD=quest --net host postgres:12 psql -U admin -d qdb -p 8812 -h localhost
