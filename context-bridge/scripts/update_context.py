import argparse
import os
import re
from datetime import datetime

SHARED_FILE_NAME = "PROJECTS_SHARED_CONTEXT.md"
# Assuming script is run from project root, and shared file is in parent dir
# Adjust as needed if structure differs.
SHARED_FILE_PATH = os.path.abspath(os.path.join(os.getcwd(), "..", SHARED_FILE_NAME))

def get_header(project_name):
    return f"## {project_name} Context"

def create_initial_file():
    content = f"# Shared Project Context\n\n{get_header('World-Building')}\n\n{get_header('Unity')}\n"
    with open(SHARED_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created new shared context file at: {SHARED_FILE_PATH}")

def update_context(project_name, new_content):
    if not os.path.exists(SHARED_FILE_PATH):
        create_initial_file()

    with open(SHARED_FILE_PATH, 'r', encoding='utf-8') as f:
        file_content = f.read()

    header = get_header(project_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_content = f"{header}\n[Last Updated: {timestamp}]\n\n{new_content.strip()}\n"

    # Regex to find the section for this project
    # Looks for the specific header, then captures everything until the next header (## ) or end of file
    pattern = re.compile(f"({re.escape(header)}).*?(?=\n## |$)", re.DOTALL)

    if pattern.search(file_content):
        updated_file_content = pattern.sub(formatted_content.strip(), file_content)
    else:
        # If section doesn't exist (e.g. file was manually edited), append it
        updated_file_content = file_content.strip() + "\n\n" + formatted_content

    with open(SHARED_FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(updated_file_content)
    
    print(f"Successfully updated context for '{project_name}'.")

def main():
    parser = argparse.ArgumentParser(description="Update shared project context.")
    parser.add_argument("--project", required=True, help="Project name (e.g., World-Building, Unity)")
    parser.add_argument("--content", help="Content to update. If not provided, reads from stdin.")
    
    args = parser.parse_args()
    
    content = args.content
    if not content:
        import sys
        print("Enter content (Ctrl+Z then Enter to finish):")
        content = sys.stdin.read()

    if not content:
        print("Error: No content provided.")
        return

    update_context(args.project, content)

if __name__ == "__main__":
    main()
