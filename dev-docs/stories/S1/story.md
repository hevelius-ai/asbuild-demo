# S1: Count words

## Request (the owner's words, unchanged)

I want the app to count the words in a text file. When I give it a file name, it should tell me how many words the file has. If the file doesn't exist, it should tell me that instead of crashing.

## Criteria

| ID | Criterion | Cites |
| --- | --- | --- |
| S1-C1 | `python -m app count <file>` prints `words: <n>` as its last line and exits 0, where n is the number of words separated by whitespace | Request, sentence 2 |
| S1-C2 | For a file that does not exist, `python -m app count <file>` exits 2 and its error output contains "no such file" | Request, sentence 3 |

## Plain checklist (approved by the owner; the receipt quotes it word for word)

| ID | plain: |
| --- | --- |
| S1-C1 | When you name a text file, the app shows how many words it has, like "words: 3". |
| S1-C2 | If the file you name doesn't exist, the app tells you so instead of crashing. |
