# Backend (optional, future)
La v1 usa **Formspree** (sin servidor propio). Si más adelante quieres tu propia API, la arquitectura sería:
Frontend → Java + Spring Boot (`POST /api/contact`) → proveedor de correo (Resend, SendGrid, SMTP) → tu bandeja.
Pasos: validar con `@Valid` (nombre, email, mensaje), limitar tasa de envíos, CORS solo para tu dominio, guardar claves en `.env` (ver `../.env.example`), y cambiar `FORM_ENDPOINT` en `js/config.js` a tu URL.
