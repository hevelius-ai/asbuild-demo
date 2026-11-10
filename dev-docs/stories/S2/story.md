# S2: count lines

## Request (the owner's words, unchanged)

I'd like the app to tell me how many lines a text file has. When I give it a file name it should show the number of lines, and a empty file should show 0 lines.

## Criteria

| ID | Criterion | Cites |
| --- | --- | --- |
| S2-C1 | Given the name of a text file with three lines, the app shows `lines: 3`. | Request, sentence 2 |
| S2-C2 | Given the name of an empty file, the app shows `lines: 0`. | Request, sentence 2 |

## Plain checklist (approved by the owner; the receipt quotes it word for word)

| ID | plain: | Examples (approved) |
| --- | --- | --- |
| S2-C1 | When you give the app the name of a text file, it shows how many lines the file has. | `lines: 3` |
| S2-C2 | When the file is empty, the app shows 0 lines. | `lines: 0` |

## Not in this story

The request does not say what happens for a missing file, a last line without a line break, or very large files. The build will use the app's existing behaviour for a missing file and count a last line without a line break as a line. The command is `python -m app lines <file name>`.
