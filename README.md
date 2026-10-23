# URL Shortener

A small FastAPI service that turns long URLs into short links. Send it a URL, get back a 6-character code, and anyone who opens the short link gets redirected to the original. Links are saved in a local SQLite file (`url_shortener.db`), which is created on first run.

## Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)
- [just](https://github.com/casey/just) (optional)

## Run locally

From the project root:

```bash
uv sync
just run
```

No `just`? Start the server directly:

```bash
uv run uvicorn app.main:app --reload
```

The server runs at http://localhost:8000. Interactive API docs are at http://localhost:8000/docs.

## Get a short URL

```bash
curl -X POST http://localhost:8000/api/v1/urls \
  -H "Content-Type: application/json" \
  -d '{"url": "https://github.com/fastapi/fastapi"}'
```

Response:

```json
{
  "original_url": "https://github.com/fastapi/fastapi",
  "short_code": "sd5ivZ",
  "short_url": "http://localhost:8000/sd5ivZ"
}
```

Open the `short_url` in your browser and it takes you to the original link. Your code will be different, since codes are random.

## Endpoints

| Method | Path            | Description                                                      |
| ------ | --------------- | ---------------------------------------------------------------- |
| POST   | `/api/v1/urls`  | Create a short URL. Body: `{"url": "<long url>"}`                |
| GET    | `/{short_code}` | Redirect to the original URL, or return 404 if the code is unknown |

Invalid URLs are rejected with a 422.
