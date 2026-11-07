"""Record actual subprocess commands, environment, outputs and exit codes."""
import argparse, datetime, json, os, pathlib, shlex, subprocess, sys, time
p=argparse.ArgumentParser()
p.add_argument('--cwd',required=True)
p.add_argument('--log-dir',required=True)
p.add_argument('--name',required=True)
p.add_argument('command',nargs=argparse.REMAINDER)
a=p.parse_args()
cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
out=pathlib.Path(a.log_dir); out.mkdir(parents=True,exist_ok=True)
start=datetime.datetime.now(datetime.timezone.utc).isoformat(); t=time.monotonic()
proc=subprocess.run(cmd,cwd=a.cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
(out/(a.name+'.stdout.txt')).write_text(proc.stdout)
(out/(a.name+'.stderr.txt')).write_text(proc.stderr)
record={'name':a.name,'started_utc':start,'cwd':str(pathlib.Path(a.cwd).resolve()),'argv':cmd,
        'shell_rendering':shlex.join(cmd),'exit_code':proc.returncode,'elapsed_seconds':time.monotonic()-t,
        'environment':{k:os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},
        'stdout':a.name+'.stdout.txt','stderr':a.name+'.stderr.txt'}
with (out/'commands.jsonl').open('a') as f:f.write(json.dumps(record)+'\n')
print(json.dumps(record),flush=True)
print(proc.stdout,end=''); print(proc.stderr,end='',file=sys.stderr)
sys.exit(proc.returncode)
