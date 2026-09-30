from flask import Flask, render_template, request, redirect, url_for, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import os
import random

app = Flask(__name__)

# 1. МЕТРИКА: Счётчик всех посещений/запросов для Prometheus
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Общее количество запросов к приложению'
)

# Хранилище картинок в памяти (для выполнения условия "редактируемость")
images = [
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F0.gif?alt=media&token=0fff4b31-b3d8-44fb-be39-723f040e57fb",
    "https://firebasestorage.googleapis.com/v0/b/docker-curriculum.appspot.com/o/catnip%2F1.gif?alt=media&token=2328c855-572f-4a10-af8c-23a6e1db574c"
]


@app.route("/")
def index():
    # Увеличиваем счётчик при каждом просмотре страницы
    REQUEST_COUNT.inc()

    url = random.choice(images) if images else ""
    return render_template("index.html", url=url, images=images)


# 2. РЕДАКТИРУЕМОСТЬ: Добавление новой картинки через форму
@app.route("/add", methods=["POST"])
def add_image():
    new_url = request.form.get("url")
    if new_url:
        images.append(new_url)
    return redirect(url_for("index"))


# 2. РЕДАКТИРУЕМОСТЬ: Удаление картинки по индексу
@app.route("/delete/<int:img_id>", methods=["POST"])
def delete_image(img_id):
    if 0 <= img_id < len(images):
        images.pop(img_id)
    return redirect(url_for("index"))


# 3. HEALTH CHECK: Обязательно по ТЗ
@app.route("/health")
def health():
    return jsonify(status="ok"), 200


# 4. ЭНДПОИНТ МЕТРИК: Prometheus будет забирать метрики отсюда
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))