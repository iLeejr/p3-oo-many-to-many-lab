class Author:
    authors = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        Author.authors.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        return [contract.book for contract in self.contracts_list]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)


class Book:
    books = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        Book.books.append(self)

    def contracts(self):
        return self.contracts_list

    def authors(self):
        return [contract.author for contract in self.contracts_list]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        author.contracts_list.append(self)
        book.contracts_list.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        contracts_on_date = [contract for contract in cls.all if contract.date == date]
        return sorted(contracts_on_date, key=lambda contract: contract.date)
