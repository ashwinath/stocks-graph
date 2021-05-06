.PHONY: proto
proto:
	protoc -I . \
		--python_out=generated \
		--mypy_out=generated \
		proto/*.proto

.PHONY: questdb
questdb:
	docker run -d \
		-p 9000:9000 \
		-p 8812:8812 \
		-v /etc/questdb:/root/.questdb/db \
		questdb/questdb:5.0.6.2-linux-amd64
