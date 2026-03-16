def chunk_code(code, chunk_size=500):
    chunks = []
    start = 0

    while start < len(code):
        end = start + chunk_size
        chunks.append(code[start:end])
        start = end

    return chunks