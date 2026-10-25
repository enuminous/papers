"""Fetch only selected members of the public Figshare archives using HTTP ranges.
Original byte provenance: DOI 10.6084/m9.figshare.27047617.v1 (CC BY 4.0).
"""
import urllib.request, json, struct, zipfile, zlib, hashlib, time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
META=json.loads((ROOT/'source/figshare_metadata.json').read_text())

def get_range(url, start, end):
    req=urllib.request.Request(url, headers={'Range':f'bytes={start}-{end}'})
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 206: raise RuntimeError(f'Range ignored: {r.status}')
        cr=r.headers.get('Content-Range','')
        if not cr.startswith(f'bytes {start}-{end}/'): raise RuntimeError(cr)
        b=r.read()
    if len(b)!=end-start+1: raise RuntimeError('Incomplete range')
    return b

def inventory(name):
    f=next(x for x in META['files'] if x['name']==name)
    tail_path=ROOT/'source'/(name+'.tail')
    tail=tail_path.read_bytes() if tail_path.exists() else get_range(f['download_url'],f['size']-65536,f['size']-1)
    pos=tail.rfind(b'PK\x05\x06')
    eocd=struct.unpack('<4s4H2IH',tail[pos:pos+22])
    central_size, central_offset=eocd[5:7]
    # None of these source archives requires ZIP64 central-directory offsets.
    if central_offset < f['size']-len(tail):
        tail=get_range(f['download_url'],central_offset,f['size']-1)
    p=ROOT/'source'/(name+'.sparse')
    with p.open('wb') as w: w.seek(f['size']-len(tail));w.write(tail)
    with zipfile.ZipFile(p) as z: infos=z.infolist()
    (ROOT/'source'/(name+'.entries.json')).write_text(json.dumps([dict(name=i.filename,size=i.file_size,compressed=i.compress_size,offset=i.header_offset,crc=i.CRC,method=i.compress_type) for i in infos],indent=2))
    return f,infos

def fetch_member(f,i,destination):
    path=ROOT/destination
    if path.exists() and path.stat().st_size==i.file_size:
        b=path.read_bytes()
        if zlib.crc32(b)==i.CRC: print('Verified cached',path.name,flush=True);return
    print('Fetching',i.filename,i.file_size,flush=True)
    h=get_range(f['download_url'],i.header_offset,i.header_offset+29)
    fields=struct.unpack('<4s5H3I2H',h)
    start=i.header_offset+30+fields[-2]+fields[-1]
    b=get_range(f['download_url'],start,start+i.compress_size-1)
    if i.compress_type==8: b=zlib.decompress(b,-15)
    elif i.compress_type!=0: raise ValueError('Unsupported compression')
    assert len(b)==i.file_size and zlib.crc32(b)==i.CRC
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(b)
    print('Saved',path.name,'sha256',hashlib.sha256(b).hexdigest(),flush=True)

if __name__=='__main__':
    f,infos=inventory('SourceData.zip')
    wanted=['SourceData/README.txt','SourceData/SupplementaryData1/df_tx_MCF10A.xlsx','SourceData/SupplementaryData1/df_ETGs_MCF10A.xlsx','SourceData/SupplementaryData1/df_erk_MCF10A.xlsx']
    for name in wanted:
        i=next(x for x in infos if x.filename==name)
        fetch_member(f,i,'data/'+Path(name).name)
    f,infos=inventory('Code_files.zip')
    print('Code entries',len(infos),flush=True)
    for i in infos:
        if i.filename.endswith(('.m','.py','.ipynb','.txt')) and not any(x in i.filename for x in ['site-packages','.git/','__MACOSX']):
            print('CODE',i.filename,i.file_size,flush=True)
    selected=[i for i in infos if i.filename.endswith(('DEMO.m','Figure_script.m','PredictionModel_exp2.ipynb','README.ipynb'))]
    for i in selected: fetch_member(f,i,'source/code/'+Path(i.filename).name)
