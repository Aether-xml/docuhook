import os, json, requests
from pathlib import Path

def get_config():
    cfg = {
        "api_key": os.getenv("DU_API_KEY", ""),
        "api_url": os.getenv("DU_API_URL", "https://openrouter.ai/api/v1"),
        "model": os.getenv("DU_MODEL", "openrouter/free")
    }
    if not cfg["api_key"]:
        home_config = Path.home() / ".docuhook.json"
        if home_config.exists():
            try:
                data = json.loads(home_config.read_text(encoding="utf-8"))
                cfg["api_key"] = data.get("api_key", cfg["api_key"])
                cfg["api_url"] = data.get("api_url", cfg["api_url"])
                cfg["model"] = data.get("model", cfg["model"])
            except Exception: pass
    return cfg

def analyze_diff(diff, readme_content):
    cfg = get_config()
    if not cfg["api_key"]: return "ERROR_NO_KEY"
    sys_prompt = "Sen sadece ham Markdown formatında çıktı veren profesyonel bir teknik yazarsın. Git diffe gore READMEyi guncelle. Degisiklik gerekmiyorsa sadece NO_CHANGES_NEEDED yaz. Baska hicbir sey ekleme."
    user_prompt = f"--- MEVCUT README ---\n{readme_content}\n\n--- DIFF ---\n{diff}"
    try:
        res = requests.post(
            f"{cfg["api_url"].rstrip("/")}/chat/completions",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {cfg["api_key"]}"},
            json={"model": cfg["model"], "messages": [{"role": "system", "content": sys_prompt}, {"role": "user", "content": user_prompt}], "temperature": 0.2},
            timeout=60
        ).json()
        return res["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"ERROR_API_{str(e)}"
