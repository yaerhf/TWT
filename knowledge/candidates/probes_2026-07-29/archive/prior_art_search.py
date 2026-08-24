# Prior-art search: metric perturbations sourced by a soliton's INTERNAL rotation;
# spinning gravitating skyrmions; rotating boson stars; gravitomagnetic sector of solitons.
# READ-ONLY probe (network queries only). 2026-07-29 cross-class ontology review.
import json, urllib.request, urllib.parse, time, sys

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "TWT-review-probe/1.0 (mailto:hfyaer@gmail.com)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def inspire(q, size=5):
    url = ("https://inspirehep.net/api/literature?sort=mostrecent&size=%d&q=%s"
           "&fields=titles,dois,arxiv_eprints,earliest_date,citation_count" % (size, urllib.parse.quote(q)))
    try:
        d = get(url)
    except Exception as ex:
        print("  INSPIRE ERROR:", ex); return
    hits = d.get("hits", {}).get("hits", [])
    tot = d.get("hits", {}).get("total", 0)
    print("  total hits: %s" % tot)
    for h in hits:
        m = h["metadata"]
        t = m.get("titles", [{}])[0].get("title", "?")
        doi = (m.get("dois") or [{}])[0].get("value", "-")
        arx = (m.get("arxiv_eprints") or [{}])[0].get("value", "-")
        yr = m.get("earliest_date", "?")[:4]
        cc = m.get("citation_count", "?")
        print("  [%s] (%s cites) %s | doi:%s arxiv:%s" % (yr, cc, t[:110], doi, arx))

def inspire_cited(q, size=5):
    url = ("https://inspirehep.net/api/literature?sort=mostcited&size=%d&q=%s"
           "&fields=titles,dois,arxiv_eprints,earliest_date,citation_count" % (size, urllib.parse.quote(q)))
    try:
        d = get(url)
    except Exception as ex:
        print("  INSPIRE ERROR:", ex); return
    hits = d.get("hits", {}).get("hits", [])
    tot = d.get("hits", {}).get("total", 0)
    print("  total hits: %s" % tot)
    for h in hits:
        m = h["metadata"]
        t = m.get("titles", [{}])[0].get("title", "?")
        doi = (m.get("dois") or [{}])[0].get("value", "-")
        arx = (m.get("arxiv_eprints") or [{}])[0].get("value", "-")
        yr = m.get("earliest_date", "?")[:4]
        cc = m.get("citation_count", "?")
        print("  [%s] (%s cites) %s | doi:%s arxiv:%s" % (yr, cc, t[:110], doi, arx))

def crossref(q, rows=4):
    url = ("https://api.crossref.org/works?rows=%d&query.bibliographic=%s"
           "&select=title,DOI,issued,container-title" % (rows, urllib.parse.quote(q)))
    try:
        d = get(url)
    except Exception as ex:
        print("  CROSSREF ERROR:", ex); return
    for it in d.get("message", {}).get("items", []):
        t = (it.get("title") or ["?"])[0]
        doi = it.get("DOI", "-")
        yr = (it.get("issued", {}).get("date-parts") or [["?"]])[0][0]
        jn = (it.get("container-title") or ["-"])[0]
        print("  [%s] %s | %s | doi:%s" % (yr, t[:110], jn[:40], doi))

QUERIES_INSPIRE_CITED = [
    't "spinning gravitating skyrmions"',
    't skyrmion and t rotating and t gravitating',
    't "rotating boson stars"',
    't boson star and t "frame dragging"',
    't isospinning skyrmions',
    't skyrmion and t "angular momentum"',
    'a heusler and t rotating and t soliton',
    't "slowly rotating" and t skyrmion',
]
QUERIES_INSPIRE_RECENT = [
    't gravitomagnetic and t soliton',
    't "internal rotation" and t "metric perturbation"',
    'abstract "momentum density" and abstract "zero energy density" and abstract gravitomagnetic',
]
QUERIES_CROSSREF = [
    "spinning gravitating skyrmions",
    "rotating boson stars quantized angular momentum",
    "Kaup Klein-Gordon geon",
    "Ruffini Bonazzola systems of self-gravitating particles",
    "slowly rotating boson stars Kobayashi Kasai Futamase",
]

for q in QUERIES_INSPIRE_CITED:
    print("\n=== INSPIRE (mostcited): %s ===" % q); inspire_cited(q); time.sleep(1)
for q in QUERIES_INSPIRE_RECENT:
    print("\n=== INSPIRE (recent): %s ===" % q); inspire(q); time.sleep(1)
for q in QUERIES_CROSSREF:
    print("\n=== CROSSREF: %s ===" % q); crossref(q); time.sleep(1)
print("\nDONE")
