# RegEx Quiz

## Introduction

## Design

### GUI Design

<img width="1102" height="903" alt="Wireframe" src="https://github.com/user-attachments/assets/b3af7a21-2eab-4fba-b37a-155b6343ef94" />

**Figure 1:** Wireframe


### Functional and Non-functional requirements

#### Functional Requirements

#### Non-functional Requirements

#### Tech Stack Outline

#### Code Design

<img width="583" height="1056" alt="image" src="https://github.com/user-attachments/assets/5510f45c-9199-41a9-a0da-0c0350b571d4" />

**Figure 2:** Class diagram


## Development

## Testing

#### 📋 Manual Testing Table for Tkinter RegEx Quiz App

| **Test Case ID** | **Functionality**                      | **Test Description**                                                                   | **Expected Result (with UI Behaviour Notes)**                                                                            | **Actual Result** | **Pass/Fail** |
| ---------------- | -------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------- | ------------- |
| **1**            | App Launch & Window                    | Launch the app and verify window title and size.                                       | **Window titled “RegEx Knowledge Quiz” opens.** UI loads without delay. Window is centred and responsive; no flickering. |                   |               |
| **2**            | Login UI Elements                      | Verify login screen shows app title, username label, entry, and **Start Quiz** button. | Title is bold and centred; username prompt visible; Entry widget accepts typing; Start button fully clickable.           |                   |               |
| **3**            | Username Validation – Valid            | Enter `DevUser23` and click **Start Quiz**.                                            | Login frame disappears; first question screen fades in instantly; no warning dialogs.                                    |                   |               |
| **4**            | Username Validation – Too Short        | Enter `Jo` and click **Start Quiz**.                                                   | Error dialog appears in focus; background UI is disabled; dialog must be dismissed before retrying.                      |                   |               |
| **5**            | Username Validation – Too Long         | Enter a username >15 chars.                                                            | Same validation error dialog; input box is highlighted or unchanged (but still interactive).                             |                   |               |
| **6**            | Username Validation – Non‑alphanumeric | Enter `User!@#` and click Start.                                                       | Error dialog appears; form remains interactive; no crash, freeze, or partial UI update.                                  |                   |               |
| **7**            | Questions Load – Happy Path            | Start quiz with a valid `questions.csv`.                                               | First question displays; text is readable; 4 radio options appear vertically; **Next** button aligned below them.        |                   |               |
| **8**            | Questions Load – Missing File          | Rename/remove `questions.csv` and start app.                                           | App loads dummy “file missing” question; options show N/A; UI still fully functional; no crash.                          |                   |               |
| **9**            | Questions Load – Bad Columns           | Use CSV missing a required column.                                                     | App should display console warning; UI may show malformed questions but must not crash.                                  |                   |               |
| **10**           | Question Counter                       | View counter label on first question.                                                  | Label shows “Question 1/N”; increments by 1 each time **Next** is used; always accurate.                                 |                   |               |
| **11**           | No Selection Warning                   | Press **Next** without selecting an answer.                                            | Warning dialog appears; dialog must be acknowledged; user stays on same question.                                        |                   |               |
| **12**           | Selecting an Answer                    | Select correct answer and click **Next**.                                              | Score increments; next question displays immediately; selection resets to empty.                                         |                   |               |
| **13**           | Incorrect Answer                       | Select incorrect answer and continue.                                                  | No score increment; next question loads normally.                                                                        |                   |               |
| **14**           | Options Behavior                       | Verify radio button behavior.                                                          | Only one option can be selected at a time; selecting a new one deselects previous.                                       |                   |               |
| **15**           | Navigation – End of Quiz               | Finish final question.                                                                 | Completion dialog appears: “Quiz Complete! Score: X\nResults saved.” App closes cleanly after clicking OK.               |                   |               |
| **16**           | Results Export – File Creation         | Complete a full quiz session.                                                          | `results.csv` is created if missing; no secondary files generated; no errors.                                            |                   |               |
| **17**           | Results Export – Row Content           | Inspect last row of results file.                                                      | Contains `username`, `score`, and timestamp in `DD/MM/YYYY HH:MM`. No missing fields.                                    |                   |               |
| **18**           | Results Export – Append Behavior       | Complete quiz twice.                                                                   | Results file contains separate rows for each run; rows do not overwrite each other.                                      |                   |               |
| **19**           | Styling – Theme Application            | Observe overall styling.                                                               | `clam` theme active; buttons have hover darkening; radio buttons and labels follow Segoe UI fonts.                       |                   |               |
| **20**           | Text Wrapping & Readability            | Use long question text.                                                                | Text wraps around 500 px width; no overflow; layout remains aligned and readable.                                        |                   |               |
| **21**           | Accessibility – Keyboard               | Navigate using keyboard.                                                               | Arrow keys switch radio options; Enter triggers **Next** when focused; UI updates smoothly.                              |                   |               |
| **22**           | Robustness – Regex Characters          | Use questions with symbols like `^\d+$`.                                               | UI displays symbols correctly without escaping issues or formatting breakage.                                            |                   |               |
| **23**           | Robustness – Blank CSV Rows            | Add a blank line at end of CSV.                                                        | Loader ignores or handles blank row gracefully; no crash on quiz start.                                                  |                   |               |
| **24**           | Progress Across Questions              | Move through full quiz.                                                                | Counter increments smoothly; no duplicated questions; transitions have no lag.                                           |                   |               |
| **25**           | Cleanup on Exit                        | Let app finish or close manually.                                                      | Window closes fully; python process ends; no ghost Tk windows remain.                                                    |                   |               |



## Documentation

## Evaluation
