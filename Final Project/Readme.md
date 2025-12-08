Technical Documentation
Journey to the Mysterious Island
1. Where the Code Is Hosted
All project files are stored locally in the following structure:
- Chpt1.py (Chapter 1 logic)
- Chpt2.py (Chapter 2 logic)
- Chpt3.py (Chapter 3 logic)
- Chpt4.py (Chapter 4 logic)
- Chpt5.py (Chapter 5 logic)
- main.py (Main driver program)
- utils.py (Utility functions)

2. External Services
This program does not use any external services, APIs, web servers, or databases. It runs fully offline using standard Python libraries only.
3. Languages and Technologies Used
Programming Language: Python 3
Paradigm: Modular procedural design
Technologies:
- Input/output handling
- State dictionary for story progression
- Modular chapter-based architecture

4. System Requirements and Supported Applications
Minimum Requirements:
- Python 3.8 or higher
- Terminal or command-line interface
Supported Platforms:
- Windows, macOS, Linux

5. Coding and Naming Conventions
Files follow a modular structure for each chapter.
Functions use lowercase_with_underscores.
Shared game state is handled through a dictionary named 'state'.

6. How to Run / Build / Deploy the Program
To run the program:
1. Install Python
2. Open a terminal in the project folder
3. Run: python main.py
No build or deployment steps are required.
7. Overview of the Architecture
The project uses a chapter‑based modular architecture.
- main.py controls flow using checkpoint labels.
- Each chapter has a play(state) function.
- utils.py provides shared functions such as banner(), prompt_choice(), checkpoint(), restart_chapter().

8. How to Start the Program
Run: python main.py
Player enters their name.
Game begins at Chapter 1.
Checkpoints route the story until the successful ending.

