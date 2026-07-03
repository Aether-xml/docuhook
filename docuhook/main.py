import sys, difflib, argparse, json
from pathlib import Path
from docuhook.git_utils import get_staged_diff, run_git
from docuhook.ai_utils import analyze_diff
from docuhook.installer import install_hook

def configure_globally():
    api_key = input("OpenRouter API Key girin: ").strip()
    config = {"api_key": api_key, "api_url": "https://openrouter.ai/api/v1", "model": "openrouter/free"}
    (Path.home() / ".docuhook.json").write_text(json.dumps(config, indent=4), encoding="utf-8")
    print("Küresel ayarlar kaydedildi! (~/.docuhook.json)")

def main():
    parser = argparse.ArgumentParser(description="DocuHook")
    parser.add_argument("--install", action="store_true", help="Kanca kur")
    parser.add_argument("--hook", action="store_true", help="Kanca modu")
    parser.add_argument("--configure", action="store_true", help="Küresel API Key ayarla")
    args = parser.parse_args()

    if args.configure:
        configure_globally()
        sys.exit(0)
    if args.install:
        install_hook()
        sys.exit(0)

    diff = get_staged_diff()
    if not diff:
        if args.hook: sys.exit(0)
        print("Staged değişiklik yok."); sys.exit(1)

    readme_path = next((p for p in Path('.').glob('*') if p.name.lower() == 'readme.md'), None)
    if not readme_path:
        if args.hook: sys.exit(0)
        print("README.md yok."); sys.exit(1)

    readme_content = readme_path.read_text(encoding='utf-8')
    ai_resp = analyze_diff(diff, readme_content)

    if ai_resp == "ERROR_NO_KEY":
        print("Hata: API anahtarı bulunamadı! docuhook --configure çalıştırın.")
        sys.exit(1 if args.hook else 0)
    elif ai_resp.startswith("ERROR_API_"):
        print(f"API Hatası: {ai_resp}")
        sys.exit(1 if args.hook else 0)

    if ai_resp.startswith("```markdown"): ai_resp = ai_resp[11:].rstrip("` \n")
    elif ai_resp.startswith("```"): ai_resp = ai_resp[3:].rstrip("` \n")

    if "NO_CHANGES_NEEDED" in ai_resp:
        print("DocuHook: Doküman güncel.")
        sys.exit(0)

    if args.hook:
        readme_path.write_text(ai_resp, encoding='utf-8')
        run_git(['add', str(readme_path)])
        print("DocuHook: README.md otomatik güncellendi.")
        sys.exit(0)

    print("\n--- ÖNERİLEN DEĞİŞİKLİKLER ---")
    diff_lines = list(difflib.unified_diff(readme_content.splitlines(), ai_resp.splitlines(), fromfile='Eski', tofile='Yeni', lineterm=''))
    for line in diff_lines: print(line)
    
    print("\n" + "="*40)
    if input("README.md güncellensin mi? [y/N]: ").strip().lower() == 'y':
        readme_path.write_text(ai_resp, encoding='utf-8')
        run_git(['add', str(readme_path)])
        print("README.md güncellendi ve sahneye eklendi.")
