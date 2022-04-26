# Design an iterator that supports the peek operation on an existing iterator in addition to the hasNext and the next operations.
#
# Implement the PeekingIterator class:
#
# PeekingIterator(Iterator<int> nums) Initializes the object with the given integer iterator iterator.
# int next() Returns the next element in the array and moves the pointer to the next element.
# boolean hasNext() Returns true if there are still elements in the array.
# int peek() Returns the next element in the array without moving the pointer.

# First Trial

class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator

    def peek(self):
        clone = copy.deepcopy(self.iter)
        return clone.next()

    def next(self):
        return self.iter.next()

    def hasNext(self):
        return self.iter.hasNext()

# iterator 객체 안의 list 값 조회가 불가능하기에 peek 구현하기 위해 deepcopy하는 방법을 생각.
# 객체를 그대로 복사하고 불러오기에 런타임과 메모리 모두 비효율

# Runtime: 102 ms, faster than 5.09% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.2 MB, less than 29.71% of Python3 online submissions for Peeking Iterator.


# Second Trial

class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.cur = None
        self.pop_next()

    def pop_next(self):
        self.cur = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.cur

    def next(self):
        result = self.cur
        self.pop_next()
        return result

    def hasNext(self):
        if self.cur:
            return True
        else:
            return False


# peek 구현을 위해 값을 미리 꺼내놓은 cur 변수와 꺼내놓는 함수 pop_next 구현. 속도를 1/3 수준으로 줄이게 됨.
# Runtime: 32 ms, faster than 90.40% of Python3 online submissions for Peeking Iterator.
# Memory Usage: 14.2 MB, less than 29.71% of Python3 online submissions for Peeking Iterator.

