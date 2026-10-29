#!/usr/bin/env python3
"""Render the source-coded benchmark. Does not change the protocol or measurements."""
from pathlib import Path
import base64, csv, hashlib, html, json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
def esc(x):return html.escape(str(x))

def table(headers, rows):
    return '<div class="table-wrap"><table><thead><tr>'+''.join('<th>'+esc(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'

def main():
    m=json.loads((ROOT/'results/metrics.json').read_text())
    profiles=json.loads((ROOT/'comparisons.json').read_text())['profiles']
    refs=json.loads((ROOT/'source_manifest.json').read_text())['references']
    assert len(profiles)==16 and len({p['id'] for p in profiles})==16
    refids={r['id'] for r in refs}
    assert all(set(p['sources'])<=refids for p in profiles)
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'text.color':'#24364b','axes.labelcolor':'#24364b'})
    fig,(a,b)=plt.subplots(1,2,figsize=(12,5.4),gridspec_kw={'width_ratios':[1.4,1]})
    labels=['Structural encoding','Analytic model','Partial specialization','Open']
    vals=[m['frozen_review_counts'][k] for k in ['structural_encoding','analytic_model','partial_specialization','open']]
    a.barh(labels,vals,color=['#6d8495','#008675','#be934c','#9ca3af']);a.invert_yaxis();a.set_xlim(0,61)
    for y,v in enumerate(vals):a.text(v+.7,y,str(v),va='center',fontweight='bold')
    a.set_xlabel('Catalogue entries (total 102)');a.set_title('A  |  Frozen review categories',loc='left',fontweight='bold',pad=16)
    forms=m['representation_control']['forms'];v=[forms[x]['ast_nodes'] for x in ['rational_memory','expanded_Maxwell']]
    bars=b.bar(['Rational form','Expanded form'],v,width=.55,color=['#008675','#be934c'])
    for rect,number in zip(bars,v):b.text(rect.get_x()+rect.get_width()/2,number+2,str(number),ha='center',fontweight='bold')
    b.set_ylim(0,112);b.set_ylabel('Python AST nodes');b.set_title('B  |  Same model, different length',loc='left',fontweight='bold',pad=16)
    b.text(.5,.94,'Equivalent response at 3,003 test points',transform=b.transAxes,ha='center',va='top',fontsize=9)
    a.grid(axis='x',alpha=.12);a.set_axisbelow(True);b.grid(axis='y',alpha=.12);b.set_axisbelow(True)
    fig.suptitle('EFMW-CX-001  •  Corpus structure and representation sensitivity',fontsize=17,fontweight='bold',y=.98)
    fig.text(.5,.025,'Categories describe a formalization snapshot. Syntax size describes a representation. Neither measures physical truth.',ha='center',fontsize=10)
    fig.tight_layout(rect=[0,.075,1,.89],w_pad=3)
    fig.savefig(ROOT/'results/benchmark.png',dpi=180)
    fig.savefig(ROOT/'results/benchmark.svg')
    plt.close(fig)
    metricrows=[['Canonical records / unique IDs','102 / 102'],['Formula Unicode code points',f"{m['total_formula_codepoints']:,}"],['Formula UTF-8 bytes',f"{m['total_formula_utf8_bytes']:,}"],['Lexical tokens / median per record',f"{m['total_lexical_tokens']:,} / {m['median_lexical_tokens']}"],['Token range per record',f"{m['token_min']}–{m['token_max']}"],['Exact / normalized duplicate groups','0 / 0'],['Source classification strings','67'],['Independent physical-law count','NOT ESTABLISHED'],['Whole-theory independent-parameter count','NOT ESTABLISHED']]
    controlrows=[[esc(name.replace('_',' ')),x['codepoints'],x['tokens'],x['ast_nodes']] for name,x in forms.items()]
    matrix=[];details=[]
    for p in profiles:
        cites=' '.join(f'<a href="#ref-{esc(s)}">[{esc(s)}]</a>' for s in p['sources'])
        matrix.append([f'<a href="#profile-{p["id"]}">{esc(p["name"])}</a>',esc(p['primitives']),esc(p['machinery']),esc(p['choices'])])
        fields=[('Selected formulation','variant'),('Primitive carriers','primitives'),('Dynamics and constraints','machinery'),('Independent choices','choices'),('Predictive closure','closure'),('Scope','scope'),('Calculation burden','computation'),('Comparison with EFMW','comparison')]
        details.append(f'<details id="profile-{p["id"]}" open><summary>{esc(p["name"])}</summary><dl>'+''.join('<dt>'+label+'</dt><dd>'+esc(p[key])+'</dd>' for label,key in fields)+'</dl><p class="sources">'+cites+'</p></details>')
    replacements={
      '{{METRICS_TABLE}}':table(['Metric','Recorded value'],metricrows),
      '{{CONTROL_TABLE}}':table(['Equivalent expression','Characters','Lexical tokens','AST nodes'],controlrows),
      '{{FIGURE}}':'<img alt="Frozen review category counts and unequal syntax sizes of mathematically equivalent formulas" src="data:image/png;base64,'+base64.b64encode((ROOT/'results/benchmark.png').read_bytes()).decode()+'">',
      '{{COMPARISON_TABLE}}':table(['Framework','Primitive carriers','Mathematical machinery','Independent choices'],matrix),
      '{{PROFILE_DETAILS}}':'\n'.join(details)
    }
    narrative=(ROOT/'narrative.html').read_text()
    for token,value in replacements.items():narrative=narrative.replace(token,value)
    assert '{{' not in narrative
    references='<section id="references"><h2>Sources and provenance</h2><p>Accessed 29 October 2026. Literature sources define selected formulations; their historical predictions are not adopted as present empirical facts. The EFMW source files are included with exact Git blob verification.</p><ol>'+''.join('<li id="ref-'+esc(r['id'])+'"><strong>'+esc(r['id'])+'</strong> — <a href="'+esc(r['url'])+'">'+esc(r['title'])+'</a>. '+esc(r['locator'])+(' <a href="'+esc(r['supplement'])+'">Companion text</a>.' if 'supplement' in r else '')+'</li>' for r in refs)+'</ol></section>'
    provenance='<section><h2>Reproduction</h2><p>Run <code>python analyze.py</code>, then <code>python render_report.py</code> in the accompanying package. The audit uses the standard library; rendering uses NumPy 2.3.5 and Matplotlib 3.10.8. All 102 per-entry measurements, coded profiles and source hashes are included.</p><p>Protocol SHA256:</p><pre>'+esc(m['protocol_sha256'])+'</pre><p><strong>Prepared for Matthew Chenoweth Wright / Monolithic LLC.</strong> AI-assisted research and coding by Codex. This is an exploratory comparative report, not peer-reviewed research, an empirical validation of EFMW, or an exhaustive literature census.</p></section>'
    style='''*{box-sizing:border-box}body{margin:0;background:#f4f5f4;color:#223445;font:17px/1.62 system-ui,-apple-system,sans-serif}main{max-width:1180px;margin:auto;padding:44px 36px 70px;background:#fff}header{border-bottom:3px solid #008675;padding-bottom:30px;margin-bottom:32px}.eyebrow{color:#008675;font-weight:750;letter-spacing:.1em;font-size:13px}h1{font-size:40px;line-height:1.15;max-width:950px;margin:15px 0}h2{font-size:27px;margin-top:44px;line-height:1.25}h3{font-size:21px}p{max-width:950px}a{color:#006f63}nav{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:25px;font-size:14px}.lead{font-size:21px}.badge{display:inline-block;background:#eaf5f1;padding:6px 12px;border-radius:4px;font-size:14px}.table-wrap{overflow-x:auto;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.5}th{background:#edf4f2;color:#24364b;text-align:left}th,td{padding:12px;vertical-align:top;border-bottom:1px solid #dce4e1}#comparison table{min-width:850px}#comparison td:first-child{min-width:150px;font-weight:650}figure{margin:30px 0}img{width:100%;height:auto}figcaption{font-size:13px;color:#536575}details{border:1px solid #d5e0dc;border-radius:7px;margin:18px 0;padding:16px 20px}summary{font-size:20px;font-weight:700;cursor:pointer}dl{display:grid;grid-template-columns:185px 1fr;gap:8px 18px;font-size:15px}dt{font-weight:650}dd{margin:0}.sources{font-size:13px}.equation,pre{background:#f1f5f3;padding:16px;overflow-wrap:anywhere;white-space:pre-wrap;font:15px/1.6 ui-monospace,monospace}.equation{text-align:center;font-size:18px}code{font-size:.85em;overflow-wrap:anywhere}li{margin:12px 0;font-size:14px}footer{font-size:13px;color:#536575;border-top:1px solid #ccd8d3;padding-top:20px;margin-top:35px}@media(max-width:650px){main{padding:24px 18px}h1{font-size:30px}h2{font-size:23px}dl{grid-template-columns:1fr;gap:4px}dd{margin-bottom:10px}}@media print{body{background:white}main{max-width:none;padding:0;font-size:10pt}h1{font-size:25pt}h2{font-size:17pt;break-after:avoid}h3,summary{break-after:avoid}nav{display:none}details{break-inside:avoid}table{font-size:8pt}#comparison table{min-width:0}a{color:inherit}figure{break-inside:avoid}summary{list-style:none}}'''
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EFMW-CX-001 — Complexity benchmark</title><style>'+style+'</style></head><body><main><header><div class="eyebrow">MONOLITHIC RESEARCH · EFMW-CX-001 · 29 OCTOBER 2026</div><h1>How complex is EFMW compared with other physical frameworks?</h1><p class="lead">An executed corpus audit and a sixteen-framework literature comparison.</p><span class="badge">Exploratory benchmark · no universal ranking</span><nav><a href="#finding">Finding</a><a href="#methods">Method</a><a href="#corpus">Measurements</a><a href="#comparison">16-framework comparison</a><a href="#graph">Dependency audit</a><a href="#references">Sources</a></nav></header>'+narrative+references+provenance+'<footer>Complexity, predictive completeness, novelty and physical truth are separate claims. This report preserves that separation.</footer></main></body></html>'
    (ROOT/'report.html').write_text(page)
    with (ROOT/'results/comparison_profiles.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(profiles[0]));w.writeheader();w.writerows([{**p,'sources':';'.join(p['sources'])} for p in profiles])
    print(json.dumps({'profiles':len(profiles),'references':len(refs),'report_bytes':len(page.encode()),'matplotlib':matplotlib.__version__,'numpy':np.__version__}))

if __name__=='__main__':main()
