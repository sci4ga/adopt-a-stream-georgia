# Exported dataset

The raw export sent from AaS-GA is the file "AAS_Chemical_Data_12202021.xlsx - Sheet1.csv".

It has been processed so far in two stages, resulting in the files "export_dataframe_stage1.csv" and similarly for #2. These files are provided via git's Large File System. If bandwidth has been exceeded for the month, the "large" data files (the largest are just a few MB) are mirrored on [GDrive](https://drive.google.com/drive/folders/1czjUCDzNSZo3kzIlp4ET4kRqLhmnNm2j) and at [Sci4Ga](<tbd>), and the stages can be reproduced by running the notebooks.

## Data dictionary

This work was begun by students of the Emory Data Science Club (EDSC) in Spring, 2022. It is based on the lightly-prepped data recorded as the output of "stage 2". The work plan is summarized [here](https://docs.google.com/document/d/1hYmoadOKfQp2WeefrYxM4qdam5gv6LI61Gf_4WYRaLQ/edit#).

The data dictionary can always be improved. Please submit a PR!

### Goals

The data dictionary is intended to provide context about the data and improve the accuracy of analyses by clarifying its trustworthy use.

There are two data dictionary files in the form of computational notebooks, one in python and one in R.

## Enablement

This work builds on the data dictionaries and looks for deeper patterns in the data that might indicate errors, inconsistencies, and other issues. Here is an introductory [presentation](https://docs.google.com/presentation/d/1QKZtmtNVaXTy71amFAhivt1yFn9nrD_rjOzWxtyrwVU/edit) about data enablement and how it relates to Adopt-a-Stream in Georgia, and a [general-purpose checklist for helping data projects have impact](https://docs.google.com/document/d/1_DuzNIHcsv1lIF0586P9CmUuLfMO8uWQDZPsYv5AfJk/edit).

Examples for this particular dataset are provided in the student presentations:

 * "How much do you trust your dataset?"
   * [GDrive](https://docs.google.com/presentation/d/1fK-stxOf-rVTpWozLHjKywHbQ-kbp9SmOXoYQ4We3jE/edit?usp=sharing) and [Sci4Ga]() PDF mirror.
   * Work by Ginger Lau, Audrey Bu, Ivan Chang.

 * "Exploring errors in adopt-a-stream quantitative data"
   * [GDrive](https://docs.google.com/presentation/d/1fK-stxOf-rVTpWozLHjKywHbQ-kbp9SmOXoYQ4We3jE) and [Sci4Ga]() PDF mirror.
   * Work by Victoria Ontiveros.
