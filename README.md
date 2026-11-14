# wordle

A command-line implementation of the Wordle word game in Python. The secret word is picked at random from a Microsoft SQL Server table that is filled from `words.csv`.

## Features

- Six attempts to guess a five-letter word.
- After each guess, a five-character feedback string is printed:
  - `o` – correct letter in the correct position
  - `z` – letter is in the word but in a different position
  - `x` – letter is not in the word
- Handles words with repeated letters.
- At the end, prints a summary (`Wordle n/6`), the feedback rows and the secret word.
- Word list of 15,918 five-letter words in `words.csv`.

## Project structure

| File | Description |
|------|-------------|
| `wordle.py` | Game logic, database connection and score printing |
| `words.csv` | Word list (single `words` column) used to populate the database |

## Getting started

### Requirements

- Python 3
- `pandas`, `numpy` and `pyodbc`
- Microsoft SQL Server with the Windows "SQL Server" ODBC driver

```bash
pip install pandas numpy pyodbc
```

### Database setup

`wordle.py` connects to the `master` database on a server named `MARIAM` using Windows authentication (`Trusted_Connection=yes`). Change the `SERVER=` value in the connection string to match your machine.

The game reads from a table called `words`. The code that creates this table and inserts the rows from `words.csv` is included in `wordle.py` but commented out. Uncomment the `CREATE TABLE` and insert blocks for the first run, then comment them out again.

### Run

```bash
python wordle.py
```

Note: the script currently prints the secret word when a game starts (useful for debugging).

## Tech

Python, pandas, pyodbc, Microsoft SQL Server (T-SQL `NEWID()` for random selection).

## License

Apache License 2.0 – see [LICENSE](LICENSE).
