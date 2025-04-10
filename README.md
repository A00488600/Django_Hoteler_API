# 🏨 Hotel Reservation API - Django REST Framework

This project is a simple REST API built using Django and Django REST Framework that allows users to:

- 📋 View a list of hotels
- ➕ Add a new hotel
- 🛏️ Submit a reservation and receive a confirmation number

---

## 🚀 Features

- Retrieve all hotels (GET)
- Confirm a reservation (POST)
- Uses Django ORM for database operations
- UUID-based confirmation number generation
- JSON-based REST API
- Stores data in SQLite (Django default)

---

## 📦 Technologies Used

- Python 3.x
- Django
- Django REST Framework
- SQLite (default Django DB)

---

## 🧱 Model Structure

### 🔹 Hotel

| Field Name        | Type     | Description                           |
|-------------------|----------|---------------------------------------|
| `name`            | String   | Name of the hotel (max 100 chars)     |
| `availability`    | Boolean  | Whether the hotel is available        |
| `price_per_night` | Decimal  | Price per night (up to 9999.99)       |

### 🔹 Guest

| Field Name     | Type    | Description                       |
|----------------|---------|-----------------------------------|
| `guest_name`   | String  | Name of the guest (max 100 chars) |
| `gender`       | String  | Gender of the guest               |

### 🔹 Reservation

| Field Name           | Type            | Description                             |
|----------------------|-----------------|-----------------------------------------|
| `hotel_name`         | String          | Name of the hotel                       |
| `checkin`            | String          | Check-in date                           |
| `checkout`           | String          | Check-out date                          |
| `guests`             | ManyToManyField | List of guests                          |
| `confirmation_number`| String          | Auto-generated reservation ID (UUID)    |

---

## 🔌 API Endpoints

Base URL: `http://127.0.0.1:8000/api/`

---

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
  },
  {
    "id": 2,
    "name": "Sunset Stay",
    "availability": false,
    "price_per_night": "120.00"
  }
]
