
**pxsh** is a minimalist CLI tool to run shell commands on multiple remote servers over SSH. It supports complex commands (`|`, `&&`, `;`) and provides quick server availability checks.

---

## 🚀 Features

- Secure remote command execution via SSH
- Supports multi-host targets (comma-separated)
- Handles complex bash syntax
- Server activity check with `--active`

---

## ⚙️ Usage

### Run command on multiple servers
```bash
python3 shell.py --server user@host1,user@host2 --send "uptime && whoami"
```
Check if servers are online
```bash
python3 shell.py --server user@host1,user@host2 --active
```

---

🛡 Security

Commands are sent only to remote hosts — never run locally. SSH handles execution securely.


---

📄 License

MIT © 2025 HnvDie

---
