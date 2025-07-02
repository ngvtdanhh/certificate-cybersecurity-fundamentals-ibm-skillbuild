# 🛡️ Incident Response Scenario – Unauthorized Access

## Context
User account shows login attempts from `192.0.2.44`. Time: 03:17 AM UTC.

## Actions
- Lock account
- Preserve `/var/log/auth.log`
- Notify user

## Commands
```bash
grep "Failed password" /var/log/auth.log
lastlog | grep user
who | grep user
```

## Follow-up

- Enforce password reset

- Enable 2FA

- User training on phishing
