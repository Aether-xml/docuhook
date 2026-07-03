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

## Claude Code & OpenCode CLI Entegrasyonu (Skill)

Bu proje, Claude Code ve OpenCode CLI gibi otonom yapay zeka araçlarıyla doğrudan uyumlu yerleşik bir **Agent Skill** (`SKILL.md`) içerir.

Yapay zeka ajanı üzerinden doğrudan `/docuhook` komutunu kullanabilmek için aşağıdaki komutlarla kurulumu tamamlayabilirsiniz:

```bash
mkdir -p ~/.claude/skills/docuhook
cp .claude/skills/docuhook/SKILL.md ~/.claude/skills/docuhook/SKILL.md
```

Artık Claude veya OpenCode arayüzünde sadece `/docuhook` yazarak akıllı güncellemeyi başlatabilirsiniz.
