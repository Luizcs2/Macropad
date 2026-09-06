run app 
Run the app

Start the server (development, reload enabled):

```bash
uvicorn app.main:app --reload
```

Available endpoints and example requests

- Health check (GET):

```bash
curl -s http://127.0.0.1:8000/health
# => {"status":"ok"}
```

- Open an app (POST /commands/app/open)

Request body: JSON with a `name` field matching an entry in `app/commands/<os>.json` (examples: `notepad`, `chrome`, `vscode`).

```bash
curl -X POST http://127.0.0.1:8000/commands/app/open \
	-H "Content-Type: application/json" \
	-d '{"name":"notepad"}'
```

- Put the system to sleep (POST /commands/system/sleep)

Request body: JSON with a `name` value that exists under the `system` section in `app/commands/<os>.json` (example: `sleep`).

```bash
curl -X POST http://127.0.0.1:8000/commands/system/sleep \
	-H "Content-Type: application/json" \
	-d '{"name":"sleep"}'
```

For more commands, see the JSON files in `app/commands/` for your OS.