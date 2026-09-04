def extract_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

if __name__ == "__main__":
    result = extract_text("test.txt") 
    print(result)