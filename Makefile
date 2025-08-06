# Tower Jump Analyzer - Makefile
# Author: Bruno Vinícius


# Build and run backend
run:
	docker compose up --build

# Stop and remove containers
stop:
	docker compose down

# View real-time logs
logs:
	docker compose logs -f

# Clean output files
clean:
	rm -rf output/*

# Rebuild without cache
rebuild:
	docker compose down
	docker compose build --no-cache
	docker compose up

# Open shell in running backend container
shell:
	docker compose run --rm backend bash

# Run unit tests
test:
	docker compose run --rm -e PYTHONPATH=/app/ backend pytest -vv

# Frontend : Generate results + Enable UI
run-frontend:
	docker compose up --build &
	sleep 10  
	mkdir -p frontend/public/output
	cp output/tower_jump_analysis.csv frontend/public/output/
	cd frontend && npm install && npm run dev
