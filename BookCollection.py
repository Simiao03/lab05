class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertBook(self, book):
        node = BookCollectionNode(book)
        if self.isEmpty():
            self.head = node
        elif node.book > self.head.book:
            node.setNext(self.head)
            self.head = node
        else:
            current = self.head
            while current.getNext() is not None and current.getNext().book > node.book:
                current = current.getNext()
            node.setNext(current.getNext())
            current.setNext(node)

    def getBooksByAuthor(self, author):
        result = []
        current = self.head
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                result.append(current.getData())
            current = current.getNext()
        return result

    def getAllBooksInCollection(self):
        result = []
        current = self.head
        while current != None:
            result.append(current.getData())
            current = current.getNext()

    def removeAuthor(self, author):
        author = author.lower()
        current = self.head
        previous = None
        while current is not None:
            if current.getData().getAuthor().lower() == author:
                if previous is None:
                    # Removing the head node
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                # Move the current pointer to the next node
                current = current.getNext()
            else:
                # Move the previous and current pointers to the next node
                previous = current
                current = current.getNext()

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode is None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        else:
            return self.recursiveSearchTitle(title, bookNode.getNext())



