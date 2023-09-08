with open('test.txt', 'r') as reader:  # close automatically. No need to xxx.close()
    content = reader.readlines()  # [avc, bd, "cat", dog, elephant] after elephant /n
    reversed(content)  # [elephant, dog, "cat", bd, avc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
