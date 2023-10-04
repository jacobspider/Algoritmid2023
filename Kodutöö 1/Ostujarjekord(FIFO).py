class Ostujarjekord:
    def __init__(self):
        self.nimed = []
    def enqueue(self, nimi):
        self.nimed.append(nimi)
    def dequeue(self):
        if not self.is_empty():
            return self.nimed.pop(0)
        else:
            raise IndexError("Rohkem inimesi järjekorras ei ole")
    def is_empty(self):
        return len(self.nimed) == 0
    def size(self):
        return len(self.nimed)

    
ostujarjekord = Ostujarjekord()
ostujarjekord.enqueue("Mari")
ostujarjekord.enqueue("Mikk")
ostujarjekord.enqueue("Joonas")
ostujarjekord.enqueue("Anna")
ostujarjekord.enqueue("Oskar")

print("Hetkene järjekord: ", ostujarjekord.nimed)
dequeue_nimi= ostujarjekord.dequeue()
dequeue_nimi= ostujarjekord.dequeue()
print("Hetkene järjekord: ", ostujarjekord.nimed)
dequeue_nimi= ostujarjekord.dequeue()
dequeue_nimi= ostujarjekord.dequeue()
print("Kas järjekord on tühi?", ostujarjekord.is_empty())
print("Kui palju inimesi on veel järjekorras:", ostujarjekord.size())
