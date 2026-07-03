import sys, subprocess
from pathlib import Path

def install_hook():
    hook_path = Path(".git/hooks/pre-commit")
    if not hook_path.parent.exists():
        print("Hata: .git/hooks klasörü bulunamadı.")
        sys.exit(1)
    hook_content = "#!/bin/sh\ndocuhook --hook\n"
    hook_path.write_text(hook_content, encoding="utf-8")
    subprocess.run(["chmod", "+x", str(hook_path)])
    print("Pre-commit kancası başarıyla kuruldu!")
