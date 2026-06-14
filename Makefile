dev:
docker-compose --build --up -d

clean:
rm -rf __pycache__

test:
pytest tests/

lint:
flake8 sentinel_core/

bench:
pytest benchmarks/

format:
black sentinel_core/ tests/

all: clean format test bench lint