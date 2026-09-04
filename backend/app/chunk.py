def chunk_text(text):
    words = text.split()
    results = []
    chunk_size = 500
    step = 450
    for start in range(0, len(words), step):
        chunk_words = words[start : start + chunk_size]
        chunk_string = " ".join(chunk_words)
        results.append(chunk_string)
    return results

if __name__ == "__main__":
    sample_text = "word " * 1200  # fake a 1200-word document
    chunks = chunk_text(sample_text)
    print(f"Number of chunks: {len(chunks)}")
    for i, c in enumerate(chunks):
        print(f"Chunk {i}: {len(c.split())} words")