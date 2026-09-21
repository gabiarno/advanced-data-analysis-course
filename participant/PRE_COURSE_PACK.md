# Before the course — participant pack

Send this as early as possible before Day 1, with the entry diagnostic attached.

---

## Welcome

You are booked on **Advanced Data Analysis Techniques**, five days in Genoa. Sessions run for five hours each day with two breaks. Delivery is in English with Arabic interpretation throughout.

We understand you already work with Python and analyse data as part of your role. The course is pitched accordingly: we will not spend time on syntax or on a first introduction to modelling. You will read and modify working code from the first hour, and the time goes into method choice, evaluation design and judgement.

Every exercise is drawn from public administration — service-centre demand, inspection scheduling, emergency call volume, records quality, road safety — so you should not have to translate a retail example into your own work.

We have also been told you want to see how this work is done in Europe. That runs through all five days: which rules apply to what, the principles that shape how European public bodies design an analytics project, and two European systems that went badly wrong and changed the law as a result.

There are three things to do before Day 1.

## 1. Set up your laptop and confirm it runs

**Please arrive with the software installed and tested.** Installing in the first session costs everyone an hour.

You need:

- A laptop you can install software on, with at least 4 GB of free disk space.
- **Python 3.12** — from [python.org](https://www.python.org/downloads/).
- The course materials, sent to you as a download link.

Open a terminal in the course folder:

```
python -m venv .venv
```

Activate it — macOS or Linux `source .venv/bin/activate`, Windows PowerShell `.venv\Scripts\Activate.ps1` — then:

```
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open `day-01-eda/worked.ipynb` and run all cells. If it completes without error, you are ready. **Please reply to confirm it ran**, or send us the error — either answer is useful, and both are much easier to deal with now than on Monday morning.

If you would like to attempt the optional Spark lab on Day 5, that needs Java 17 and a separate install; instructions are in `SETUP.md`. It is genuinely optional and there is a prepared alternative.

### If your laptop is locked down

Some official laptops block installation. Tell us in advance and we will arrange a prepared environment or a shared machine. There is also a complete paper route through every activity, so **nobody is excluded from anything** — but we need to know beforehand.

## 2. Complete the diagnostic

Twelve questions, about twelve minutes. **It is not scored against you and no individual result is shared with anyone.** It tells us where to pitch the week.

It is deliberately not easy. Several questions have no single right answer and ask what you would do. Answer honestly, including "I don't know" — a diagnostic everyone passes tells us nothing and wastes your week.

## 3. Bring a problem

On Day 1 you choose a problem to work on across the week, and on Day 5 you present a one-page recommendation on it.

The best choice is a real question from your own work — ideally a decision made on judgement today, or one where you suspect the current method has never been properly checked.

**Bring the problem, not the data.** Describe it in general terms. Nothing confidential is needed and no data of yours is uploaded anywhere. Supplied scenarios are available if you prefer.

Think about: *What decision would this support? Who makes that decision? How is it made today?*

One framing note that will save you time. The exercises all concern allocating resources — which locations, which times, which rounds, which process steps — rather than scoring individuals. European practice treats those two very differently, and we spend real time on why. If your problem is about individuals, still bring it: there is almost always a resource-shaped version of the same question, and finding it together is one of the more useful hours of the week.

## What to expect

| | |
|---|---|
| Level | Working analyst. Method choice and evaluation, not syntax |
| Pace | Concept, short demonstration, then you work. Interpretation time is built in |
| Format | Pairs — one drives the keyboard, one checks and writes the finding. Roles swap |
| Data | Synthetic, generated for teaching. Nothing confidential or personal |
| Materials | A printed handbook on Day 1, plus all notebooks to keep |
| Assessment | Daily questions, a capstone and a short final exercise. Formative, to help you learn |

## What you do not need

- A powerful laptop, a GPU or a cloud account.
- An internet connection during the sessions — everything runs offline once installed.
- Prior experience of machine learning specifically.
- Legal expertise. The European material is a framework and its reasoning, not legal training.

## Questions

Contact your course organiser. Setup problems in particular are far easier to fix the week before than on Monday morning.

We look forward to meeting you.
