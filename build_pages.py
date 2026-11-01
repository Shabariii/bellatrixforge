"""Builds bellatrix/index.html and battles/index.html from the home page's style and scripts."""
STARS = """
// A living sky behind the page: twinkling stars that drift with the scroll, and now and then a comet.
(() => {
  const c = document.getElementById('stars'); if (!c) return;
  const x = c.getContext('2d'); let w, h, stars = [], comets = [];
  const size = () => { w = c.width = innerWidth; h = c.height = innerHeight;
    stars = Array.from({ length: Math.round(w * h / 5000) }, () => ({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.4 + .2, p: Math.random() * 6.28, d: Math.random() * .6 + .1, blue: Math.random() < .3 })); };
  addEventListener('resize', size); size();
  (function tick(tm) {
    requestAnimationFrame(tick);
    if (document.hidden) return;
    x.clearRect(0, 0, w, h);
    const sy = scrollY;
    for (const s of stars) {
      const a = .35 + .65 * Math.abs(Math.sin(s.p + tm / 900 * s.d)), y = ((s.y - sy * s.d * .15) % h + h) % h;
      x.fillStyle = s.blue ? `rgba(140,200,255,${a})` : `rgba(255,244,220,${a})`;
      x.beginPath(); x.arc(s.x, y, s.r, 0, 7); x.fill();
    }
    if (!reduce && comets.length < 2 && Math.random() < .004) comets.push({ x: Math.random() * w * .8, y: Math.random() * h * .4, vx: 6 + Math.random() * 5, vy: 2 + Math.random() * 2.5, life: 1 });
    comets = comets.filter(k => (k.life -= .012) > 0);
    for (const k of comets) {
      k.x += k.vx; k.y += k.vy;
      const g = x.createLinearGradient(k.x, k.y, k.x - k.vx * 22, k.y - k.vy * 22);
      g.addColorStop(0, `rgba(220,240,255,${k.life})`); g.addColorStop(1, 'rgba(108,192,255,0)');
      x.strokeStyle = g; x.lineWidth = 2; x.beginPath(); x.moveTo(k.x, k.y); x.lineTo(k.x - k.vx * 22, k.y - k.vy * 22); x.stroke();
    }
  })(0);
})();
"""
SITE = r'C:\Users\bruno\Claude Code\bellatrix-forge-site'
home = open(SITE + r'\index.html', encoding='utf-8').read()
style = home[home.index('<style>'):home.index('</style>') + 8].replace('url(img/', 'url(../img/')
libs = home[home.index('<script src="https://cdnjs'):home.index('<script>\ngsap.registerPlugin')]
engine = home[home.index('<script>\ngsap.registerPlugin'):home.index('</body>')]
# keep: lenis, progress bar, filmChapter, gallery, embers, reveals. drop: oath, hut, brew, home film calls
for a, b in [('// The oath:', '// Gallery:'), ('// The hut opens', '// Embers drift')]:
    engine = engine[:engine.index(a)] + engine[engine.index(b):]
engine = engine.replace("filmChapter(document.getElementById('top'));", '').replace("filmChapter(document.getElementById('bellatrix'));", '')
engine = engine.replace("// Gallery: vertical scroll slides the screenshots sideways.\nconst track", "// Gallery: vertical scroll slides the screenshots sideways.\nconst track")
engine = engine.replace("const track = document.querySelector('.track');\ngsap.to(track",
                        "const track = document.querySelector('.track');\nif (track) gsap.to(track")
engine = engine.replace('</script>', "document.querySelectorAll('.film').forEach(filmChapter);\n" + STARS + "</script>")


EXTRA = '''<style>
html { background:var(--night); } body.sky { background:transparent; }
#stars { position:fixed; inset:0; width:100%; height:100%; z-index:-1; pointer-events:none; }
.page-sec { padding:12vh clamp(16px,6vw,96px); max-width:1760px; margin:auto; }
.page-sec h2.big { font:900 clamp(36px,5.4vw,92px)/1 "Cinzel Decorative", serif; margin:.3em 0 .5em; }
.steps { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:clamp(18px,2.4vw,40px); counter-reset:s; }
.step { position:relative; padding:28px 26px 26px; border:1px solid #e8b75a33; background:linear-gradient(160deg,#12141b,#0a0b10); }
.step::before { counter-increment:s; content:counter(s, upper-roman); position:absolute; top:-22px; left:22px; font:900 34px "Cinzel Decorative", serif; color:var(--gold); background:var(--night); padding:0 10px; }
.step h3, .feat h3 { font:700 clamp(19px,1.5vw,25px) "Cinzel Decorative", serif; color:var(--gold-hi); margin:6px 0 10px; }
.step p, .feat p { margin:0; color:#c9c0ac; }
.feats { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr)); gap:clamp(18px,2.4vw,40px); }
.feat { border-top:2px solid var(--gold-dk); padding-top:18px; }
.clips { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,560px),1fr)); gap:18px; }
.clips figure { margin:0; border:1px solid #e8b75a44; box-shadow:0 30px 80px #000; }
.clips video { width:100%; display:block; aspect-ratio:16/9; object-fit:cover; }
.clips figcaption { padding:12px 16px; font:600 12px Cinzel, serif; letter-spacing:.3em; text-transform:uppercase; color:var(--dim); }
.road { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr)); gap:0; position:relative; }
.road::before { content:""; position:absolute; left:0; right:0; top:15px; height:2px; background:linear-gradient(90deg,var(--gold),var(--gold-dk) 40%,#333 100%); }
.mile { position:relative; padding:44px 22px 0 0; }
.mile::before { content:""; position:absolute; top:7px; left:0; width:16px; height:16px; transform:rotate(45deg); background:#333; border:2px solid #555; }
.mile.done::before { background:var(--gold); border-color:var(--gold-hi); box-shadow:0 0 18px var(--gold); }
.mile b { display:block; font:700 18px "Cinzel Decorative", serif; color:var(--gold-hi); }
.mile span { font:600 11px Cinzel, serif; letter-spacing:.25em; text-transform:uppercase; color:var(--dim); }
.mile.done span { color:var(--blue); }
.mile p { color:#c9c0ac; margin:.5em 0 0; font-size:15px; }
.two-cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr)); gap:clamp(18px,2.4vw,40px); }
.card { padding:30px; border:1px solid #e8b75a44; background:linear-gradient(160deg,#12141b,#0a0b10); }
.card h3 { font:900 clamp(24px,2vw,34px) "Cinzel Decorative", serif; margin:0 0 6px; }
.card ul { margin:14px 0 0; padding-left:20px; color:#c9c0ac; } .card li { margin:.3em 0; }
.keys { display:flex; flex-wrap:wrap; gap:12px 26px; margin-top:12px; color:#c9c0ac; }
kbd { font:600 13px "IBM Plex Mono", monospace; padding:3px 9px; border:1px solid #e8b75a66; border-bottom-width:3px; border-radius:4px; color:var(--gold-hi); margin-right:6px; }
.hero-art { position:relative; min-height:100vh; display:grid; place-items:end center; overflow:hidden; text-align:center; padding:0 16px 10vh; }
.hero-art .bg { position:absolute; inset:0; background:center top/cover; }
.hero-art .bg::after { content:""; position:absolute; inset:0; background:linear-gradient(0deg,var(--night) 6%,transparent 55%); }
.hero-art .in { position:relative; }
.hero-art .tagline { font:500 clamp(22px,2.4vw,36px)/1.3 "Cormorant Garamond", serif; font-style:italic; color:var(--gold-hi); text-shadow:0 2px 20px #000; margin:0 0 22px; }
.hero-art .btns { justify-content:center; }
</style>
'''


def page(title, desc, og, nav, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Bellatrix Forge Studios</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:image" content="{og}">
<link rel="icon" href="../img/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;800;900&family=Cinzel+Decorative:wght@700;900&family=Cormorant+Garamond:ital,wght@0,500;1,500&family=IBM+Plex+Mono:wght@600&family=Inter:wght@400;500&display=swap" rel="stylesheet">
{style}
{EXTRA}</head>
<body class="sky">
<canvas id="stars" aria-hidden="true"></canvas>
<div class="progress"></div>
<canvas id="embers" aria-hidden="true"></canvas>
<header class="bar">
  <a class="brand" href="../"><img src="../img/icon.png" alt="">Bellatrix Forge</a>
  <nav>{nav}<a href="../">All Games</a></nav>
</header>
{body}
<footer>
  <img src="../img/studio_lockup.webp" alt="Bellatrix Forge Studios">
  <nav><a href="../">The Forge</a><a href="https://pixelforgestudiosgames.itch.io" target="_blank" rel="noopener">itch.io</a><a href="https://www.youtube.com/@PixelForgeStudios-z7y" target="_blank" rel="noopener">YouTube</a></nav>
  <p>&copy; 2026 Bellatrix Forge Studios &middot; Made in Brazil</p>
</footer>
{libs}{engine}</body>
</html>
'''


ITCH_BX = 'https://pixelforgestudiosgames.itch.io/bellatrix'
bx = page('BELLATRIX', 'BELLATRIX, a space-opera bullet heaven. The blue giant of Orion is changing, the fleet has turned, and one pilot launches with ECHO. Free demo in your browser.',
          '../film/title_reveal_end.jpg',
          '<a href="#move">See it move</a><a href="#plays">How it plays</a><a href="#roadmap">Roadmap</a><a href="#demo">Demo</a>', f'''
<section class="film" id="top">
  <video src="../film/title_reveal.mp4" muted playsinline autoplay preload="auto"></video>
  <div class="veil"></div>
  <div class="lines"><p>While she shines, we fly.</p></div>
  <div class="hint">SCROLL</div>
</section>

<div class="chapter" id="story">
  <div class="eyebrow reveal">The star is changing</div>
  <div class="split">
    <div>
      <h2 class="reveal flame">BELLATRIX</h2>
      <p class="lede reveal">Bellatrix, the blue giant of Orion, is in transition. Something in the asteroid belt is corrupting the change, and it has turned our own fleet against us.</p>
    </div>
    <div class="reveal">
      <p>You launch alone. ECHO, the memory of the ancients, speaks in your ear through every climb.</p>
      <p>A space-opera bullet heaven: fly a fighter with real momentum, build your hull one module at a time, and break the fortress that closes every level.</p>
      <div class="btns"><a class="btn" href="{ITCH_BX}" target="_blank" rel="noopener">Play the free demo</a><span class="btn ghost">Steam: coming</span></div>
    </div>
  </div>
</div>

<section class="page-sec" id="move">
  <div class="eyebrow reveal">Real footage from the demo</div>
  <h2 class="big reveal flame">See it move</h2>
  <div class="clips">
    <figure class="reveal"><video src="../film/the_bastion_ring.mp4" muted playsinline loop autoplay preload="metadata"></video><figcaption>The Bastion turns a station of our own fleet around</figcaption></figure>
    <figure class="reveal"><video src="../film/the_armory_lasers.mp4" muted playsinline loop autoplay preload="metadata"></video><figcaption>The Armory sweeps the arena with lasers</figcaption></figure>
  </div>
</section>

<section class="page-sec" id="plays">
  <div class="eyebrow reveal">Three verbs</div>
  <h2 class="big reveal flame">How it plays</h2>
  <div class="steps">
    <div class="step reveal"><h3>Move</h3><p>Your fighter has real momentum. Drift, turn, and cut through the swarm with an offensive dash. Your hull weapons do the shooting; your hands do the surviving.</p></div>
    <div class="step reveal"><h3>Choose</h3><p>Every level-up offers a hull module, a passive or a skill. Each card shows the numbers before and after, so you always know what your build is doing.</p></div>
    <div class="step reveal"><h3>Break the Fortress</h3><p>No boss, no clear. Every level ends against a named fortress with phases and telegraphed laser sweeps. Move, survive, then hit the exposed core.</p></div>
  </div>
</section>

<section class="rail" aria-label="BELLATRIX screenshots">
  <div class="track">
    <figure><img loading="lazy" src="../img/bx_01_swarm.webp" alt=""><figcaption>The swarm</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_05_level_up_cards.webp" alt=""><figcaption>Choose your module</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_02_boss_the_bastion.webp" alt=""><figcaption>The Bastion</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_08_warp_corridor.webp" alt=""><figcaption>The warp</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_03_boss_the_armory.webp" alt=""><figcaption>The Armory</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_06_campaign_map.webp" alt=""><figcaption>The campaign</figcaption></figure>
    <figure><img loading="lazy" src="../img/bx_11_starforge.webp" alt=""><figcaption>The Starforge</figcaption></figure>
  </div>
</section>

<section class="page-sec" id="hangar">
  <div class="eyebrow reveal">What waits in the hangar</div>
  <h2 class="big reveal flame">The Wake</h2>
  <div class="feats">
    <div class="feat reveal"><h3>Splash and Chain</h3><p>Flak that airbursts, lightning that jumps from hull to hull, plasma that burns. Weapons are modules mounted on your ship, and they evolve as you level.</p></div>
    <div class="feat reveal"><h3>Named Fortresses</h3><p>THE BASTION, THE ARMORY, AEGIS REVENANT. Our own stations and our own flagship, still wearing our crest.</p></div>
    <div class="feat reveal"><h3>The Starforge</h3><p>Between runs, stardust lights the stars of a growing constellation, unlocking weapons, passives and skills for the next launch.</p></div>
    <div class="feat reveal"><h3>ECHO</h3><p>Your guardian intelligence and the memory of the ancients. She talks you through the campaign, one line at a time, and never cuts herself off.</p></div>
    <div class="feat reveal"><h3>Mission Control</h3><p>Station, campaign map, hangar, Starforge and records. Register your callsign, feel the dock ignite, and warp into the sector.</p></div>
    <div class="feat reveal"><h3>Your Way to Play</h3><p>Keyboard or gamepad. EASY and NORMAL in the demo. Built to run in a browser on an ordinary laptop.</p></div>
  </div>
</section>

<section class="page-sec" id="roadmap">
  <div class="eyebrow reveal">Where the flight goes</div>
  <h2 class="big reveal flame">Roadmap</h2>
  <div class="road">
    <div class="mile done reveal"><span>Now</span><b>Free demo</b><p>Playable in your browser on itch.io: the first zone and its three fortresses.</p></div>
    <div class="mile reveal"><span>To be confirmed</span><b>Early Access</b><p>BELLATRIX on Steam while the campaign grows: new zones, weapons and fortresses as they are forged.</p></div>
    <div class="mile reveal"><span>To be confirmed</span><b>Launch</b><p>The full campaign across three corrupted zones, Endless mode and HARD difficulty.</p></div>
  </div>
</section>

<section class="page-sec" id="demo">
  <div class="eyebrow reveal">Demo and full game</div>
  <h2 class="big reveal flame">Launch Now</h2>
  <div class="two-cards">
    <div class="card reveal"><h3 class="flame">Free Demo</h3><p>In your browser, no install.</p>
      <ul><li>The first zone of the Wake</li><li>Three fortress bosses: THE BASTION, THE ARMORY, AEGIS REVENANT</li><li>EASY and NORMAL</li><li>Keyboard or gamepad</li></ul>
      <div class="btns"><a class="btn" href="{ITCH_BX}" target="_blank" rel="noopener">Play in your browser</a></div></div>
    <div class="card reveal"><h3 class="flame">Full Game</h3><p>Coming to Steam for Windows. Release date to be confirmed.</p>
      <ul><li>The zones beyond the Wake</li><li>Endless mode</li><li>HARD difficulty</li><li>The rest of ECHO's story</li></ul>
      <div class="btns"><span class="btn ghost">Wishlist: soon</span></div></div>
  </div>
  <div class="keys reveal"><span><kbd>WASD</kbd>Fly</span><span><kbd>Shift</kbd>Dash</span><span><kbd>Esc</kbd>Pause</span><span>Gamepad supported</span></div>
</section>
''')

ITCH_BB = 'https://pixelforgestudiosgames.itch.io/bellatrix-battles'
bb = page('Bellatrix Battles', 'Bellatrix Battles: build your clan, equip your fighters and face the arenas of Vesper in a sci-fi tactical arena. Early demo in your browser.',
          '../img/bb_cover.webp',
          '<a href="#home">Home base</a><a href="#fight">How it fights</a><a href="#modes">Modes</a><a href="#play">Play</a>', f'''
<section class="hero-art" id="top">
  <div class="bg" style="background-image:url(../img/bb_cover.webp)"></div>
  <div class="in">
    <p class="tagline">Build your clan. Earn your legacy. The arenas of Vesper await.</p>
    <div class="btns"><a class="btn" href="{ITCH_BB}" target="_blank" rel="noopener">Play the early demo</a></div>
  </div>
</section>

<div class="chapter" id="home">
  <div class="eyebrow reveal">Single player &middot; Tactical arena &middot; Sci-fi</div>
  <div class="split">
    <div>
      <h2 class="reveal flame">Bellatrix Battles</h2>
      <p class="lede reveal">Your next fight starts at home. Recruit a crew, shape their strengths, and lead them into battle.</p>
    </div>
    <div class="reveal">
      <p>Wayfarer is your foothold on Vesper. Begin with a founder, meet new allies, and build a clan worth fighting for. Between battles, return to base to equip, train and prepare your next formation.</p>
      <p>ECHO, your guardian intelligence, will guide the way.</p>
    </div>
  </div>
</div>

<section class="page-sec" id="fight">
  <div class="eyebrow reveal">Recruit. Prepare. Fight. Grow.</div>
  <h2 class="big reveal flame">How it fights</h2>
  <div class="steps">
    <div class="step reveal"><h3>Build Your Crew</h3><p>Discover new heroes as your campaign unfolds. Give your clan a name and make its story your own.</p></div>
    <div class="step reveal"><h3>Make Every Loadout Count</h3><p>Combine equipment, formations and companion drones before you enter the arena.</p></div>
    <div class="step reveal"><h3>Take the Lead</h3><p>Watch your squad fight on its own, or take control of your captain and use their abilities yourself.</p></div>
    <div class="step reveal"><h3>Face the Unexpected</h3><p>Pirates, creatures, hostile machines and a boss. Return stronger for the next encounter.</p></div>
  </div>
</section>

<section class="page-sec" id="modes">
  <div class="eyebrow reveal">Two ways into the arena</div>
  <h2 class="big reveal flame">Modes</h2>
  <div class="two-cards">
    <div class="card reveal"><h3 class="flame">Campaign</h3><p>A guided beginning, a growing roster, and a path toward the Circuit.</p></div>
    <div class="card reveal"><h3 class="flame">Free Battle</h3><p>A separate practice mode to experiment with your team and your tactics.</p></div>
  </div>
  <div class="keys reveal"><span>Difficulty: Easy &middot; Normal &middot; Hard</span><span><kbd>WASD</kbd>Move</span><span><kbd>Space</kbd>Attack</span><span><kbd>E</kbd>Ability</span><span><kbd>P</kbd>Pause</span></div>
</section>

<section class="page-sec" id="play">
  <div class="eyebrow reveal">Early demo &middot; v0.1a.2</div>
  <h2 class="big reveal flame">Enter the Arena</h2>
  <div class="two-cards">
    <div class="card reveal"><h3 class="flame">Play Now</h3><p>In your browser, best fullscreen on desktop with mouse and keyboard. Six local save slots keep your progress.</p>
      <div class="btns"><a class="btn" href="{ITCH_BB}" target="_blank" rel="noopener">Play the early demo</a></div></div>
    <div class="card reveal"><h3 class="flame">Release</h3><p>Still on the anvil. Release date to be confirmed.</p><div class="stamp">To Be Confirmed</div></div>
  </div>
</section>
''')
import os
os.makedirs(SITE + r'\battles', exist_ok=True)
open(SITE + r'\bellatrix\index.html', 'w', encoding='utf-8').write(bx)
open(SITE + r'\battles\index.html', 'w', encoding='utf-8').write(bb)
print('built')
