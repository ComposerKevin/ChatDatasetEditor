# JSONL Editor - In-Browser JSONL File Editor

Screenshot of JSONL Editor
![Screenshot](https://github.com/ComposerKevin/ChatDatasetEditor/blob/main/screenshot.png?raw=true "Screenshot")

# Description

This project is a simple, in-browser JSONL (JSON Lines) file editor built using Python Flask for the backend and pure HTML/CSS/JavaScript for the frontend. It provides a user-friendly graphical interface to view and modify JSONL files directly in your web browser, without relying on any external JavaScript dependencies or frameworks.

Each line in the JSONL file is treated as a standalone JSON object, typically structured as:
```json
{"messages":[{"role":"system","content":"...text..."}]}
```

The editor features pagination, allowing you to navigate through each JSON object as a separate page.

# Features

- File Listing:
* Displays a list of .jsonl files from the jsonl_files directory on the server.
- Load and Edit:
* Select a file from the list to load its content into the editor.
* Each {"messages"} object is presented as a separate page.
* Edit "role" and "content" for each message within a JSON object.
- Pagination:
* Navigate through JSON objects using "PREV" and "NEXT" buttons.
* Jump to specific pages using a dropdown menu.
* Displays current page number and total page count.
- Add/Remove Objects and Messages:
* Add new JSON objects to the file.
* Remove existing JSON objects.
* Add new messages to a JSON object.
* Remove individual messages from a JSON object.
- Create New File:
* Create new, empty .jsonl files directly from the browser interface.
- Clone File:
* Clone existing .jsonl files to create copies with new filenames.
- Save Changes:
* Save modifications back to the selected .jsonl file on the server.
- Professional GUI:
* User-friendly and clean interface with proper button styling and layout, designed for usability.
- No External Dependencies:
* Built without any external JavaScript libraries or CSS frameworks, keeping it lightweight and simple.

# How to Use

Setup:
* Ensure you have Python and Flask installed (pip install Flask).
* Save the app.py, index.html, and style.css files in the same directory structure as intended (create templates and static folders if needed).
* Create a folder named jsonl_files in the same directory as app.py to store your JSONL files.

Run the Application:
* Open your terminal, navigate to the project directory, and run python app.py.
* Access the editor in your web browser by going to the address provided in the terminal (usually http://127.0.0.1:5000/).

Using the Editor:
* File Selection: The initial view shows a list of .jsonl files in the jsonl_files directory.
* Create New File: Click "Create New File" to create a new, empty JSONL file. You will be prompted for a filename (must end with .jsonl).
* Load File: Click on a filename in the list to load its content into the editor.
* Clone File: Click on the "(clone)" link next to a filename in the list to create a copy of that file. You will be prompted for a new filename for the clone.
* Navigate Pages: Once a file is loaded, use the "*lt; PREV", "NEXT >" buttons or the page dropdown to navigate between JSON objects.
* Edit Content: Modify the "Role" and "Content" fields for each message in the currently displayed JSON object.
* Add/Remove Messages: Use the "Add Message" and "Remove Message" buttons within each JSON object to manage messages.
* Add/Remove Objects: Use the "Add JSON Object" and "Remove JSON Object" buttons at the bottom of the editor to manage JSON objects (pages).
* Save: Click "Save" to save your changes to the current file.
* Back to File List: Click "Back to File List" to return to the file selection screen.
# License

This project is licensed under the GNU Lesser General Public License v3.0.

# Screenshot

A screenshot of the JSONL Editor interface is available in the file screenshot.png in the project's root directory. It provides a visual overview of the editor in action.
