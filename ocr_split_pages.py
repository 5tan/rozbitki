import fitz

pdf = fitz.open("Rozbitki albo Dwudziestomiesięczny pobyt na Wyspach.pdf")

with open("ocr_split_pages.txt", "w", encoding="utf-8") as f:
    for page_num, page in enumerate(pdf, start=1):
        f.write(f"<!-- page {page_num} -->\n\n")
        f.write(page.get_text())
        f.write("\n\n")