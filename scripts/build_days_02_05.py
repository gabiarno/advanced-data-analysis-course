"""Rebuild the source notebooks for Days 2–5; no network or external data needed."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n')
def nb(folder,title,sections,tasks):
 cells=[]
 def add(kind,text):
  cell={'cell_type':kind,'id':f'cell-{len(cells):03d}','metadata':{},'source':text.strip().splitlines(True)}
  if kind=='code':cell.update(execution_count=None,outputs=[])
  cells.append(cell)
 add('markdown',f'# {title}\n\nAll data are synthetic. Run from top to bottom. Work in pairs and pause after each result to explain its meaning. Use TEACHING_GUIDE.md and TASK_CARDS.md for timing. Optional sections are marked. Numerical outputs are examples, not evidence about real operations.')
 for heading,explanation,source in sections:
  add('markdown','## '+heading+'\n\n'+explanation);add('code',source)
 obj={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.12'}},'nbformat':4,'nbformat_minor':5}
 prefix='spark_' if title == 'Day 5 — Spark SQL and MLlib' else ''
 write(folder+'/'+prefix+'worked.ipynb',json.dumps(obj,indent=2))
 # Student copy includes runnable scaffolding, then tasks to adapt it; learners do not type models from scratch.
 add('markdown','# Your pair challenge\n\nUse the working examples above. Complete the tasks below in new cells. For model experiments use training/validation data; do not optimise against a final test set.')
 for task in tasks:
  add('markdown',task);add('code','# Add your experiment or calculation here.\n')
 write(folder+'/'+prefix+'student.ipynb',json.dumps(obj,indent=2))

nb('day-02-machine-learning','Day 2 — Predict, evaluate and compare',[
('1. Define a prediction problem','Predict route duration before departure. Inputs are planned distance and stops; actual duration and the derived delayed flag are outcomes. Independent synthetic routes allow random splitting here. Real time-dependent routes would require chronological evaluation.', '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, confusion_matrix, classification_report, accuracy_score
rng=np.random.default_rng(22)
X=pd.DataFrame({'distance_km':rng.uniform(1,40,400),'stops':rng.integers(1,9,400)})
y=12+2.4*X.distance_km+4*X.stops+rng.normal(0,9,len(X))
delayed=(y>85).astype(int)
X.loc[::23,'distance_km']=np.nan
train_ids,test_ids=train_test_split(np.arange(len(X)),test_size=.25,random_state=42,stratify=delayed)
X_train,X_test=X.iloc[train_ids],X.iloc[test_ids]
y_train,y_test=y.iloc[train_ids],y.iloc[test_ids]
c_train,c_test=delayed.iloc[train_ids],delayed.iloc[test_ids]
print('Rows:',len(X),'Training:',len(X_train),'Final test:',len(X_test))
print(X.head().to_string(index=False))'''),
('2. Regression and a baseline','The imputer learns only from training rows. Cross-validation measures performance within training data. Larger scikit-learn scores are better, so neg_mean_absolute_error is negated for readable MAE. This lab preselects linear regression; the final test is used once.', '''cv=KFold(n_splits=5,shuffle=True,random_state=42)
reg=make_pipeline(SimpleImputer(strategy='median'),LinearRegression())
cv_mae=-cross_val_score(reg,X_train,y_train,cv=cv,scoring='neg_mean_absolute_error')
reg.fit(X_train,y_train)
base=DummyRegressor(strategy='mean').fit(X_train,y_train)
print('Validation MAE by fold:',np.round(cv_mae,2))
print('Baseline final-test MAE:',round(mean_absolute_error(y_test,base.predict(X_test)),2))
print('Regression final-test MAE:',round(mean_absolute_error(y_test,reg.predict(X_test)),2))
plt.figure(figsize=(6,4));plt.scatter(y_test,reg.predict(X_test),alpha=.6)
plt.xlabel('Actual minutes');plt.ylabel('Predicted minutes');plt.title('Held-out route durations');plt.tight_layout();plt.show()'''),
('3. Classification and model selection','Compare logistic regression, a tree and a forest on training folds. Tune a small forest grid on those same training data. Select a candidate using validation only. Final test metrics do not feed further choices. Accuracy can hide different types of error.', '''scv=StratifiedKFold(n_splits=4,shuffle=True,random_state=42)
candidates={
 'logistic':make_pipeline(SimpleImputer(),StandardScaler(),LogisticRegression(max_iter=1000)),
 'tree':make_pipeline(SimpleImputer(),DecisionTreeClassifier(max_depth=3,random_state=42)),
 'forest':make_pipeline(SimpleImputer(),RandomForestClassifier(n_estimators=60,max_depth=5,random_state=42,n_jobs=1))}
scores={name:cross_val_score(model,X_train,c_train,cv=scv,scoring='f1').mean() for name,model in candidates.items()}
search=GridSearchCV(candidates['forest'],{'randomforestclassifier__max_depth':[3,5,None],'randomforestclassifier__min_samples_leaf':[2,5]},cv=scv,scoring='f1',n_jobs=1)
search.fit(X_train,c_train)
scores['tuned_forest']=search.best_score_
candidates['tuned_forest']=search.best_estimator_
selected_name=max(scores,key=scores.get)
selected=candidates[selected_name].fit(X_train,c_train)
pred=selected.predict(X_test)
dummy=DummyClassifier(strategy='most_frequent').fit(X_train,c_train)
print('Validation F1:',{k:round(v,3) for k,v in scores.items()})
print('Selected before testing:',selected_name)
print('Baseline accuracy:',round(accuracy_score(c_test,dummy.predict(X_test)),3))
print('Confusion matrix: rows=actual, columns=predicted; class order [0,1]')
print(confusion_matrix(c_test,pred,labels=[0,1]))
print(classification_report(c_test,pred,zero_division=0))'''),
('4. Clustering and PCA — guided extension','Unsupervised analysis uses only training features here. Standardisation prevents kilometres dominating stop counts solely because of units. K=3 is chosen for demonstration, not discovered as a true number of customer types. PCA rotates/compresses variation; it does not establish business meaning.', '''from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
prep=make_pipeline(SimpleImputer(),StandardScaler())
Z=prep.fit_transform(X_train)
clusters=KMeans(n_clusters=3,n_init=10,random_state=42).fit_predict(Z)
pca=PCA(n_components=1).fit(Z)
print('Cluster counts:',np.bincount(clusters))
print('Variance retained by one component:',round(pca.explained_variance_ratio_[0],3))
plt.figure(figsize=(6,4));plt.scatter(Z[:,0],Z[:,1],c=clusters,cmap='viridis',s=18)
plt.xlabel('Standardised distance');plt.ylabel('Standardised stops');plt.title('Exploratory route groups');plt.tight_layout();plt.show()''')],
['A. Explain the two regression MAEs in minutes. Why is the baseline necessary?',
 'B. From the confusion matrix calculate false negatives: actual delayed, predicted not delayed. Explain their operational cost. Do not alter the threshold using this test set.',
 'C. On training folds only, compare tree depths 1, 3 and 8. Record training accuracy and mean validation F1. A larger gap suggests overfitting; it does not prove that depth 8 always performs worse.',
 'Extension. Compare k=2 and k=4 on Z. Explain why different partitions are not automatically errors.'])

nb('day-03-time-series-nlp','Day 3 — Forecast a series and classify text',[
('1. Build an ordered series','Daily synthetic demand contains a trend and a seven-day pattern. Hold out the final 28 days before fitting or choosing models. Do not shuffle future and past.', '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
rng=np.random.default_rng(33)
t=np.arange(210)
series=pd.Series(120+.15*t+18*np.sin(2*np.pi*t/7)+rng.normal(0,5,len(t)),index=pd.date_range('2026-01-01',periods=len(t),freq='D'),name='demand')
train,test=series.iloc[:-28],series.iloc[-28:]
print('Training:',train.index.min().date(),train.index.max().date())
print('Final test:',test.index.min().date(),test.index.max().date())
train.plot(figsize=(8,3),title='Training demand only');plt.ylabel('Units per day');plt.tight_layout();plt.show()'''),
('2. Trend, seasonality and baselines','A seven-day trailing mean smooths the series; it is not a complete statistical decomposition. Lag-7 correlation can reflect seasonality and trend together. Last-value and weekly-repeat forecasts use only past observations. The two baseline rules are predeclared, not selected on the final test.', '''rolling=train.rolling(7).mean()
print('Lag-7 correlation:',round(train.autocorr(7),3))
fig,ax=plt.subplots(figsize=(8,3));train.plot(ax=ax,label='Observed');rolling.plot(ax=ax,label='Trailing 7-day mean');ax.legend();ax.set_ylabel('Demand units');plt.tight_layout();plt.show()
last=np.repeat(train.iloc[-1],len(test))
weekly=np.resize(train.iloc[-7:].to_numpy(),len(test))
print('Last-value test MAE:',round(mean_absolute_error(test,last),2))
print('Weekly-repeat test MAE:',round(mean_absolute_error(test,weekly),2))'''),
('3. ARIMA and decomposition — statsmodels required','ARIMA(p,d,q) combines autoregressive lags, differencing and moving-average error terms. Here (1,1,1) is a fixed illustration, not a tuned optimum. It does not explicitly model the known weekly seasonality. A model may lose to a seasonal baseline. Decomposition is fitted only to training data; its residuals are not forecast validation.', '''from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
parts=seasonal_decompose(train,model='additive',period=7)
parts.plot();plt.tight_layout();plt.show()
fit=ARIMA(train,order=(1,1,1)).fit()
forecast=fit.get_forecast(steps=len(test))
pred=forecast.predicted_mean
interval=forecast.conf_int()
print('ARIMA final-test MAE:',round(mean_absolute_error(test,pred),2))
print('Optimiser convergence:',fit.mle_retvals.get('converged'))
fig,ax=plt.subplots(figsize=(8,3));ax.plot(test.index,test.to_numpy(),label='Actual');ax.plot(pred.index,pred.to_numpy(),label='ARIMA')
ax.plot(test.index,weekly,label='Weekly baseline')
ax.fill_between(test.index,interval.iloc[:,0],interval.iloc[:,1],alpha=.2,label='Model 95% interval')
ax.set_ylabel('Demand units');ax.legend();plt.tight_layout();plt.show()'''),
('4. Text classification — a separate problem','Classify short English service messages into delivery or billing. These deliberately small authored examples teach a pipeline, not deployment accuracy or Arabic NLP. Training and test messages are listed separately; vocabulary is learned only from training text.', '''from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
texts=['delivery arrived late','where is my parcel','courier missed the address','shipment is delayed','package arrived damaged','tracking shows no delivery','driver could not find my building','my order has not arrived',
'invoice has an incorrect amount','payment was charged twice','please send my receipt','refund is missing','billing address is incorrect','card payment was rejected','the invoice includes extra charges','I need a payment refund']
labels=['delivery']*8+['billing']*8
test_texts=['parcel delivery is delayed','courier delivered a damaged package','tracking says my shipment arrived','driver missed my address','invoice charged twice','please refund this payment','receipt amount is incorrect','card charge is missing']
test_labels=['delivery']*4+['billing']*4
text_model=make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression(C=2,max_iter=1000))
text_model.fit(texts,labels)
text_pred=text_model.predict(test_texts)
print(pd.DataFrame({'message':test_texts,'actual':test_labels,'predicted':text_pred}).to_string(index=False))
print(classification_report(test_labels,text_pred,zero_division=0))
print('Ambiguous message prediction:',text_model.predict(['my order payment is late'])[0])
print('A forced label is not proof of reliable understanding.')''')],
['A. Explain why a random split is inappropriate for this forecast. Compare the three predeclared MAEs without changing the models after seeing test results.',
 'B. Use train only to create a development split: last 14 training days as validation. Compare last-value and weekly-repeat forecasts on this validation window.',
 'C. For each held-out message, explain which words may have influenced the predicted label. Write two ambiguous messages and explain why human review may be needed.',
 'Extension. What data, language support and evaluation would be needed before using this pipeline for Arabic service messages? Do not infer performance from the English toy examples.'])

nb('day-04-bayesian-generative','Day 4 — Update uncertainty and generate data',[
('1. A probability model for defects','Let p be an unknown defect probability. Prior Beta(2,18) has mean 0.10. Observing 8 defects in 100 independent inspected items yields Beta(10,110). This assumes a stable rate and a representative sample. Posterior is proportional to likelihood times prior.', '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import beta
rng=np.random.default_rng(44)
a,b=2,18
n,k=100,8
post_a,post_b=a+k,b+n-k
lo,hi=beta.ppf([.025,.975],post_a,post_b)
print('Prior mean:',a/(a+b))
print('Posterior parameters:',post_a,post_b)
print('Posterior mean:',post_a/(post_a+post_b))
print('95% equal-tailed credible interval:',np.round([lo,hi],4))
print('Posterior probability p > 0.10:',round(beta.sf(.10,post_a,post_b),4))
grid=np.linspace(.001,.35,400)
plt.figure(figsize=(7,3));plt.plot(grid,beta.pdf(grid,a,b),label='Prior');plt.plot(grid,beta.pdf(grid,post_a,post_b),label='Posterior');plt.xlabel('Defect probability');plt.ylabel('Probability density');plt.legend();plt.tight_layout();plt.show()'''),
('2. MCMC: a real Metropolis sampler — guided demonstration','Direct Beta sampling is available, so MCMC is unnecessary for this problem; the exact posterior lets us check the sampler. Propose a symmetric Gaussian step in p, reject proposals outside (0,1), then accept according to the posterior-density ratio. Repeated states are legitimate. Never clip proposals to the boundary: that changes the proposal mechanism.', '''def metropolis(start,seed,steps=12000,proposal_sd=.025):
    random=np.random.default_rng(seed)
    p=start; chain=np.empty(steps); accepted=0
    for i in range(steps):
        proposal=p+random.normal(0,proposal_sd)
        if 0<proposal<1:
            log_ratio=beta.logpdf(proposal,post_a,post_b)-beta.logpdf(p,post_a,post_b)
            if np.log(random.uniform())<min(0,log_ratio):
                p=proposal;accepted+=1
        chain[i]=p
    return chain,accepted/steps
runs=[metropolis(start,seed) for start,seed in [(0.02,1),(0.35,2),(0.65,3),(0.9,4)]]
chains=np.array([run[0][2000:] for run in runs])
print('Acceptance rates:',np.round([run[1] for run in runs],3))
print('Retained-chain means:',np.round(chains.mean(axis=1),4))
print('Exact mean:',round(post_a/(post_a+post_b),4))
print('Pooled MCMC interval:',np.round(np.quantile(chains,[.025,.975]),4))
fig,axes=plt.subplots(1,2,figsize=(10,3))
for row in chains: axes[0].plot(row[:500],alpha=.6)
axes[0].set(xlabel='Retained iteration',ylabel='p',title='First 500 retained draws')
axes[1].hist(chains.ravel(),bins=40,density=True,alpha=.5);axes[1].plot(grid,beta.pdf(grid,post_a,post_b));axes[1].set(xlabel='p',title='Sample versus exact density')
plt.tight_layout();plt.show()
print('Lag-1 correlations:',np.round([np.corrcoef(row[:-1],row[1:])[0,1] for row in chains],3))'''),
('3. Posterior predictive simulation','Uncertainty about p and variability in a new batch are different. Draw p from the posterior, then draw the number of defects in 100 future items. This produces synthetic counts. A credible interval for p is not a predictive interval for a future defect count.', '''p_draws=rng.beta(post_a,post_b,10000)
future_counts=rng.binomial(100,p_draws)
print('Expected future defects in 100:',round(future_counts.mean(),2))
print('Central 95% simulated count interval:',np.quantile(future_counts,[.025,.975]))
print('Probability of more than 12 future defects:',round(np.mean(future_counts>12),3))
plt.figure(figsize=(7,3));plt.hist(future_counts,bins=np.arange(0,32)-.5);plt.xlabel('Defects in next 100 items');plt.ylabel('Simulation count');plt.tight_layout();plt.show()'''),
('4. Generate synthetic service times','A fitted lognormal model produces positive synthetic durations. Fit in log space and sample. This is a simple generative statistical model, not a GAN. Matching a marginal mean does not preserve relationships, privacy or realism.', '''observed=rng.lognormal(mean=3,sigma=.35,size=150)
log_mu=np.log(observed).mean();log_sd=np.log(observed).std(ddof=1)
synthetic=rng.lognormal(log_mu,log_sd,150)
summary=pd.DataFrame({'observed':observed,'synthetic':synthetic}).describe().loc[['mean','std','min','50%','max']]
print(summary.round(2))
fig,ax=plt.subplots(figsize=(7,3));ax.hist(observed,bins=15,alpha=.5,label='Observed synthetic source');ax.hist(synthetic,bins=15,alpha=.5,label='Generated');ax.set_xlabel('Service minutes');ax.legend();plt.tight_layout();plt.show()''')],
['A. Replace the prior with Beta(1,1), using the same 8 defects in 100. Compare posterior means and explain prior sensitivity.',
 'B. Calculate a posterior for 16 defects in 200 inspected items under Beta(2,18). Compare interval widths with the original case.',
 'C. Explain why the interval for p cannot be used directly as an interval for the number of defects in a future batch.',
 'Extension. Run metropolis with proposal_sd=.001. Compare trace movement and lag-1 correlation. High acceptance does not imply efficient exploration.'])

nb('day-05-big-data','Day 5 — Distributed thinking, neural networks and a toy GAN',[
('1. Map, combine and reduce on a laptop','A local simulation divides records into partitions, computes partial totals, then combines them. This illustrates the idea of distributed aggregation; it is not Hadoop or Spark execution. Hadoop includes HDFS storage, YARN resource management and MapReduce processing. Spark uses a different execution engine and can work with Hadoop storage/resource infrastructure.', '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
rows=[('A',10),('B',20),('A',5),('C',7),('B',3),('C',8)]
partitions=[rows[:3],rows[3:]]
partials=[]
for partition in partitions:
    subtotal=defaultdict(int)
    for key,value in partition: subtotal[key]+=value
    partials.append(dict(subtotal))
combined=defaultdict(int)
for partial in partials:
    for key,value in partial.items(): combined[key]+=value
print('Partial totals:',partials)
print('Combined totals:',dict(sorted(combined.items())))
assert dict(combined)=={'A':15,'B':23,'C':15}'''),
('2. A small neural network','Two hidden layers form a small multilayer perceptron. Scaling is fitted on training data only. This local synthetic example is not big-data training and uses no GPU. Compare with a linear decision boundary. Architectures are fixed before test evaluation; do not choose a new architecture from test results.', '''from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X,y=make_moons(n_samples=600,noise=.22,random_state=55)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
linear=make_pipeline(StandardScaler(),LogisticRegression()).fit(X_train,y_train)
network=make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=(16,8),max_iter=1200,early_stopping=True,n_iter_no_change=30,random_state=42)).fit(X_train,y_train)
print('Linear test accuracy:',round(accuracy_score(y_test,linear.predict(X_test)),3))
print('Neural-network test accuracy:',round(accuracy_score(y_test,network.predict(X_test)),3))
print('Network training iterations:',network[-1].n_iter_)
plt.figure(figsize=(6,3));plt.plot(network[-1].loss_curve_);plt.xlabel('Epoch');plt.ylabel('Training loss');plt.title('Loss is not a test-set metric');plt.tight_layout();plt.show()'''),
('3. A tiny adversarial generator — optional demonstration','This is an actual one-dimensional adversarial training loop, not an image GAN or a deep network. Generator G(z)=mu+sigma*z produces a Gaussian. Discriminator uses logistic scores of x and x squared. Alternate discriminator and generator updates. The exercise illustrates competing objectives and instability, not useful production synthesis.', '''from scipy.special import expit
rng=np.random.default_rng(55)
mu,log_sigma=-1.0,0.0
w=np.zeros(3)
log=[]
for step in range(2500):
    real=rng.normal(2,.6,256)
    z=rng.normal(size=256)
    fake=mu+np.exp(log_sigma)*z
    phi_r=np.column_stack([np.ones(len(real)),real,real**2])
    phi_f=np.column_stack([np.ones(len(fake)),fake,fake**2])
    pr,pf=expit(phi_r@w),expit(phi_f@w)
    w+=.03*((1-pr)@phi_r/len(real)-pf@phi_f/len(fake))
    z=rng.normal(size=256);sigma=np.exp(log_sigma);fake=mu+sigma*z
    score=w[0]+w[1]*fake+w[2]*fake**2
    gradient=(expit(score)-1)*(w[1]+2*w[2]*fake)
    mu-=.01*gradient.mean()
    log_sigma-=.01*np.mean(gradient*sigma*z)
    log_sigma=float(np.clip(log_sigma,-2,1))
    if step%250==0:log.append((step,mu,np.exp(log_sigma)))
print(pd.DataFrame(log,columns=['step','generator_mean','generator_sd']).round(3).to_string(index=False))
print('Target mean/sd:',2,.6,'Final generator:',round(mu,3),round(np.exp(log_sigma),3))
generated=mu+np.exp(log_sigma)*rng.normal(size=2000)
reference=rng.normal(2,.6,2000)
plt.figure(figsize=(7,3));plt.hist(reference,bins=30,alpha=.5,label='Reference');plt.hist(generated,bins=30,alpha=.5,label='Generator');plt.xlabel('Synthetic scalar value');plt.ylabel('Count');plt.legend();plt.tight_layout();plt.show()
print('An overlapping histogram is not a privacy or deployment-quality guarantee.')''')],
['A. Add (A,4) to the partition example and recompute the totals. Explain which stage requires combining matching keys.',
 'B. In spark_worked.ipynb, run aggregation and SQL, then explain what collect would do to memory on a large dataset. Use OFFLINE_ACTIVITY.md if Spark is unavailable.',
 'C. Compare the fixed neural-network and linear results. State why this does not prove neural networks always win.',
 'Extension. Inspect the adversarial generator log. Explain the generator and discriminator roles, and why this Gaussian toy cannot generate realistic customer records.'])

nb('day-05-big-data','Day 5 — Spark SQL and MLlib',[
('1. Start local Spark','Requires Java 17 and PySpark 4.0.1. This standalone lab runs on one laptop using two local threads. Do not present its timing as a cluster benchmark. Use OFFLINE_ACTIVITY.md if the environment was not successfully rehearsed.', '''import os
os.environ.setdefault('SPARK_LOCAL_IP','127.0.0.1')
from pyspark.sql import SparkSession,functions as F
spark=SparkSession.builder.master('local[2]').appName('course-day5').config('spark.ui.enabled','false').config('spark.sql.shuffle.partitions','2').getOrCreate()
spark.sparkContext.setLogLevel('ERROR')
print('Spark version:',spark.version)
df=spark.range(0,10000).withColumn('region',F.when(F.col('id')%2==0,'A').otherwise('B')).withColumn('amount',(F.col('id')%100+1).cast('double'))
print('Rows:',df.count())
df.show(5)'''),
('2. Aggregate with DataFrames and SQL','Transformations build a plan; actions trigger execution. groupBy may require shuffling records by key. Only collect a tiny aggregate, not a large source table.', '''totals=df.groupBy('region').agg(F.count('*').alias('orders'),F.sum('amount').alias('revenue')).orderBy('region')
totals.show()
df.createOrReplaceTempView('orders')
sql_totals=spark.sql('SELECT region, COUNT(*) AS orders, SUM(amount) AS revenue FROM orders GROUP BY region ORDER BY region')
assert totals.collect()==sql_totals.collect()
print('DataFrame and SQL totals agree.')
totals.explain()'''),
('3. Train a Spark MLlib regression pipeline','Synthetic route features and target are constructed in Spark. The id-based split is predetermined for this independent synthetic example, not a recommended temporal split. Real chronology or grouped identities require a suitable split. VectorAssembler creates the feature vector expected by MLlib.', '''from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
routes=spark.range(0,1000).withColumn('distance',1+30*F.rand(seed=42)).withColumn('stops',F.floor(1+7*F.rand(seed=43))).withColumn('duration',12+2.4*F.col('distance')+4*F.col('stops')+3*F.randn(seed=44)).cache()
train=routes.filter(F.col('id')%5!=0)
test=routes.filter(F.col('id')%5==0)
pipeline=Pipeline(stages=[VectorAssembler(inputCols=['distance','stops'],outputCol='features'),LinearRegression(featuresCol='features',labelCol='duration',regParam=.01,maxIter=50)])
model=pipeline.fit(train)
predictions=model.transform(test)
evaluator=RegressionEvaluator(labelCol='duration',predictionCol='prediction',metricName='mae')
mae=evaluator.evaluate(predictions)
training_mean=train.agg(F.avg('duration')).first()[0]
baseline_mae=test.select(F.avg(F.abs(F.col('duration')-F.lit(training_mean)))).first()[0]
print('Training rows:',train.count(),'Test rows:',test.count())
print('Model MAE:',round(mae,3),'Baseline MAE:',round(baseline_mae,3))
assert mae<baseline_mae
predictions.select('duration','prediction').show(5)
routes.unpersist()
spark.stop()''')],['Change the SQL to compute mean amount by region. Compare it with revenue divided by order count.','Explain the difference between a transformation and an action using this notebook.'])
