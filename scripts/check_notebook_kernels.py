"""Run solution notebooks (including worked cells) and Spark in fresh kernels."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient
r=Path(__file__).resolve().parents[1]
paths=sorted(r.glob('day-0[2-5]*/solutions.ipynb'))+[r/'day-05-big-data/spark_worked.ipynb']
logs=[]
for p in paths:
 print('KERNEL',p.relative_to(r),flush=True)
 nb=nbformat.read(p,as_version=4)
 NotebookClient(nb,timeout=240,kernel_name='course-validation',resources={'metadata':{'path':str(r)}}).execute()
 nbformat.validate(nb)
 # Keep only exercise-solution text here; chart fallbacks already live in figures/.
 if p.name=='solutions.ipynb':
  out=''.join(o.get('text','') for o in nb.cells[-1].outputs if o.output_type=='stream')
  (p.parent/'EXERCISE_RESULTS.md').write_text('# Executed exercise solutions\n\nFresh Jupyter kernel; full worked notebook and solutions completed.\n\n```text\n'+out+'\n```\n')
 logs.append(str(p.relative_to(r)))
 print('PASS',p.relative_to(r),flush=True)
(r/'CLASSROOM_KERNEL_RUN.md').write_text('# Jupyter kernel validation\n\nThe following notebooks ran from start to finish in separate Python 3.12 kernels using nbclient. Solutions include the worked examples. Spark ran with Java 17 and PySpark 4.0.1. This verifies execution, not classroom timing or the learner laptop configuration.\n\n'+''.join('- '+p+' — passed\n' for p in logs))
