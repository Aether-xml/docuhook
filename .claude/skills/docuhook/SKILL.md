---
name: docuhook
description: "Automatically updates and synchronizes project README.md and documentation with staged git changes (git diff) using the docuhook CLI tool."
version: "1.0.0"
---

# DocuHook Skill

## Overview
Bu yetenek, geliştiricinin yazdığı kodlara göre `README.md` dosyasını otomatik olarak senkronize etmesini sağlar.

## Ne Zaman Tetiklenmeli?
- Kullanıcı `/docuhook` komutunu yazdığında.
- Kullanıcı "README dosyasını güncelle", "dokümanları eşitle" veya "kod değişikliklerimi README'ye işle" dediğinde.

## Talimatlar

1. Öncelikle terminal aracını (Bash tool) kullanarak `git diff --cached` komutunun çıktısının boş olup olmadığını kontrol et.
2. Eğer staged (sahneye eklenmiş) değişiklik yoksa, kullanıcıya kibarca şunları söyle:
   "Lütfen değişikliklerinizi önce `git add <dosya>` ile ekleyin, ardından tekrar deneyin."
3. Eğer sahneye eklenmiş değişiklikler varsa, terminal üzerinde doğrudan küresel olarak kurulu olan `docuhook` komutunu çalıştır.
4. `docuhook` komutunun terminale bastığı çıktıları takip et ve terminal etkileşimi (Prompt onay süreci) üzerinden kullanıcının onay vermesini (y/N) bekle.
