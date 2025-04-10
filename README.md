# 🏨 Hotel Reservation API - Django REST Framework

This project is a simple REST API built using Django and Django REST Framework that allows users to:

- 📋 View a list of hotels
- ➕ Add a new hotel

---

## 🚀 Features

- Retrieve all hotels (GET)
- Add a new hotel (POST)
- Uses Django ORM for database operations
- Boolean field to track availability of hotels
- JSON-based REST API

---

## 📦 Technologies Used

- Python 3.x
- Django
- Django REST Framework
- SQLite (default Django DB)

---

## 🧱 Model Structure

The `Hotel` model includes the following fields:

| Field Name       | Type      | Description                      |
|------------------|-----------|----------------------------------|
| `name`           | String    | Name of the hotel (max 100 chars)|
| `availability`   | Boolean   | Whether the hotel is available   |
| `price_per_night`| Decimal   | Price per night (up to 9999.99)  |

---

## 🔌 API Endpoints

Base URL: `http://127.0.0.1:8000/api/`

### 📍 GET `/hotels/`

Returns a list of all hotels in the database.

**Response example:**

```json
[
  {
    "id": 1,
    "name": "Seaside Inn",
    "availability": true,
    "price_per_night": "150.00"
  }
]
