# Conversational workshop update

Prepared against repository commit `9a57450def87e66b6229d65b07cf46716b637fcc`.

## The current audience

Participants already analyse data and use Python. The course is a guided practical workshop, with prepared notebooks and selected experiments. The paper-only route remains a contingency. Public-service analogies concern appointments, service capacity, facilities, request routing and quality inspection; existing notebook data remain explicitly synthetic.

## Start here

- `instructor/TUTOR_SCRIPT.md`: one English document containing the tutor's planned explanations, questions, activity instructions, expected responses, recovery lines and closing for all five days. Around 8,200 words, with interpretation and practical-work blocks rather than continuous lecturing.
- `dist/participant-handbook.pdf`: 28-page participant edition with coloured charts, diagrams, exercises and writing space.
- `participant/HANDBOOK.md`: the same core content in Markdown.
- `participant/HANDBOOK_TECHNICAL_REFERENCE.md`: the earlier detailed handbook, preserved for reference.
- `PROGRAMME.md`: the conversational programme for the confirmed audience.

## Rebuild

```bash
python -m pip install -r requirements-handbook.txt
python scripts/build_visual_handbook.py
python scripts/build_participant_handbook.py
```

Edit `participant/handbook_content.json` for the participant edition. The visual builder regenerates its Markdown, PDF and chart assets. The HTML builder embeds the images and includes the reference appendices. The tutor script is edited directly.

## Review completed

All 28 PDF pages were rendered and visually reviewed, with full-size checks of dense charts. Text bounds stay within each page. Schedule totals, selected calculations, posterior tail probability, HTML image embedding and internal anchors were checked. The handbook's text and PDF are generated from the same content source.

Original notebook code and PPTX files were not changed or rerun. Existing slide review tasks remain open. A licensed real-data activity remains open. Classroom timing and interpretation need rehearsal. INE and datos.gob.es are cited as documented reference points; the proposed working routine is not presented as universal European practice.

## Applying a downloaded update archive

The archive contains changed and new files, not a complete clone. Open a fresh checkout of the repository, compare its current version with the baseline above, then copy the reviewed files into matching paths. Preserve any later changes made by others. Commit the result after review. The archive does not include authentication information and does not change repository history by itself.
