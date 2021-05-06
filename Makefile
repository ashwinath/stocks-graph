.PHONY: proto
proto:
	protoc -I . \
		--python_out=generated \
		--mypy_out=generated \
		proto/*.proto
