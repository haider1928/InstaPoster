def add_newlines(text, interval):
    # Split the text into chunks of the specified interval
    chunks = [text[i:i+interval] for i in range(0, len(text), interval)]
    # Join the chunks with '\n'
    return '-\n\n'.join(chunks)