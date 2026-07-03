# DocuHook 🪝

Yapay zeka tabanlı otomatik git pre-commit dokümantasyon güncelleyici.

## Nasıl Çalışır?

Siz kod yazıp `git commit` komutunu verdiğinizde **DocuHook** arka planda otomatik olarak tetiklenir:
1. Sahneye eklediğiniz değişiklikleri (`git diff`) analiz eder.
2. README.md dosyasını otomatik olarak günceller ve commite ekler.

## Kurulum

1. Paketi yerel olarak kurun:
   ```bash
   pip3 install .
   ```

2. OpenRouter API anahtarınızı tanımlayın (Sadece bir kez yapmanız yeterlidir):
   ```bash
   docuhook --configure
   ```

## Kullanım

Herhangi bir Git projenizin klasörüne gidin ve şu komutla kancayı aktif edin:
```bash
docuhook --install
```
