# AI Network Troubleshooting Assistant

A web app that helps diagnose and fix Cisco network issues using AI. You describe the problem, it gives you the exact `show` commands to run and walks you through fixing it — step by step.

Built this while preparing for my CCNA to make troubleshooting practice more interactive.

🔗 **Live Demo:** [Try it locally — setup takes 2 minutes](#how-to-run-it)

---

## What it does

Most network issues follow patterns. OSPF neighbor down? Check hello timers, area mismatch, authentication. VLAN not communicating? Check trunk, allowed VLANs, SVI. This tool knows those patterns and guides you through them.

You type something like:

> *"OSPF neighbors not forming between R1 and R2, both in area 0"*

And it responds with:

- What's likely causing it
- The exact Cisco `show` and `debug` commands to confirm
- Step-by-step fix with IOS config examples
- Why the fix works (useful for actually learning, not just copying)

---

## Tech stack

| | |
|---|---|
| Backend | Python, Flask |
| AI | Google Gemini API |
| Frontend | HTML, CSS, Vanilla JS |
| Deployment | Localhost (Flask dev server) |

---

## Topics covered

The assistant handles most CCNA-level troubleshooting scenarios:

- **Routing** — OSPF, EIGRP, RIP, static routes, route redistribution
- **Switching** — VLANs, inter-VLAN routing, STP/RSTP, EtherChannel, trunk links
- **IP Services** — DHCP, DNS, NAT/PAT, NTP
- **Security** — Standard and extended ACLs, port security
- **Connectivity** — Layer 1-3 issues, ARP, ping failures, default gateway problems
- **Subnetting** — VLSM, CIDR, address planning

---

## How to run it

**Requirements:** Python 3, a free Google Gemini API key

```bash
# 1. Clone the repo
git clone https://github.com/Priyanshikushwah05/ai-network-troubleshooter
cd ai-network-troubleshooter

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Gemini API key (free at aistudio.google.com)
# Open app.py and set your key on line 4

# 4. Run
python app.py
```

Open http://localhost:5000 — that's it.

---

## Screenshots

> UI shows a dark-themed chat interface with a sidebar of common issues (OSPF down, VLAN routing, DHCP failure etc.) and a chat window where the AI responds with structured diagnostics and Cisco IOS commands.



---

## Project structure

```
ai-network-troubleshooter/
├── app.py          # Flask server + Gemini API calls
├── index.html      # Chat UI (pure HTML/CSS/JS)
├── requirements.txt
└── README.md
```

---

## What I learned building this

- How to structure AI system prompts to get consistent, formatted responses
- Integrating a third-party REST API (Gemini) into a Flask backend
- Handling API rate limits and error responses gracefully
- A lot more about Cisco IOS troubleshooting than I expected — writing the prompts forced me to think through every failure scenario properly

---

## Known limitations

- Free Gemini tier has rate limits (60 requests/minute). If you hit a quota error, wait a moment and retry.
- No authentication — meant for local/personal use only
- Responses are AI-generated, always verify commands in a lab before using on production gear

---

## Future improvements

- [ ] Add Packet Tracer / GNS3 topology diagram support
- [ ] Save and export troubleshooting sessions as PDF
- [ ] Add a subnet calculator tool
- [ ] Deploy to a cloud server

