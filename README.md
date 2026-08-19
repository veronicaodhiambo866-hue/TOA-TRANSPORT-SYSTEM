# TOA Transport System

Flask backend for the TOA staff transport management dashboard.

## Run locally

```powershell
..\venv\Scripts\python.exe app.py
```

Open `http://127.0.0.1:5000` in a browser.

## Endpoints

- `GET /` serves the transport dashboard.
- `GET /api/health` reports the backend status.
- `GET /api/dashboard` returns the dashboard summary data as JSON.