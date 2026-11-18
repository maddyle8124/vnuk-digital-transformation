import fitz, re, json, sys
md = open("report_v4.md", encoding="utf-8").read()
heads = [t for _, t in re.findall(r"^(#{1,3}) (.*)$", md, flags=re.M)]
d = fitz.open(sys.argv[1])
texts = [re.sub(r"\s+", " ", p.get_text()) for p in d]
def pnum(i):
    m = re.search(r"PAGE (\d+)", texts[i]); return int(m.group(1)) if m else i + 1
# body starts at the page with "CHAPTER 1. EXECUTIVE SUMMARY" as heading after the lists
start = max(i for i, t in enumerate(texts) if "LIST OF TABLES" in t) + 1
out = {}
cur = start
for h in heads:
    key = re.sub(r"\s+", " ", h)
    for i in range(cur, len(texts)):
        if key in texts[i]:
            out[h] = pnum(i); cur = i; break
    else:
        print("missing", h)
tc = re.findall(r"^TABLE\[\w+\]: (.*)$", md, flags=re.M)
fc = [c.split("|")[1].strip() for c in re.findall(r"^FIG\[\w+\]: (.*)$", md, flags=re.M)]
for kind, caps in (("Figure", fc), ("Table", tc)):
    for n, c in enumerate(caps, 1):
        pat = f"{kind} {n}. " + re.sub(r"\s+", " ", c)[:18]
        hit = [i for i in range(start, len(texts)) if pat in texts[i]]
        if hit: out[f"{kind} {n}"] = pnum(hit[0])
        else: print("missing", pat)
json.dump(out, open("pages.json", "w"), ensure_ascii=False, indent=0)
print(len(out), "entries; front matter ends at page", pnum(start - 1))
