# SEOS REST API Reference

SEOS can run as a headless REST API server, allowing other applications (like the VS Code Extension or custom scripts) to interact with it programmatically.

---

## Starting the Server

To start the API server, run SEOS and use the `/serve` command:

```bash
seos
> /serve
```

The server will start on:

```text
http://127.0.0.1:8080
```

---

## Interactive Docs (Swagger UI)

Because SEOS uses FastAPI, interactive API documentation is automatically generated.

Once the server is running, open your browser and navigate to:

```text
http://127.0.0.1:8080/docs
```

---

# Endpoints

## 1. Health Check

Verifies that the SEOS API is running.

**URL**

```text
/
```

**Method**

```text
GET
```

**Response**

```json
{
  "status": "ok",
  "message": "SEOS API is running"
}
```

---

## 2. Chat

Sends a message to the SEOS ChatAgent.

The agent will process the message, use conversational memory, and delegate to other agents if necessary.

**URL**

```text
/chat
```

**Method**

```text
POST
```

**Body**

```json
{
  "message": "Explain what the file core/kernel.py does"
}
```

---

## 3. Code Review

Triggers the ReviewAgent to audit a specific Python file for bugs, vulnerabilities, and code smells.

**URL**

```text
/review
```

**Method**

```text
POST
```

**Body**

```json
{
  "review": "**Bugs:**\n1. In the __init__ method...\n**Recommendations:**\n..."
}
```
