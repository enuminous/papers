#!/usr/bin/env python3
"""EFMW-CX-001: deterministic artifact metrics, not intrinsic theory complexity."""
from pathlib import Path
from collections import Counter, defaultdict
import ast, csv, hashlib, json, math, re, statistics, sys, unicodedata

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)
TOKENIZER = r'\w+|[^\w\s]'
MARKERS = {
    'spatial/covariant/wave derivative symbols': ['∂', '∇', '□'],
    'integral symbol': ['∫'],
    'summation symbol': ['Σ'],
    'norm notation': ['||'],
    'optimization words': ['arg min', 'arg max'],
    'limit notation': ['lim('],
    'explicit xi(t) noise': ['ξ(t)'],
    'tensor-product symbol': ['⊗'],
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def group_duplicates(entries, norm):
    groups=defaultdict(list)
    for e in entries: groups[norm(e['formula'])].append(e['id'])
    return [g for g in groups.values() if len(g)>1]

def scc(graph):
    """Tarjan SCC; diagnostic of declared documentation links only."""
    index=0; indexes={}; low={}; stack=[]; on=set(); result=[]
    def visit(v):
        nonlocal index
        indexes[v]=low[v]=index; index+=1; stack.append(v); on.add(v)
        for w in graph[v]:
            if w not in indexes: visit(w); low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],indexes[w])
        if low[v]==indexes[v]:
            comp=[]
            while True:
                w=stack.pop();on.remove(w);comp.append(w)
                if w==v:break
            result.append(sorted(comp))
    for v in graph:
        if v not in indexes:visit(v)
    return result

def main():
    protocol=json.loads((ROOT/'protocol.json').read_text())
    assert sha(ROOT/'protocol.json')=='5ccfbf169830cec63cb4bbe447f34d1256c1af0a7456bffbe348e66af760440e'
    source=json.loads((ROOT/'sources/canonical_equations.json').read_text())
    coverage=json.loads((ROOT/'sources/frozen_coverage.json').read_text())
    entries=source['equations']; assert len(entries)==source['count']==102
    assert len({e['id'] for e in entries})==102
    assert [e['number'] for e in entries]==list(range(1,103))
    assert source['source_sha256']==coverage['canonical_source_sha256']
    src={e['id']:e for e in entries}
    assert all(e['formula']==src[e['id']]['formula'] for e in coverage['entries'])
    statuses=Counter(e['review_status'] for e in coverage['entries'])
    assert dict(statuses)==coverage['counts']
    metrics=[]
    for e in entries:
        s=e['formula']
        row={'id':e['id'],'title':e['title'],'classification':e['classification'],
             'codepoints':len(s),'utf8_bytes':len(s.encode()),
             'lexical_tokens':len(re.findall(TOKENIZER,s)),
             'physical_law_count':None,
             'review_status':next(x['review_status'] for x in coverage['entries'] if x['id']==e['id'])}
        for name,markers in MARKERS.items():row[name]=int(any(x in s for x in markers))
        metrics.append(row)
    with (OUT/'entry_metrics.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(metrics[0]));w.writeheader();w.writerows(metrics)
    tokens=[x['lexical_tokens'] for x in metrics]
    graph={e['id']:e['dependencies'] for e in coverage['entries']}
    assert all(v in graph for neighbors in graph.values() for v in neighbors)
    cycles=[x for x in scc(graph) if len(x)>1 or x[0] in graph[x[0]]]
    # Two equivalent expressions in different textual representations.
    forms={
      'rational_memory':'-1/(k-m*w*w+1j*b*w+4*G*(1j*w*tau)/(1+1j*w*tau))',
      'expanded_Maxwell':'-1/(k-m*w*w+4*G*(w*tau)**2/(1+(w*tau)**2)+1j*(b*w+4*G*w*tau/(1+(w*tau)**2)))'
    }
    representation={name:{'expression':s,'codepoints':len(s),'tokens':len(re.findall(TOKENIZER,s)),
                          'ast_nodes':len(list(ast.walk(ast.parse(s,mode='eval'))))}
                    for name,s in forms.items()}
    parameters=[(363870.,2.495e-6,.04,10000.,8e-6),(120000.,1e-6,.01,500.,1e-6),(900000.,1e-5,.12,30000.,5e-5)]
    rel=0.; count=0
    for k,m,b,G,tau in parameters:
        for j in range(1001):
            w=2*math.pi*2000*100**(j/1000)
            z=w*tau
            a=-1/(k-m*w*w+1j*b*w+4*G*(1j*z)/(1+1j*z))
            c=-1/(k-m*w*w+4*G*z*z/(1+z*z)+1j*(b*w+4*G*z/(1+z*z)))
            rel=max(rel,abs(a-c)/abs(a));count+=1
    assert rel<1e-12
    result={
      'study_id':'EFMW-CX-001','protocol_sha256':sha(ROOT/'protocol.json'),
      'python':sys.version.split()[0],'entries':len(entries),'unique_ids':len(src),
      'total_formula_codepoints':sum(x['codepoints'] for x in metrics),
      'total_formula_utf8_bytes':sum(x['utf8_bytes'] for x in metrics),
      'total_lexical_tokens':sum(tokens),'median_lexical_tokens':statistics.median(tokens),
      'token_min':min(tokens),'token_max':max(tokens),
      'exact_duplicate_groups':group_duplicates(entries,lambda x:x),
      'normalized_duplicate_groups':group_duplicates(entries,lambda x:re.sub(r'\s+','',unicodedata.normalize('NFC',x))),
      'source_classification_counts':dict(Counter(e['classification'] for e in entries)),
      'source_classification_count':len(set(e['classification'] for e in entries)),
      'source_labels_starting_standard':sum(e['classification'].startswith('standard') for e in entries),
      'source_labels_starting_working':sum(e['classification'].startswith('working') for e in entries),
      'frozen_review_counts':dict(statuses),
      'marker_counts':{name:sum(x[name] for x in metrics) for name in MARKERS},
      'tokenizer':TOKENIZER,'marker_definitions':MARKERS,
      'supplementary_post_inspection_diagnostics':{
         'reason':'ME-102 contains prose; declared dependency cycles were seen during source inspection. These diagnostics were added after the protocol freeze and are not confirmatory.',
         'ME102_tokens':metrics[-1]['lexical_tokens'],'tokens_excluding_ME102':sum(tokens[:-1]),
         'dependency_nodes':len(graph),'dependency_edges':sum(map(len,graph.values())),
         'entries_with_declared_dependencies':sum(bool(v) for v in graph.values()),
         'nontrivial_sccs':cycles,
         'warning':'Documentation links are not a complete proof graph. A cycle is not proof of logical circularity; an empty list is not proof of independence.'},
      'representation_control':{'forms':representation,'test_points':count,'maximum_relative_difference':rel,
                                'criterion':1e-12,'status':'PASS'},
      'global_complexity_rank':'UNRESOLVED_NOT_DEFINED',
      'physical_truth':'NOT_TESTED'
    }
    (OUT/'metrics.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    (OUT/'source_hashes.json').write_text(json.dumps({p.name:sha(p) for p in sorted((ROOT/'sources').glob('*'))},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['source_classification_counts','marker_definitions']},indent=2,ensure_ascii=False))

if __name__=='__main__':main()
