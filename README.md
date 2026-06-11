# AI Network Troubleshooting Assistant

A web-based network troubleshooting tool powered by Google Gemini AI. Built as a personal project to combine my CCNA studies with Python development.

You describe a network problem in plain English and the assistant walks you through how to diagnose and fix it using real Cisco IOS commands.

---

* Why I built this

I was studying for my CCNA and kept forgetting the exact `show` commands to use during troubleshooting. I thought it would be useful to have something I could just describe a problem to and get a structured walkthrough back. So I built it.

---

* Tech used

- Python 3
- Flask
- Google Gemini API (free tier)
- HTML/CSS/JavaScript (no frameworks)

---

* How to run it

**1. Clone the repo**
```
git clone https://github.com/yourusername/ai-network-troubleshooter
cd ai-network-troubleshooter
```

**2. Install dependencies**
```
pip install -r requirements.txt
```

**3. Get a free Gemini API key**

Go to https://aistudio.google.com, sign in with Google, and create an API key. It's free.

**4. Add your API key**

Open `app.py` and replace the placeholder on line 4:
```python
GEMINI_API_KEY = "your-key-here"
```

**5. Run it**
```
python app.py
```

Then open http://localhost:5000 in your browser.

---

* What it can help with

- OSPF / EIGRP / RIP neighbor issues
- VLAN and inter-VLAN routing problems
- Spanning Tree (STP/RSTP) troubleshooting
- DHCP not assigning addresses
- NAT/PAT configuration issues
- Access Control List (ACL) problems
- Basic connectivity (ping, ARP, Layer 1-3)
- Trunk link and port configuration

---

* Project structure

```
├── app.py          # Flask app + Gemini API integration
├── index.html      # Frontend UI
├── requirements.txt
└── README.md
```

---

* Notes

- The free Gemini tier has rate limits. If you get a quota error just wait a minute and try again.
- I'm using `gemini-2.5-flash-lite` as the model — it's fast and free.
- This is a learning project, not production software. Don't use it for anything critical.

---

* What I learned

- How to call a REST API from Flask and pass results to the frontend
- Structuring a system prompt to get consistent, formatted AI responses
- A lot more Cisco IOS troubleshooting commands than I knew before

