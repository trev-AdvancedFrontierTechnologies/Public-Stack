# Security Policy

This repository is public-safe by design.

Do not commit:

- Private keys
- SSL certificates or CSR private material
- `.env` files
- API keys
- Passwords
- Tokens
- Docker image archives
- Docker volume archives
- Full Docker desktop packages
- Model weights
- Customer data
- Internal evidence records
- Private binders
- Logs containing secrets
- SAM.gov, Namecheap, or GitHub account credentials

Before every push, run:

```bash
./scripts/public_safety_check.sh
