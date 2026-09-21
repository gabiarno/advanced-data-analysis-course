# Reference 3 — English–Arabic glossary

**Draft for interpreter validation.** The Arabic column is a starting proposal, not an approved translation. Review it with the interpreter before Day 1 and correct anything they disagree with — their judgement takes precedence over this table in every case. Once agreed, the terms must be used consistently for all five days; switching terms mid-course is the fastest way to lose a bilingual audience.

**Code stays in English.** Function names, variable names, file paths and library names (`pandas`, `fit`, `predict`, `df`, `.ipynb`) are never translated. They are read aloud in English.

## Data and description

| English | Plain-English meaning | العربية |
|---|---|---|
| Dataset | A collection of observations | مجموعة بيانات |
| Row / observation | One recorded case | صف / مُشاهَدة |
| Column / variable | One recorded property | عمود / متغيّر |
| Missing value | Not recorded; not the same as zero | قيمة مفقودة |
| Duplicate record | A repeated row; whether it is an error depends on the rule | سجل مكرّر |
| Sample | The observations we actually have | عيّنة |
| Population | The wider set we want to describe | مجتمع الدراسة |
| Mean | Sum divided by count | المتوسط الحسابي |
| Median | The middle value after sorting | الوسيط |
| Standard deviation | Spread around the mean | الانحراف المعياري |
| Interquartile range | The range of the middle half | المدى الربيعي |
| Outlier | An unusually distant value; not necessarily an error | قيمة شاذّة |
| Correlation | Association between two quantities | الارتباط |
| Causation | One thing producing another | السببية |
| Distribution | How values are spread across their range | التوزيع |
| Probability | A number between 0 and 1 expressing how likely | الاحتمال |
| Uncertainty | What we do not know about a quantity | عدم اليقين |
| Bias | A systematic error in one direction | التحيّز |
| Synthetic data | Artificially generated observations | بيانات اصطناعية |

## Modelling

| English | Plain-English meaning | العربية |
|---|---|---|
| Model | A rule fitted from data to produce an output | نموذج |
| Feature | An input the model uses | سمة / متغيّر مُدخَل |
| Target | The outcome the model predicts | المتغيّر الهدف |
| Training | Estimating a model from examples | التدريب |
| Prediction | Applying the fitted model to a new input | التنبؤ |
| Training set | Examples used to fit the model | مجموعة التدريب |
| Validation set | Examples used to choose between models | مجموعة التحقّق |
| Test set | Held-out examples used once, for final evaluation | مجموعة الاختبار |
| Baseline | A simple reference method to compare against | النموذج المرجعي |
| Overfitting | Learning patterns that do not generalise | الإفراط في الملاءمة |
| Underfitting | The model is too simple to capture the pattern | قصور الملاءمة |
| Data leakage | Using information that would not really be available | تسرّب البيانات |
| Cross-validation | Repeated fitting and checking within the training data | التحقّق المتقاطع |
| Hyperparameter | A setting chosen outside the fitting | معلَمة فائقة |
| Pipeline | Preprocessing and model bound into one object | خط المعالجة |
| Regression | Predicting a number | الانحدار |
| Classification | Predicting a category | التصنيف |
| Clustering | Grouping similar observations, with no target | التجميع العنقودي |
| Decision tree | Successive decisions on feature values | شجرة القرار |
| Random forest | An average of many randomised trees | الغابة العشوائية |
| Dimensionality reduction | Representing data with fewer derived columns | تخفيض الأبعاد |
| PCA | Principal component analysis | تحليل المكوّنات الرئيسية |

## Evaluation

| English | Plain-English meaning | العربية |
|---|---|---|
| Confusion matrix | A table of correct and incorrect predictions by class | مصفوفة الالتباس |
| Accuracy | Fraction of all predictions that were correct | الدقة الإجمالية |
| Precision | Of the cases flagged, how many were real | الإحكام |
| Recall | Of the real cases, how many were caught | الاستدعاء |
| False alarm (false positive) | Flagged, but it was not real | إنذار كاذب |
| Missed case (false negative) | Real, but not flagged | حالة فائتة |
| MAE | Mean absolute error, in the target's units | متوسط الخطأ المطلق |
| RMSE | Root mean squared error; punishes large errors more | الجذر التربيعي لمتوسط مربّع الخطأ |

## Time series and text

| English | Plain-English meaning | العربية |
|---|---|---|
| Time series | Observations indexed in time order | سلسلة زمنية |
| Trend | A sustained direction over time | الاتجاه العام |
| Seasonality | A repeating pattern at a known period | الموسمية |
| Cycle | A repeating pattern without a fixed period | الدورة |
| Decomposition | Splitting a series into trend, season and residual | التفكيك |
| Residual | What the decomposition or model did not explain | البواقي |
| Forecast | A predicted future value | التنبؤ المستقبلي |
| Backtesting | Testing a forecast from many past cut points | الاختبار الرجعي |
| ARIMA | Autoregressive integrated moving average | نموذج أريما |
| Stationarity | Statistical properties that do not change over time | الاستقرارية |
| NLP | Natural language processing | معالجة اللغات الطبيعية |
| Text classification | Assigning a category to a document | تصنيف النصوص |
| Vocabulary | The set of terms the model represents | المفردات |
| Embedding | A numeric vector representing meaning | تضمين متّجهي |
| Large language model | A large model trained to process and produce text | نموذج لغوي كبير |

## Bayesian and generative

| English | Plain-English meaning | العربية |
|---|---|---|
| Prior | The distribution believed before this data | التوزيع القَبْلي |
| Likelihood | How compatible the data is with each possible value | دالة الإمكان |
| Posterior | The updated distribution after the data | التوزيع البَعْدي |
| Credible interval | An interval holding a stated posterior probability | الفترة المصداقية |
| MCMC | Markov chain Monte Carlo sampling | سلاسل ماركوف مونت كارلو |
| Chain | One sequence of sampled values | السلسلة |
| Warm-up / burn-in | Early draws discarded before the chain settles | فترة الإحماء |
| Autocorrelation | How much consecutive draws resemble each other | الارتباط الذاتي |
| Generative model | A model that produces new data resembling its source | نموذج توليدي |
| GAN | Generative adversarial network | الشبكات التوليدية التنافسية |
| Generator | Produces candidate data | المولِّد |
| Discriminator | Tries to distinguish generated from real | المميِّز |

## Scale and operations

| English | Plain-English meaning | العربية |
|---|---|---|
| Big data | Data whose size or rate exceeds one machine's capacity | البيانات الضخمة |
| Distributed computing | Processing across several machines or cores | الحوسبة الموزّعة |
| Partition | One slice of the data processed independently | تجزئة |
| MapReduce | Compute partial results, then combine by key | ماب-ريديوس |
| Shuffle | Moving data between partitions to group matching keys | إعادة توزيع البيانات |
| Cluster (computing) | Several machines working as one system | عنقود حاسوبي |
| Neural network | A model of connected layers of simple units | الشبكة العصبية |
| Deep learning | Neural networks with many layers | التعلّم العميق |
| Drift | The data or relationship changing after deployment | الانجراف |
| Monitoring | Continuously checking a deployed model's behaviour | المراقبة |

## Governance and European practice

This vocabulary is harder to interpret consistently than the statistical terms, and it carries legal weight. Give it its own time in the interpreter briefing.

| English | Plain-English meaning | العربية |
|---|---|---|
| Data protection | The body of rules governing use of personal data | حماية البيانات |
| Personal data | Information relating to an identifiable person | البيانات الشخصية |
| Data subject | The person the data is about | صاحب البيانات |
| Data controller | The body that decides why and how data is processed | المتحكم في البيانات |
| Legal basis | The lawful ground permitting the processing | الأساس القانوني |
| Purpose limitation | Data may be used only for the purpose it was collected for | تحديد الغرض |
| Data minimisation | Use no more data than the purpose requires | تقليل البيانات إلى الحد الأدنى |
| Storage limitation | Keep data no longer than necessary | تحديد مدة الاحتفاظ |
| Necessity | The measure is genuinely required to achieve the aim | الضرورة |
| Proportionality | The interference is no greater than the aim requires | التناسب |
| Fundamental rights | Basic protected rights of the individual | الحقوق الأساسية |
| Impact assessment | A documented assessment of risks before deployment | تقييم الأثر |
| Human oversight | A competent person able to review and override | الإشراف البشري |
| Automated decision | A decision made by a system without human involvement | القرار الآلي |
| Redress | The route by which a person challenges a decision | الانتصاف |
| Accountability | Being able to demonstrate compliance, not merely achieve it | المساءلة |
| Transparency | The affected person can find out what happened and why | الشفافية |
| Supervisory authority | The independent body that oversees and can sanction | السلطة الرقابية |
| Profiling | Automated evaluation of personal aspects of an individual | التنميط |
| High-risk system | A category carrying a defined set of obligations | نظام عالي المخاطر |
| Prohibited practice | A use that is not permitted at all | ممارسة محظورة |
| Discrimination | Unjustified differential treatment of a group | التمييز |
| Logging / audit trail | A record allowing a decision to be reconstructed later | سجل التتبّع |
| Anonymisation | Rendering data no longer attributable to a person | إخفاء الهوية |
| Pseudonymisation | Replacing identifiers so re-identification needs extra information | الترميز |
| Law enforcement | Prevention, investigation and prosecution of offences | إنفاذ القانون |
| Suspect / witness / victim | Categories of person that must be kept distinct in records | مشتبه به / شاهد / ضحية |

## Ambiguities the interpreter should watch

These cause real confusion in bilingual technical delivery. Agree a handling for each before Day 1.

1. **Precision and accuracy.** Both are commonly rendered as الدقة. They are different measures and Day 2 contrasts them directly. Agree two distinct terms, or keep the English words and define them once.
2. **Cluster.** Day 2 means a group of similar observations; Day 5 means a group of machines. Different words are needed.
3. **Model.** A statistical model, not a business model and not a model of behaviour.
4. **Training.** Training a model, not training people — in a training course, this collides constantly.
5. **Sample.** A statistical sample, not a product sample.
6. **Row.** A row of a table, not a row of seats in the classroom.
7. **Significant.** Avoid entirely unless discussing statistical significance, which this course does not.
8. **Validation.** Choosing between models, distinct from final testing and from data validation in the quality sense.
9. **Assessment.** Three different things this week: evaluating a model, an impact assessment document, and a personal assessment recorded about someone. The third is the one European law insists is kept separate from fact. Agree three distinct terms.
10. **Risk.** Statistical risk, legal risk to the organisation, and risk to a person's rights are not the same, and the European material moves between them. Do not let one word carry all three.
11. **Bias.** Statistical bias (a systematic error) and discriminatory bias (unjustified treatment of a group) are different ideas that share an English word, and Day 2 uses both.

Spell out **NLP**, **MAE**, **MCMC**, **PCA**, **GAN** and **ARIMA** in full the first time each is used on each day.
