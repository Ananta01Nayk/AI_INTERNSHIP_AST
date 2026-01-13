import os
import ast
import json

TARGET_DIR = r"D:\ananta\AI_engineer_Intership\Day2\samples"
OUTPUT_FILE = "entities.json"

entities = {
    "functions": {},
    "classes": {},
    "variables": {}
}


class Analyzer(ast.NodeVisitor):
    def __init__(self, filename, code):
        self.filename = filename
        self.lines = code.splitlines()

    def visit_FunctionDef(self, node):
        start = node.lineno - 1
        end = node.end_lineno
        code = "\n".join(self.lines[start:end])

        key = f"{self.filename}::{node.name}"

        entities["functions"][key] = {
            "name": node.name,
            "file": self.filename,
            "function_code": code
        }

        self.generic_visit(node)

    def visit_ClassDef(self, node):
        start = node.lineno - 1
        end = node.end_lineno
        code = "\n".join(self.lines[start:end])

        key = f"{self.filename}::{node.name}"

        entities["classes"][key] = {
            "name": node.name,
            "file": self.filename,
            "class_code": code
        }

        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                key = f"{self.filename}::{target.id}"

                entities["variables"][key] = {
                    "name": target.id,
                    "file": self.filename
                }

        self.generic_visit(node)


def scan():
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        code = f.read()

                    tree = ast.parse(code)
                    Analyzer(path, code).visit(tree)

                except Exception as e:
                    print("error parsing:", path, e)


if __name__ == "__main__":
    scan()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entities, f, indent=2)

    print("analysis complete. entities.json generated.")
