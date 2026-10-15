class ArrayDeque:

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    # ---------- Fonctions de base ----------
    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def __len__(self):
        return self.size

    # ---------- Ajouts ----------
    def add_front(self, x):
        if self.is_full():
            raise IndexError("deque plein")
        # 1) on RECULE front (avec modulo pour boucler)
        self.front = (self.front - 1) % self.capacity
        # 2) on pose la valeur dans cette case
        self.data[self.front] = x
        # 3) un élément de plus
        self.size += 1

    def add_back(self, x):
        if self.is_full():
            raise IndexError("deque plein")
        # case libre juste après le dernier élément
        index = (self.front + self.size) % self.capacity
        self.data[index] = x
        self.size += 1

    # ---------- Retraits ----------
    def remove_front(self):
        if self.is_empty():
            raise IndexError("deque vide")
        # 1) on LIT d'abord
        value = self.data[self.front]
        # 2) on AVANCE front ensuite
        self.front = (self.front + 1) % self.capacity
        # 3) un élément de moins
        self.size -= 1
        return value

    def remove_back(self):
        if self.is_empty():
            raise IndexError("deque vide")
        # case du dernier élément
        index = (self.front + self.size - 1) % self.capacity
        value = self.data[index]
        self.size -= 1
        return value

    # ---------- Lecture sans retirer ----------
    def peek_front(self):
        if self.is_empty():
            raise IndexError("deque vide")
        return self.data[self.front]

    def peek_back(self):
        if self.is_empty():
            raise IndexError("deque vide")
        return self.data[(self.front + self.size - 1) % self.capacity]

    # ---------- Recherche et autres ----------
    def search(self, x):
        """Renvoie la position de x dans le deque (0 = premier), ou -1."""
        for i in range(self.size):
            if self.data[(self.front + i) % self.capacity] == x:
                return i
        return -1

    def contains(self, x):
        return self.search(x) != -1

    def clear(self):
        self.data = [None] * self.capacity
        self.front = 0
        self.size = 0

    def to_list(self):
        """Contenu logique, du premier au dernier."""
        return [self.data[(self.front + i) % self.capacity]
                for i in range(self.size)]

    def display(self):
        print(self.to_list())

    def debug(self):
        """Montre le tableau brut + front + size (utile pour comprendre)."""
        print("data =", self.data, "| front =", self.front, "| size =", self.size)


# ---------- Tests ----------
if __name__ == "__main__":
    d = ArrayDeque(5)

    # L'exemple du cours : add_front(10), add_front(20), add_back(40), remove_front()
    d.add_front(10); d.debug()   # [_,_,_,_,10]  front=4 size=1
    d.add_front(20); d.debug()   # [_,_,_,20,10] front=3 size=2
    d.add_back(40);  d.debug()   # [40,_,_,20,10] front=3 size=3
    print("retiré :", d.remove_front())          # 20
    d.debug()                                    # front=4 size=2
    d.display()                                  # [10, 40]

    assert d.to_list() == [10, 40]
    assert d.search(40) == 1 and d.search(99) == -1

    # Exercice : add_back(1), add_back(2), add_front(0), add_front(9),
    #            remove_back(), remove_front()  ->  [0, 1]
    e = ArrayDeque(5)
    e.add_back(1); e.add_back(2); e.add_front(0); e.add_front(9)
    e.remove_back(); e.remove_front()
    assert e.to_list() == [0, 1]

    # Erreurs : vide et plein
    try:
        ArrayDeque(2).remove_front()
    except IndexError as err:
        print("Erreur attendue :", err)

    f = ArrayDeque(2)
    f.add_back(1); f.add_back(2)
    try:
        f.add_back(3)
    except IndexError as err:
        print("Erreur attendue :", err)

    print("Tous les tests passent")