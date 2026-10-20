---
name: r-data-handling
description: General rules for reading, checking, cleaning and saving fisheries data in R.
status: draft
---
# r-data-handling

General conventions written by the developers, not derived from brain citations. Review before marking `status: reviewed`.

## Principles
- Raw data is read-only. Scripts read from `data/raw/` and write to `data/clean/`; never overwrite the input.
- Every cleaning step is code, in order, with a count of rows affected (`message()` or a log table). No manual spreadsheet edits.
- Keep one tidy table per observation unit (one row per capture, per net set, per fish) with consistent snake_case column names.

## Workflow in R
1. Read with explicit types (`readr::read_csv(col_types = ...)` or `read.csv(colClasses = ...)`); check `problems()` or warnings.
2. Parse dates once, with an explicit format and time zone; flag unparseable dates, do not drop them.
3. Standardize codes (species, gear, site, sex) with a lookup table; list values that match nothing.
4. Check: duplicates on the natural key, impossible values (negative or zero length/weight, future dates), length-weight outliers, missing effort.
5. Treat zeros deliberately: a zero catch needs a recorded effort row; absent rows are not zeros.
6. Write the clean file and a cleaning log (what was changed, counts, assumptions). Then produce the data summary (`utils/data_summary.py`).

## Packages
Base R, `readr`, `dplyr`, `tidyr`, `lubridate` are common choices; confirm availability with `check_r_package` and ask before installing.
