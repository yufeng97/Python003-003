# 示例代码
import threading
import queue
import time
import random


class DiningPhilosophers(threading.Thread):
    # philosopher 哲学家的编号。
    # pickLeftFork 和 pickRightFork 表示拿起左边或右边的叉子。
    # eat 表示吃面。
    # putLeftFork 和 putRightFork 表示放下左边或右边的叉子。
    def __init__(self, index, limit, leftLock, rightLock, record):
        super().__init__()
        self.index = index
        self.limit = limit
        self.leftFork = leftLock
        self.rightFork = rightLock
        self.record = record
        self.eatTimes = 0

    def eat(self):
        if self.leftFork.is_free and self.rightFork.is_free:
            self.pickLeftFork()
            self.pickRightFork()
            print("{}号哲学家正在进食".format(self.index))
            self.eatTimes += 1
            time.sleep(random.random())
            self.record.put([self.index, 0, 3])
            self.putLeftFork()
            self.putRightFork()

    def think(self):
        print("{}号哲学家正在思考".format(self.index))
        time.sleep(random.random())
        # print("{}号哲学家结束思考".format(self.index))

    def pickLeftFork(self):
        print("{}号哲学家拿起左边的叉子".format(self.index))
        self.leftFork.pickup()
        self.record.put([self.index, 1, 1])

    def pickRightFork(self):
        print("{}号哲学家拿起右边的叉子".format(self.index))
        self.rightFork.pickup()
        self.record.put([self.index, 2, 1])

    def putLeftFork(self):
        print("{}号哲学家放下左边的叉子".format(self.index))
        self.leftFork.putdown()
        self.record.put([self.index, 1, 2])

    def putRightFork(self):
        print("{}号哲学家放下右边的叉子".format(self.index))
        self.rightFork.putdown()
        self.record.put([self.index, 2, 2])

    def run(self):
        while self.eatTimes < self.limit:
            self.think()
            self.eat()


class Fork:
    def __init__(self, index):
        self.index = index
        self._lock = threading.Lock()
        self.is_free = True

    def pickup(self):
        self._lock.acquire()
        self.is_free = False

    def putdown(self):
        self._lock.release()
        self.is_free = True


if __name__ == "__main__":
    records = queue.Queue()
    limit = 1
    forks = [Fork(i) for i in range(5)]
    philosophers = [DiningPhilosophers(i, limit, forks[(i-1)%5], forks[i%5], records) for i in range(5)]
    for p in philosophers:
        p.start()

    for p in philosophers:
        p.join()

    result = []
    while not records.empty():
        result.append(records.get())
    print(result)
