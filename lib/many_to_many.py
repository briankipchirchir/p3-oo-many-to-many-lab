class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []  # Store the book's contracts
        Book.all.append(self)

    def contracts(self):
        """Return a list of related contracts."""
        return self._contracts

    def authors(self):
        """Return a list of authors associated with this book through contracts."""
        return [contract.author for contract in self._contracts]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []  # Store the author's contracts
        Author.all.append(self)

    def contracts(self):
        """Return a list of related contracts."""
        return self._contracts

    def books(self):
        """Return a list of related books through the contracts."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract between the author and book."""
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        new_contract = Contract(self, book, date, royalties)
        self._contracts.append(new_contract)
        book._contracts.append(new_contract)  # Associate the contract with the book
        return new_contract

    def total_royalties(self):
        """Return the total royalties from all contracts."""
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("The date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

        # After creating a contract, append it to the author's and book's contract list
        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that have the same date."""
        return [contract for contract in cls.all if contract.date == date]
