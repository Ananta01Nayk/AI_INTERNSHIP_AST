# AI Code Intelligence Tool  

## What this project does

This project is a simple **AI code intelligence tool** that analyzes a Python codebase and extracts:

- Functions
- Classes
- Variables
- Source code of each function and class
- The file in which each entity is defined

The goal is to help understand large and unfamiliar legacy codebases by converting raw source code into **structured, readable information**.

## How it works

1. Scans all `.py` files in a target directory  
2. Parses code using Python AST  
3. Extracts entities and their source  
4. Saves results into `entities.json`  
5. Displays them in a web dashboard  

## How to run

Activate environment:
```
my_venv\Scripts\activate
```

Run analyzer:
```
python src/analyzer.py
```

Start dashboard:
```
cd src
uvicorn show_output:app --reload
```

Open in browser:
```
http://127.0.0.1:8000
```

## What I learned

- How to analyze real enterprise code
- How AST works
- How code intelligence tools are built

## Author

Ananta Nayak
