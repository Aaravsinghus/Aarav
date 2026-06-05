# Vexo Bot — Setup Guide
**Creator: Aarav Singh**

---

## Step 1 — Bot Token Kahan Daalein

`config.env` file open karo (same folder mein hai), aur apna token daalo:

```
BOT_TOKEN=yahan_apna_token_daalo
```

Token kaise milega:
1. https://discord.com/developers/applications jaao
2. New Application → Bot → Reset Token
3. Token copy karo aur upar daalo

---

## Step 2 — Termux Pe Run Karna

```bash
pkg update && pkg upgrade
pkg install python git
pip install -e .
vexo-setup
```

Setup mein ye poochega:
- **Instance name** → koi bhi naam do jaise `main`
- **Token** → `config.env` wala token daalo
- **Prefix** → bot ka prefix jaise `!` ya `v!`

Phir start karo:
```bash
vexo main
```

## Step 3 — Generic Linux / Python Server Pe Run Karna

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
vexo-setup
vexo main
```

Yaha bhi browser se slash commands use kar sakte ho: `/combo dynk`, `/combo carl`, `/combo falcon`, `/combo xieron`.

## Slash Commands

Bot ab slash commands ko support karta hai. Agar `!` prefix bhi chalna ho, wo bhi available rahega.

Naye custom commands load karne ke liye bot chalne ke baad console mein yeh commands use karein:
```bash
!load customcombo
!load antinuke
!load slashcommands
```

Background mein chalaane ke liye (Termux band karo tab bhi chale):
```bash
pkg install tmux
tmux new -s vexo
vexo main
# Ctrl+B phir D dabaao
```

---

## Step 3 — Linux Server Pe Run Karna

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
vexo-setup
vexo main
```

---

## Bot Discord Server Mein Kaise Add Karein

1. https://discord.com/developers/applications → apni app → OAuth2
2. Scopes mein `bot` select karo
3. Permissions mein jo chahiye select karo
4. Link copy karke browser mein open karo

---

## Common Commands (Discord mein)

| Command | Kaam |
|---------|------|
| `!help` | Saari commands dikhao |
| `!info` | Bot ki info |
| `!ping` | Bot online hai ya nahi |
| `!load <cogname>` | Cog/plugin load karo |

---

## Problems?

- **`pip install` fail ho raha hai** → `pkg install python-dev` chalao
- **Token invalid** → `config.env` mein sahi token daalo
- **Bot respond nahi kar raha** → Discord Developer Portal mein `MESSAGE CONTENT INTENT` on karo
