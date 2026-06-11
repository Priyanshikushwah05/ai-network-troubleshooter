from flask import Flask, request, jsonify, send_file
import requests
import io

app = Flask(__name__)

import os
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "your-key-here")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"
SYSTEM_PROMPT = """You are NetBot, an expert AI network troubleshooting assistant specializing in Cisco networking and CCNA-level concepts. Help engineers diagnose and resolve network issues.

Your expertise:
- OSI Model troubleshooting (Layer 1-7)
- Cisco IOS commands and configurations  
- Routing protocols: OSPF, EIGRP, RIP, BGP
- VLANs, STP, trunking, EtherChannel
- NAT/PAT, ACLs, DHCP, DNS
- Subnetting and IP addressing

Structure responses with:
- DIAGNOSIS: what might be wrong
- VERIFICATION COMMANDS: Cisco show/debug commands
- RESOLUTION STEPS: how to fix it
- EXPLANATION: why this works

Always give specific Cisco IOS commands in code blocks."""

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    conversation = data.get("messages", [])
    if not conversation:
        return jsonify({"error": "No messages"}), 400

    last_msg = conversation[-1]["content"]
    if len(conversation) == 1:
        prompt = SYSTEM_PROMPT + "\n\nUser: " + last_msg
    else:
        hist = "\n".join(
            ("User: " if m["role"] == "user" else "NetBot: ") + m["content"]
            for m in conversation[:-1]
        )
        prompt = SYSTEM_PROMPT + "\n\nConversation:\n" + hist + "\n\nUser: " + last_msg

    try:
        resp = requests.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30
        )
        print("Gemini status:", resp.status_code)
        result = resp.json()
        print("Gemini response:", result)
        
        if resp.status_code != 200:
            error_msg = result.get("error", {}).get("message", "Unknown error")
            return jsonify({"error": error_msg}), 500
            
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"reply": reply})
    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
