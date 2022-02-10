phone_book = ["12","123","1235","567","88"]


class node:
    def __init__(self):
        self.n = {}
        self.answer = True

    def put(self, word):
        cur_n = self.n
        for i, alphabet in enumerate(word):
            if alphabet not in cur_n:
                if '!' in cur_n.keys():
                    self.answer = False
                    break
                cur_n[alphabet] = {}
            cur_n = cur_n[alphabet]
        if cur_n != {}:
            self.answer = False
        else:
            cur_n['!'] = word


def solution(phone_book):
    root = node()
    for name in phone_book:
        root.put(name)
        if not root.answer:
            return False

    return True

print(solution(phone_book))