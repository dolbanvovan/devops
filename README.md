Отчет по практическому заданию:

Репозиторий проекта: https://github.com/dolbanvovan/devops

Dockerfile: https://github.com/dolbanvovan/devops/blob/main/Dockerfile

Docker Compose: https://github.com/dolbanvovan/devops/blob/main/docker-compose.yml

CI/CD Workflow: https://github.com/dolbanvovan/devops/blob/main/.github/workflows/deploy.yml

Docker Hub образ: https://hub.docker.com/r/loshok1311/cat-app

Работающие сервисы на VPS (158.160.153.23):

Приложение: http://158.160.153.23:5000

Health check: http://158.160.153.23:5000/health

Метрики: http://158.160.153.23:5000/metrics

Prometheus UI: [http://158.160.153.23:9090](http://158.160.153.23:9090/graph?g0.expr=increase(http_requests_total%5B1h%5D)&g0.tab=0&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h)

cAdvisor UI: http://158.160.153.23:8080
