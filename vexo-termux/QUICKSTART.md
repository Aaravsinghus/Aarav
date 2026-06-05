# ⚡ Vexo Bot - Quick Reference Card

## 🚀 Installation (One Command!)

```bash
bash install-auto.sh
```

**Choose your platform:**
- ✅ Termux (Android)
- ✅ Linux (Ubuntu/Debian)
- ✅ macOS

---

## 🔑 Get Bot Token

1. https://discord.com/developers/applications
2. New Application → Bot → Copy Token
3. Paste in `config.env`

---

## 📝 Bot Configuration

**File:** `config.env`

```
BOT_TOKEN=your_token_here
PREFIX=!
```

---

## 🎯 Essential Commands

### Slash Commands (Type `/`)
| Command | What it does |
|---------|------------|
| `/ping` | Latency check |
| `/info` | Bot info |
| `/help` | Help message |
| `/serverinfo` | Server details |
| `/userinfo` | User info |
| `/invite` | Bot invite link |

### AntiNuke Commands (Type `!`)
| Command | What it does |
|---------|------------|
| `!antinuke enable` | Turn on protection |
| `!antinuke disable` | Turn off |
| `!antinuke status` | Check status |
| `!antinuke threshold 5` | Set action limit |
| `!antinuke whitelist @role` | Safe role |
| `!antinuke blacklist @user` | Suspicious user |

### General Commands
| Command | What it does |
|---------|------------|
| `!help` | All commands |
| `!ping` | Pong! |
| `!info` | Bot info |

---

## 🏃 Quick Start (5 Minutes)

### Step 1️⃣ Get Token
```
Discord Developer Portal → Bot → Copy Token
```

### Step 2️⃣ Configure
```bash
nano config.env
# Paste token, save
```

### Step 3️⃣ Install
```bash
bash install-auto.sh
```

### Step 4️⃣ Add to Server
```
Developer Portal → OAuth2 → Use generated link
```

### Step 5️⃣ Test
```
Type: /ping
Bot: Shows latency ✅
```

---

## 🛠️ Setup by Platform

### Termux (Android)
```bash
bash install-auto.sh
# Follow prompts
python -m vexo
```

### Linux Server
```bash
bash install-auto.sh
# Creates systemd service (auto-start)
sudo systemctl start vexo
```

### Web Server (PythonAnywhere, etc.)
See: **DEPLOYMENT.md**

---

## 🎨 Customize Colors

**File:** `vexo/cogs/slashcommands/theme.py`

```python
# Change color (RGB format)
PRIMARY = discord.Color.from_rgb(255, 0, 0)  # Red
PRIMARY = discord.Color.from_rgb(0, 255, 0)  # Green
PRIMARY = discord.Color.from_rgb(0, 0, 255)  # Blue
```

---

## 📚 Documentation Files

| File | Read when... |
|------|-------------|
| **README.md** | Want overview |
| **SETUP_GUIDE.md** | Setting up bot |
| **FEATURES.md** | Want feature details |
| **DEPLOYMENT.md** | Deploying to server |
| **CUSTOMIZATION.md** | Customizing bot |
| **This file** | Need quick reference |

---

## 🔗 Important Links

- **Discord Developers:** https://discord.com/developers
- **Bot Invite:** Ask bot with `/invite`
- **Documentation:** Read included .md files

---

## 💡 Pro Tips

1. **Enable Discord Developer Mode:**
   - Settings → App Settings → Advanced → Developer Mode
   - Now right-click to copy IDs

2. **Keep Bot Running on Phone:**
   ```bash
   tmux new -s vexo
   python -m vexo
   # Ctrl+B then D
   ```

3. **Update Bot:**
   ```bash
   git pull
   pip install -r requirements/base.txt
   ```

4. **Check Logs:**
   - Termux: See console output
   - Linux: `sudo journalctl -u vexo -f`

---

## ✅ Pre-Deployment Checklist

- [ ] Token copied from Developer Portal
- [ ] Token pasted in config.env
- [ ] Bot added to server
- [ ] MESSAGE CONTENT INTENT enabled
- [ ] Bot permissions set correctly
- [ ] Python 3.8+ installed
- [ ] All dependencies installed
- [ ] Can run bot successfully
- [ ] Slash commands work (`/ping`)
- [ ] Prefix commands work (`!help`)

---

## 🐛 Quick Fixes

**Bot not responding?**
```
→ Enable MESSAGE CONTENT INTENT in Developer Portal
→ Restart bot: Ctrl+C then python -m vexo
```

**Slash commands not showing?**
```
→ Wait 1-3 minutes
→ Restart Discord
→ Check bot token is correct
```

**Installation errors?**
```
→ Make sure Python 3.8+ is installed
→ Run: pip install --upgrade pip
→ Run: bash install-auto.sh again
```

---

## 🌟 New Features in This Version

✨ **AntiNuke** - Raid protection  
⚡ **Slash Commands** - Modern /commands  
🎨 **Modern Theme** - Colored embeds  
📦 **Auto-Install** - One-click setup  
📚 **Full Docs** - Complete guides  

---

## 👤 Create Custom Command

Edit: `vexo/cogs/slashcommands/__init__.py`

```python
@app_commands.command(name="hi", description="Say hi")
async def hi(self, interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")
```

Use: `/hi` → Bot responds: "Hello!"

---

## 📊 Common Settings

### Bot Prefix
**File:** `config.env`
```
PREFIX=!        # Default
PREFIX=v!       # Or this
PREFIX=>        # Or anything
```

### Admin User
**File:** `config.env`
```
OWNER_ID=123456789  # Your Discord ID
```

### Custom Color
**File:** `vexo/cogs/slashcommands/theme.py`
```python
PRIMARY = discord.Color.from_rgb(88, 101, 242)
```

---

## 🎯 Next Steps

1. Run installer
2. Test bot (`/ping`)
3. Read FEATURES.md for more commands
4. Customize colors/commands
5. Add to more servers
6. Enjoy! 🎉

---

## 📞 Emergency Help

**Bot crashes on startup?**
- Check Python 3.8+: `python3 --version`
- Check token: `cat config.env`
- Check intents: Discord Developer Portal

**Can't find Discord Developer Portal?**
- Go to: https://discord.com/developers/applications
- Login with your Discord account
- Click "New Application"

**Still stuck?**
- Read SETUP_GUIDE.md (detailed instructions)
- Check Discord bot documentation
- Make sure all dependencies installed

---

**Quick Start:** `bash install-auto.sh` 🚀

**Made with ❤️ for easy Discord bot setup**
