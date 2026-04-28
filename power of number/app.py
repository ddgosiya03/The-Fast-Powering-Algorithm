from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def compute_modular_exp(p, g, s):
    j = s
    blist = []
    plist = []
    steps = []
    while True:
        q = s // 2
        r = s % 2
        blist.append(r)
        steps.append(f"2 | {s} | {r}")
        if q != 0:
            s = q
        else:
            break
    u = 0
    l = ""
    for y in blist:
        c = f"{y}*(2^{u})"
        if l:
            l = f"{l} + {c}"
        else:
            l = c
        u += 1
    equation = f"{j} = {l}"
    d = (g ** (2 ** 0)) % p
    plist.append(d)
    for i in range(len(blist) - 1):
        b = (d * d) % p
        plist.append(b)
        d = b
    m = 0
    n = 1
    while m < len(plist):
        n = ((plist[m] ** blist[m]) * n) % p
        m += 1
    return {
        'steps': steps,
        'equation': equation,
        'plist': plist,
        'result': n
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    p = int(data['p'])
    g = int(data['g'])
    s = int(data['s'])
    result = compute_modular_exp(p, g, s)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
