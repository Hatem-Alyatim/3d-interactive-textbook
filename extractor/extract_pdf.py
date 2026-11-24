import fitz  # PyMuPDF
import json
import sys
from pathlib import Path

def extract_textbook_to_json(pdf_path: str, output_json: str):
    doc = fitz.open(pdf_path)
    lessons = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text").strip()
        if not text:
            continue

        lines = [line.strip() for line in text.splitlines() if line.strip()]
        title = lines[0] if lines else f"Lesson {page_num + 1}"
        body = " ".join(lines[1:])[:800]  # Extract clean summary

        lessons.append({
            "page": page_num + 1,
            "title": title,
            "description": body,
            "model_type": "procedural_3d"
        })

    Path(output_json).parent.mkdir(parents=True, exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Extracted {len(lessons)} pages into {output_json}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <path_to_textbook.pdf>")
        sys.exit(1)
    extract_textbook_to_json(sys.argv[1], "../data/extracted_lessons.json")