# NIGGANG — Contexto del Proyecto

## El Equipo
Equipo competitivo de League of Legends en servidor **LAN**.
Sitio web: **https://zsxolars01.github.io**
Repo: **https://github.com/zSxolars01/zsxolars01.github.io**

---

## Roster Titular (6 jugadores)

| Rol | Jugador | Rank | OP.GG |
|---|---|---|---|
| Top | Risardo | Diamond 4 83 LP | op.gg/summoners/lan/Risardo-LAN |
| Jungle | hwidban | Master 517 LP | op.gg/summoners/lan/Checo-Jgler |
| Mid | T1Tocino | Platinum 4 13 LP | op.gg/summoners/lan/T1 Ťocino-God |
| AD Carry | DizzyL | Diamond 4 3 LP | op.gg/summoners/lan/DizzyL-nlgan |
| Support | PykeTyson | Emerald 4 99 LP | op.gg/summoners/lan/Pyke Tyson-1389 |
| Support Suplente | zSxolars | Platinum 4 92 LP | op.gg/summoners/lan/zSxolars-MTLSA |

## Academia (4 jugadores)

| Rol | Jugador | Rank | OP.GG |
|---|---|---|---|
| Top | juanYF | Platinum 2 43 LP | op.gg/summoners/lan/crybaby-616SS |
| Top | stately | Emerald 4 42 LP | op.gg/summoners/lan/stately-LAN |
| AD Carry | DjChurches | Gold 3 14 LP | op.gg/summoners/lan/DjChurches-nigan |
| Support | Cangreburgito | Unranked | op.gg/summoners/lan/Cangreburgito69-6969 |

---

## Picks Principales (desde OP.GG, temporada 2026)

**Risardo (Top):** Hecarim 86%, Zyra 68%, Udyr 64%, Hwei 42%
**hwidban (Jungle):** Evelynn 55% (190g), Naafiri 54% (56g), Ekko 50% (40g), Graves 50% (24g)
**T1Tocino (Mid):** Azir 80%, Qiyana 67%, Orianna 60%, Zoe 50% (26g)
**DizzyL (AD Carry):** Jhin 62% (95g), Yunara 57% (37g), Aphelios 56% (41g), Draven 56% (18g)
**PykeTyson (Support):** Braum 86% (7g), Senna 67% (6g), Leona 58% (19g), Pyke 58% (26g)
**zSxolars (Support Suplente):** Nautilus 73% (11g), Braum 50% (6g), Veigar 52% (21g), Thresh 33% (3g)
**juanYF (Jungle):** Viego 60% (5g), Kayn 100% (1g), Shaco 100% (1g), Kha'Zix 0% (2g)
**stately (Top):** Veigar 67% (12g), Zed 51% (57g), Teemo 100% (3g), Darius 25% (4g)
**DjChurches (AD Carry):** Yunara 59% (41g), Kai'Sa 54% (52g), Jhin 50% (4g), Ashe 36% (11g)
**Cangreburgito (Support):** Pool en desarrollo, Veigar 100% (muestra pequeña)

---

## Iconos de Perfil (CommunityDragon)
Base URL: `https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/{id}.jpg`

| Jugador | Icon ID |
|---|---|
| juanYF | 5915 |
| hwidban | 5287 |
| T1Tocino | 4078 |
| DizzyL | 6638 |
| PykeTyson | 4065 |
| zSxolars | 744 |
| stately | 7120 |
| Risardo | 907 |
| DjChurches | 7123 |
| Cangreburgito | 6584 |

---

## Stack Técnico

- **Sitio:** Single-file HTML/CSS/JS en `index.html`
- **Hosting:** GitHub Pages desde rama `main`
- **Fuentes:** Orbitron (títulos) + Rajdhani (body) — Google Fonts
- **Íconos campeones:** DDragon CDN con patch dinámico (fetch versions.json)
- **Íconos perfil:** CommunityDragon `/latest/`
- **Ranks:** `ranks.json` actualizado por GitHub Actions diariamente
- **Riot API Key:** Personal API Key aprobada (guardada SOLO en Cloudflare Worker — nunca commitear)
  - App ID: 844641, Nombre: "LAN COMPETITIVE TEAM NUEVO LEON SAMUEL GARCIA REGIO"
  - No expira cada 24h (Personal Key)

---

## Archivos del Proyecto

| Archivo | Descripción |
|---|---|
| `index.html` | Sitio completo |
| `ranks.json` | Rangos auto-actualizados |
| `fetch_ranks.py` | Script Riot API |
| `.github/workflows/update-ranks.yml` | GitHub Actions (cron 8am UTC diario) |
| `preview.svg` | Imagen OG para SEO (1200x630) |
| `logo-preview.html` | Preview de logos (no usado en sitio) |

---

## Features Implementadas

- Navbar fijo con scroll reveal y link activo por sección
- Hero con canvas particles animado
- About section con banner NIGGANG + stats grid
- Scroll reveal animations (IntersectionObserver)
- Cards de jugadores con hover effects + ripple effect
- Modal con picks, stats, intro, clips de YouTube
- Auto-update de rangos via GitHub Actions + Riot API
- Cursor personalizado (dot instantáneo + ring con lerp 0.38)
- SEO: og:title, og:description, og:image, Twitter Card
- Sección "Reta a NIGGANG" con Discord link
- DDragon patch dinámico (Yunara y nuevos campeones)
- Grid titular: 5 cols fijas, zSxolars en col 5 fila 2 (debajo de PykeTyson)

---

## Excepciones DDragon (champImg)
```js
kaisa→Kaisa, chogath→Chogath, khazix→Khazix, reksai→RekSai,
kogmaw→KogMaw, velkoz→Velkoz, belveth→Belveth, aurelionsol→AurelionSol,
drmundo→DrMundo, jarvaniv→JarvanIV, leesin→LeeSin, masteryi→MasterYi,
missfortune→MissFortune, wukong→MonkeyKing, twistedfate→TwistedFate,
xinzhao→XinZhao, tahmkench→TahmKench
```

---

## Links Importantes

- **Sitio:** https://zsxolars01.github.io
- **Discord:** https://discord.gg/KeCuVugQKc
- **Riot Developer Portal:** developer.riotgames.com/app/844641

---

## Pendiente

- [ ] Cloudflare Worker para actualizar rangos cada 10 min (en progreso)
- [ ] Logo del equipo (el usuario no gustó de los SVG generados, prefiere diseñar en Canva)
- [ ] Redes sociales (Discord, Twitter/X, TikTok) en navbar/footer
- [ ] Versión móvil mejorada
- [ ] Historial de torneos
- [ ] Más clips de jugadores (solo DizzyL y Cangreburgito tienen clips)

---

## Notas del Usuario (preferencias)

- No quiere emojis en el código
- Prefiere nombres completos: "AD Carry" en vez de "ADC"
- No le gustaron los logos SVG generados ("se ven muy IA")
- Quiere fluidez sin lag — backdrop-filter blur eliminado del modal
- cursor: dot instantáneo, ring con lerp rápido (0.38) sin verse laggy
- zSxolars es el dueño del repo (GitHub: zSxolars01)
- juanYF juega Jungle (no Top como estaba originalmente)
- El equipo es de 6: 5 titulares + 1 suplente (zSxolars), no 5+5
