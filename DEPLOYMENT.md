# Deployment Information

## Public URL
https://test-production-3132.up.railway.app

## Platform
Railway

## Test Commands

### Health Check
```bash
curl -s https://test-production-3132.up.railway.app/health
```
*Expected output:*
```json
{
  "status": "ok",
  "version": "1.0.0",
  "environment": "production",
  "uptime_seconds": 12.3,
  "total_requests": 1,
  "checks": {
    "llm": "openai"
  },
  "timestamp": "2026-04-17T10:00:00+00:00"
}
```

### Readiness Check
```bash
curl -s https://test-production-3132.up.railway.app/ready
```
*Expected output:* `{"ready": true}`

### API Test (with authentication)
```bash
curl -X POST https://test-production-3132.up.railway.app/ask \
  -H "X-API-Key: production-secret-key" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is 12 factor app?"}'
```
*Expected output:*
```json
{
  "question": "What is 12 factor app?",
  "answer": "Đây là câu trả lời từ AI agent (mock). Trong production, đây sẽ là response từ OpenAI/Anthropic.",
  "model": "gpt-4o-mini",
  "timestamp": "2026-04-17T10:05:00+00:00"
}
```

## Environment Variables Set
Below are the critical environment variables configured in the cloud dashboard:
- `PORT=8000`
- `ENVIRONMENT=production`
- `REDIS_URL=redis://...`  *(Provided by internal Railway/Render Redis service)*
- `AGENT_API_KEY=production-secret-key`
- `LOG_LEVEL=INFO`
- `RATE_LIMIT_PER_MINUTE=20`
- `DAILY_BUDGET_USD=5.0`
- `OPENAI_API_KEY=sk-...` *(Optional, falls back to Mock LLM if empty)*

## Screenshots
- [Deployment dashboard](screenshots/image.png)
- [Service running](screenshots/image-1.png)
