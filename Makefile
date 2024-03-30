DC = docker compose
APP_FILE = docker_compose/app.yml
STORAGE_FILE = docker_compose/storage.yml

.PHONY: app
app:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f