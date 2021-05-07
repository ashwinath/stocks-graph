.PHONY: proto
proto:
	protoc -I . \
		--python_out=generated \
		--mypy_out=generated \
		proto/*.proto

.PHONY: timescaledb
timescaledb:
	docker run -d \
		--name timescaledb \
		-p 5432:5432 \
		-e POSTGRES_PASSWORD=password \
		-v /etc/timescaledb:/var/lib/postgresql/data \
		timescale/timescaledb:latest-pg12

.PHONY: connectdb
connectdb:
	docker run --rm \
		-ti \
		-e POSTGRES_PASSWORD=password \
		-e PGPASSWORD=password \
		--net host \
		postgres:12 psql -U postgres -d postgres -p 5432 -h localhost

.PHONY: grafana
grafana:
	docker volume create grafana-storage
	docker run -d \
		--net host \
		--name=grafana \
		-e "GF_INSTALL_PLUGINS=grafana-piechart-panel" \
		-v grafana-storage:/var/lib/grafana \
		grafana/grafana:7.4.2
