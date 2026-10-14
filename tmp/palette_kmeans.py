"""Extract a k-color palette from each painting with k-means (k-means++ init, NumPy only)."""
import json, sys
import numpy as np
from PIL import Image

def kmeans(X, k=5, iters=40, seed=7):
    rng = np.random.default_rng(seed)
    C = [X[rng.integers(len(X))]]
    for _ in range(1, k):
        d = np.min(((X[:, None, :] - np.array(C)[None]) ** 2).sum(-1), axis=1)
        C.append(X[rng.choice(len(X), p=d / d.sum())])
    C = np.array(C, dtype=float)
    for _ in range(iters):
        lab = np.argmin(((X[:, None, :] - C[None]) ** 2).sum(-1), axis=1)
        newC = np.array([X[lab == j].mean(0) if np.any(lab == j) else C[j] for j in range(k)])
        if np.allclose(newC, C): break
        C = newC
    counts = np.bincount(lab, minlength=k)
    return C, counts

out = {}
for f in sys.argv[1:]:
    im = Image.open(f).convert('RGB')
    w, h = im.size; m = 0.06  # trim borders / frame edges
    im = im.crop((int(w*m), int(h*m), int(w*(1-m)), int(h*(1-m)))).resize((120, 120))
    X = np.asarray(im, dtype=float).reshape(-1, 3)
    C, counts = kmeans(X)
    order = np.argsort(-counts)
    out[f.split('/')[-1]] = ['#%02x%02x%02x' % tuple(int(round(v)) for v in C[i]) for i in order]
print(json.dumps(out, indent=1))
