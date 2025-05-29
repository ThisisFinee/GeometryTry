# Shape Service API

Сервис для вычисления площади геометрических фигур и дополнительных проверок (например, является ли треугольник прямоугольным).

---

## Запуск

### 1. Склонировать репозиторий
```bash
git clone https://github.com/yourusername/shape-service.git
cd shape-service
```

### 2. Запустить docker compose
```bash
docker compose up -d --build
```

Теперь API будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

---

## Примеры запросов

### Получить список доступных фигур
```bash
curl -X GET http://localhost:8000/shapes
```
Пример ответа:
```json
{
  "circle": "Circle",
  "triangle": "Triangle"
}
```

### Вычислить площадь круга
```bash
curl -X POST http://localhost:8000/compute-area \
  -H "Content-Type: application/json" \
  -d '{"type": "circle", "parameters": {"radius": 5}}'
```
Ответ:
```json
{
  "type": "Circle",
  "area": 78.5398,
  "additional": {
    "text": "Valid circle",
    "is_specific": true
  }
}
```

### Вычислить площадь треугольника
```bash
curl -X POST http://localhost:8000/compute-area \
  -H "Content-Type: application/json" \
  -d '{"type":"triangle", "parameters":{"a":3,"b":4,"c":5}}'
```
Ответ:
```json
{
  "type": "Triangle",
  "area": 78.5398,
  "additional": {
    "text": "Valid circle",
    "is_specific": true
  }
}
```

### Вычислить площадь треугольника (автоопределение типа)
```bash
curl -X POST http://localhost:8000/compute-area \
  -H "Content-Type: application/json" \
  -d '{"parameters": {"a": 3, "b": 4, "c": 5}}'
```
Ответ:
```json
{
  "type": "Triangle",
  "area": 6.0,
  "additional": {
    "text": "It's a right-anled triangle",
    "is_specific": true
  }
}
```

---

## Тестирование

Установить `pytest`:
```bash
pip install pytest
```

Запуск тестов:
```bash
pytest --maxfail=1 --disable-warnings -q
```

---
