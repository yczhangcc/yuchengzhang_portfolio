p='css/styles.css'; s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    n=s.count(a); assert n==1,(n,a[:80]); s=s.replace(a,b)
rep('''  --teal: #1f766d;
  --blue: #2f5f8f;
  --clay: #a85f42;
  --gold: #b18434;''','''  /* Palette pulled from my own paintings (k-means, see tmp/palette_kmeans.py):
     sunflower ochre (Monet study), haystack sienna, deep stem green. */
  --accent: #8a5418;
  --sienna: #975239;
  --sunflower: #cea81f;
  --stem: #2d4038;''')
rep('color: var(--blue);','color: var(--accent);')
rep('''  border-color: var(--teal);
  background: var(--teal);''','''  border-color: var(--accent);
  background: var(--accent);''')
rep('border-left: 2px solid var(--teal);','border-left: 2px solid var(--sunflower);')
rep('''li::marker {
  color: var(--teal);''','''li::marker {
  color: var(--sunflower);''')
assert '--teal' not in s and '--blue' not in s
rep('''.work-card.featured .meta,
.work-card.featured h3,
.work-card.featured p,
.work-card.featured a {
  grid-column: 1;
}

.work-card.featured ul {
  grid-column: 2;
  grid-row: 2 / span 3;
  margin-top: 0;
}''',open('tmp/css_flow.css').read().rstrip('\n'))
rep('''  .work-card.featured .meta,
  .work-card.featured h3,
  .work-card.featured p,
  .work-card.featured a,
  .work-card.featured ul {
    grid-column: auto;
    grid-row: auto;
  }''','''  .work-card.featured .meta,
  .work-card.featured h3,
  .work-card.featured .question,
  .work-card.featured > a,
  .work-card.featured .flow {
    grid-column: auto;
    grid-row: auto;
  }

  .work-card.featured > a {
    margin-top: 18px;
  }

  .flow.compact {
    grid-template-columns: 1fr;
    gap: 12px;
  }''')
rep('''.more-item {
  display: grid;
  grid-template-columns: minmax(200px, 0.34fr) minmax(0, 1fr);
  gap: 24px;
  align-items: baseline;
  padding: 20px 0;''','''.more-item {
  display: grid;
  grid-template-columns: minmax(200px, 0.34fr) minmax(0, 1fr);
  gap: 32px;
  align-items: start;
  padding: 28px 0;''')
rep('''.contact-section {
  padding-bottom: 64px;
}''','''.contact-section {
  padding-bottom: 72px;
  text-align: center;
}

.contact-section h2 {
  max-width: 720px;
  margin-left: auto;
  margin-right: auto;
}

.contact-email {
  display: inline-block;
  font-family: var(--font-display);
  font-style: italic;
  font-size: clamp(1.2rem, 2.4vw, 1.6rem);
  border-bottom: 1px solid var(--sunflower);
}

.contact-email:hover {
  text-decoration: none;
  border-bottom-color: var(--sienna);
}''')
rep('''.hero-actions,
.resume-grid,
.contact-section p:last-child {''','''.hero-actions,
.resume-grid {''')
rep('''.contact-section p {
  margin-bottom: 12px;
}

.contact-section p:last-child a {
  padding-right: 16px;
  font-weight: 600;
}''','')
rep('/* Lightbox */',open('tmp/css_art.css').read().rstrip('\n')+'\n\n/* Lightbox */')
rep('''.lightbox img {
  max-width: 100%;
  max-height: 88vh;''',open('tmp/css_lb.css').read().rstrip('\n')+'''

.lightbox img {
  max-width: 100%;
  max-height: 70vh;''')
rep('''  .profile-pic {
    width: 112px;
    height: 112px;
  }''','''  .profile-pic {
    width: 112px;
    height: 112px;
  }

  .hero-actions {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
  }

  .hero-actions .button.primary {
    grid-column: 1 / -1;
    order: -1;
  }''')
open(p,'w',encoding='utf-8',newline='').write(s)
print('ok')
