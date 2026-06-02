# 💈 Telegram Barbershop CRM Bot

Production-ready Telegram CRM bot for barbershops and service businesses.

## Features

* 📅 Online booking
* 👤 Personal cabinet
* ❌ Booking cancellation
* 💈 Service selection
* 📆 Dynamic 14-day calendar
* ⏰ Automatic slot availability
* 📊 Admin statistics
* 📋 Client management
* ☁️ Railway deployment
* 🐘 PostgreSQL database

## Admin Commands

* `/clients` — list of clients
* `/today` — today's bookings
* `/week` — upcoming bookings
* `/stats` — booking statistics

## Tech Stack

* Python 3
* Aiogram 3
* PostgreSQL
* Railway
* GitHub

## Architecture

* FSM (Finite State Machine)
* PostgreSQL persistence
* Inline keyboards
* Modular handlers
* Environment variables

## Deployment

The bot is deployed on Railway and uses PostgreSQL for data storage.

## Screenshots

### Main Menu

![Main Menu](images/main-menu.png)

### Booking Process

![Booking](images/booking.png)

### Personal Cabinet

![Personal Cabinet](images/my-bookings.png)

### Admin Panel

![Admin Panel](images/admin-panel.png)
