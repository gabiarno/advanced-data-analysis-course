"""Build the conversational Markdown handbook and its illustrated PDF.

Run from the repository root: python scripts/build_visual_handbook.py
Requires reportlab, matplotlib, numpy, scipy and Pillow.
Content source: participant/handbook_content.json.
All chart inputs are synthetic course results or labelled schematic examples.
"""
from pathlib import Path
import json
import html
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.stats import beta, norm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Image, KeepTogether, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
ASSETS=OUT/'handbook-assets'
OUT.mkdir(exist_ok=True);ASSETS.mkdir(exist_ok=True)
PAGES=json.loads((ROOT/'participant/handbook_content.json').read_text())
NAVY='#173447';TEAL='#007F82';GOLD='#DAA441';CORAL='#C85D4D';PALE='#EAF4F2';INK='#243A45';MUTED='#536670'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.edgecolor':'#C7D4D9','text.color':INK,'axes.labelcolor':INK,'xtick.color':MUTED,'ytick.color':MUTED,'figure.facecolor':'white','axes.facecolor':'white'})

def figbase():
 fig,ax=plt.subplots(figsize=(8.8,3.0));return fig,ax

def boxes(ax,labels,links=True):
 ax.set_xlim(0,10);ax.set_ylim(0,3);ax.axis('off');n=len(labels);w=8.8/n;gap=.14
 for i,label in enumerate(labels):
  x=.3+i*w
  ax.add_patch(FancyBboxPatch((x,.9),w-gap,1.2,boxstyle='round,pad=.04,rounding_size=.10',fc=PALE,ec=TEAL,lw=1.3))
  ax.text(x+(w-gap)/2,1.5,label,ha='center',va='center',fontsize=11,color=NAVY)
  if i<n-1 and links:ax.annotate('',xy=(x+w-.03,1.5),xytext=(x+w-gap+.03,1.5),arrowprops={'arrowstyle':'->','color':TEAL,'lw':1.5})

def save(name,fig):
 fig.tight_layout(pad=1.2);fig.savefig(ASSETS/f'{name}.png',dpi=170,bbox_inches='tight');plt.close(fig)

def charts():
 for name,labels in [('workflow',['Frame\nthe decision','Inspect\nthe evidence','Analyse\nand compare','Challenge\nthe result','Decide\nand review']),('review',['Agree\ndefinitions','Repeatable\nanalysis','Colleague\nreview','Decision\nrecord']),('audit',['122\nraw rows','119\nvalid orders','116\npriced orders']),('uncertainty',['Unknown rate\np','Possible rate\nfrom posterior','Future batch\ncount'])]:
  fig,ax=figbase();boxes(ax,labels);save(name,fig)
 fig,ax=figbase();v=[6310,3700,200];ax.barh(['Store','Online','Unknown'],v,color=[TEAL,NAVY,GOLD]);ax.invert_yaxis();ax.set_xlim(0,7600);ax.set_xlabel('Known revenue (EUR)');ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
 for i,x in enumerate(v):ax.text(x+100,i,f'{x:,}',va='center',weight='bold')
 save('revenue',fig)
 fig,axs=plt.subplots(1,4,figsize=(8.8,3.0));rng=np.random.default_rng(8)
 axs[0].bar(['A','B','C'],[3,6,4],color=TEAL);axs[0].set_title('Compare')
 axs[1].plot([1,2,3,4,5],[2,4,3,5,6],color=TEAL,marker='o');axs[1].set_title('Follow time')
 axs[2].hist(rng.normal(size=100),bins=8,color=TEAL);axs[2].set_title('See spread')
 x=np.arange(15);axs[3].scatter(x,x*.4+rng.normal(size=15),color=TEAL);axs[3].set_title('Explore a link')
 for a in axs:a.set_xticks([]);a.set_yticks([])
 save('chart_choices',fig)
 fig,ax=figbase();boxes(ax,['Training\nlearn parameters','Validation\ncompare choices','Final test\none final check']);save('split',fig)
 for name,labels,vals in [('mae',['Training-mean baseline','Regression model'],[24.34,8.43]),('forecast',['Last value','Weekly repeat','Fixed ARIMA'],[22.38,5.53,22.11])]:
  fig,ax=figbase();ax.barh(labels,vals,color=[NAVY,TEAL,GOLD][:len(vals)]);ax.invert_yaxis();ax.set_xlim(0,max(vals)*1.3);ax.set_xlabel('MAE (minutes)' if name=='mae' else 'MAE (daily demand units)');ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
  for i,x in enumerate(vals):ax.text(x+.3,i,f'{x:.2f}',va='center',weight='bold')
  save(name,fig)
 fig,ax=plt.subplots(figsize=(7,3.2));ax.axis('off');tab=ax.table(cellText=[['55\nCorrect on time','2\nFalse alarms'],['9\nMissed delays','34\nDetected delays']],rowLabels=['Actual on time','Actual delayed'],colLabels=['Predicted on time','Predicted delayed'],cellLoc='center',loc='center',bbox=[.26,.04,.72,.88]);tab.auto_set_font_size(False);tab.set_fontsize(11)
 for (r,c),cell in tab.get_celld().items():cell.set_edgecolor('white');cell.set_facecolor(PALE if r else NAVY);cell.set_text_props(color='white' if r==0 else INK)
 save('confusion',fig)
 fig,ax=figbase();ax.set_xlim(0,12);ax.set_ylim(-.7,3.7);ax.set_yticks([3,2,1]);ax.set_yticklabels(['Origin 1','Origin 2','Origin 3']);ax.set_xlabel('Time → (schematic)');ax.set_xticks([])
 for y,end in [(3,4),(2,6),(1,8)]:ax.barh(y,end,height=.5,color=TEAL);ax.barh(y,1.6,left=end,height=.5,color=GOLD)
 ax.barh(0,1.5,left=10,height=.5,color=NAVY);ax.text(5,.0,'Final holdout kept separate',va='center',fontsize=10);ax.text(.2,3.65,'Training',color=TEAL);ax.text(3,3.65,'Next-window validation',color='#946D1C');save('rolling',fig)
 fig,ax=figbase();x=np.linspace(.001,.35,500);ax.plot(x*100,beta.pdf(x,2,18),label='Prior: Beta(2,18)',color=GOLD,lw=2);ax.plot(x*100,beta.pdf(x,10,110),label='Posterior: Beta(10,110)',color=TEAL,lw=2.5);ax.fill_between(x*100,beta.pdf(x,10,110),where=x>.1,color=TEAL,alpha=.18);ax.axvline(10,color=NAVY,ls='--',lw=1);ax.set_xlabel('Possible underlying defect rate (%)');ax.set_ylabel('Density');ax.legend(frameon=False,fontsize=10);save('posterior',fig)
 fig,ax=figbase();boxes(ax,['Partition 1\n2 orders / EUR 100','Partition 2\n8 orders / EUR 320','Combine\nEUR 420 / 10 = 42']);save('partitions',fig)
 fig,ax=figbase();x=np.linspace(0,4,500);ax.plot(x,norm.pdf(x,2,.6),color=NAVY,lw=2,label='Target: mean 2.00, SD 0.60');ax.plot(x,norm.pdf(x,2.10,.287),color=CORAL,lw=2,label='Illustration: mean 2.10, SD 0.287');ax.set_xlabel('Generated value (teaching units)');ax.set_ylabel('Density');ax.legend(frameon=False,fontsize=9);save('gan',fig)

def markdown():
 result=['# Make the next decision better\n\n## Advanced Data Analysis - participant handbook\n\nPractical Python workshop for experienced analysts. English with Arabic interpretation.\n\n[Download the illustrated PDF](../dist/participant-handbook.pdf). The earlier detailed handbook is retained as [technical reference](HANDBOOK_TECHNICAL_REFERENCE.md).']
 for i,p in enumerate(PAGES):
  if i==0:continue
  result.append(f"\n## {p['title']}\n\n*{p['kicker']}*\n\n{p.get('body','')}")
  if p.get('visual'):result.append(f"\n![{p.get('caption',p['title'])}](../dist/handbook-assets/{p['visual']}.png)\n\n{p.get('caption','')}")
  if p.get('table'):
   t=p['table'];result.append('\n| '+' | '.join(t['headers'])+' |\n| '+' | '.join(['---']*len(t['headers']))+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in t['rows']))
  if p.get('callout'):result.append('\n> '+p['callout'])
  if p.get('notes'):result.append('\nYour notes: '+'_'*50)
  for label,url in p.get('references',[]):result.append(f'\n- [{label}]({url})')
 (ROOT/'participant/HANDBOOK.md').write_text('\n'.join(result)+'\n')

FONTDIR=Path(matplotlib.get_data_path())/'fonts/ttf'
pdfmetrics.registerFont(TTFont('DejaVu',str(FONTDIR/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DejaVu-Bold',str(FONTDIR/'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVu-Bold',italic='DejaVu',boldItalic='DejaVu-Bold')
STYLES={
 'body':ParagraphStyle('body',fontName='DejaVu',fontSize=10.2,leading=15.5,textColor=colors.HexColor(INK),spaceAfter=10),
 'title':ParagraphStyle('title',fontName='DejaVu-Bold',fontSize=25,leading=29,textColor=colors.HexColor(NAVY),spaceAfter=15),
 'caption':ParagraphStyle('caption',fontName='DejaVu',fontSize=8,leading=11,textColor=colors.HexColor(MUTED)),
 'cell':ParagraphStyle('cell',fontName='DejaVu',fontSize=9,leading=12,textColor=colors.HexColor(INK)),
 'headcell':ParagraphStyle('headcell',fontName='DejaVu-Bold',fontSize=9,leading=12,textColor=colors.white),
 'callout':ParagraphStyle('callout',fontName='DejaVu-Bold',fontSize=10,leading=15,textColor=colors.HexColor(NAVY)),
}

def clean(s):
 return s.replace('–','-').replace('—','-').replace('‑','-')

def para(s,style='body'):
 return Paragraph(html.escape(clean(s)).replace('\n','<br/>'),STYLES[style])

def pdf():
 w,h=595.276,841.89;m=48;usable=w-2*m
 c=canvas.Canvas(str(OUT/'participant-handbook.pdf'),pagesize=(w,h))
 c.setTitle('Make the next decision better | Advanced Data Analysis');c.setAuthor('Advanced Data Analysis course team');c.setSubject('Practical Python workshop: participant handbook')
 for i,p in enumerate(PAGES):
  c.setFillColor(colors.HexColor(TEAL));c.rect(0,h-9,w,9,fill=1,stroke=0)
  c.setFont('DejaVu-Bold',8);c.setFillColor(colors.HexColor(TEAL));c.drawString(m,h-43,clean(p['kicker']))
  y=h-66
  def put(flow,gap=10):
   nonlocal y
   fw,fh=flow.wrap(usable,h)
   if y-fh<55:raise RuntimeError(f'Page {i+1} overflow: {p["title"]}, y={y}, h={fh}')
   flow.drawOn(c,m,y-fh);y-=fh+gap
  if i==0:
   y-=45
   title=Paragraph('Make the next<br/>decision better',ParagraphStyle('cover',parent=STYLES['title'],fontSize=43,leading=49))
   put(title,25)
  else:put(para(p['title'],'title'),15)
  for block in p.get('body','').split('\n\n'):put(para(block),8)
  if p.get('visual'):
   image=ImageReader(str(ASSETS/f'{p["visual"]}.png'));iw,ih=image.getSize();height=min(185,usable*ih/iw);width=height*iw/ih
   if y-height<70:raise RuntimeError(f'Chart overflow on page {i+1}')
   c.drawImage(image,m+(usable-width)/2,y-height,width,height,mask='auto');y-=height+5
   if p.get('caption'):put(para(p['caption'],'caption'),12)
  if p.get('table'):
   t=p['table'];data=[[para(v,'headcell') for v in t['headers']]]+[[para(v,'cell') for v in row] for row in t['rows']]
   table=Table(data,colWidths=[usable/len(t['headers'])]*len(t['headers']))
   table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor(NAVY)),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor(PALE),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('LINEBELOW',(0,1),(-1,-1),.4,colors.HexColor('#DCE6E9'))]))
   put(table,16)
  if p.get('callout'):
   pflow=para(p['callout'],'callout');_,ph=pflow.wrap(usable-24,h);boxh=ph+20
   if y-boxh<55:raise RuntimeError(f'Callout overflow on {i+1}')
   c.setFillColor(colors.HexColor(PALE));c.roundRect(m,y-boxh,usable,boxh,6,fill=1,stroke=0);pflow.drawOn(c,m+12,y-10-ph);y-=boxh+15
  for label,url in p.get('references',[]):put(Paragraph(f'<link href="{html.escape(url,quote=True)}" color="{TEAL}">{html.escape(label)}</link>',STYLES['body']),8)
  if p.get('notes'):
   count=min(p['notes'],max(0,int((y-65)/21)))
   c.setStrokeColor(colors.HexColor('#D1DEE2'));c.setLineWidth(.5)
   for line in range(count):y-=21;c.line(m,y,m+usable,y)
  c.setStrokeColor(colors.HexColor('#DCE6E9'));c.line(m,42,w-m,42);c.setFillColor(colors.HexColor(MUTED));c.setFont('DejaVu',7)
  c.drawString(m,28,'ADVANCED DATA ANALYSIS  /  GENOA  /  PARTICIPANT EDITION');c.drawRightString(w-m,28,f'{i+1:02d} / {len(PAGES):02d}')
  c.showPage()
 c.save()

if __name__=='__main__':
 charts();markdown();pdf();print(f'Built {len(PAGES)} pages, Markdown source and {len(list(ASSETS.glob("*.png")))} visual assets.')
