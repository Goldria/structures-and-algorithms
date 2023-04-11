def generate_skip_table(pattern):
    pat_len = len(pattern)
    skip_table = {ch: max(1, pat_len - ind - 1)
                  for ind, ch in enumerate(pattern)}
    return skip_table


def print_text_with_idx(text):
    [print(str(ind).ljust(3), end=" ") for ind in range(len(text))]
    print()
    [print(str(ch).ljust(3), end=" ") for ch in text]
    print()


def bm_search(text, pattern):
    skip_table = generate_skip_table(pattern)
    pat_len = len(pattern)
    cur_idx = pat_len - 1
    answer = []
    while cur_idx <= len(text) - 1:
        found = True
        for i in range(pat_len-1, -1, -1):
            if pattern[i] != text[cur_idx - pat_len + i + 1]:
                shift = skip_table.get(
                    text[cur_idx - pat_len + i + 1], pat_len)
                cur_idx += shift
                found = False
                break
        if found:
            answer.append(cur_idx - pat_len + 1)
            cur_idx += pat_len
    return answer


def main():
    text = str(input(("Введите строку: ")))
    word = input("Введите слово для поиска: ")

    print_text_with_idx(text)
    print(bm_search(text, word))


if __name__ == '__main__':
    main()
