import pytest
from main import BooksCollector

class TestBooksCollector:

    # 1) негативная проверка на метод add_new_book

    def test_add_new_book_same_book_not_added_twice(self, collection):

            collection.add_new_book('Преступление и наказание')
            collection.add_new_book('Преступление и наказание')

            # в словаре должна остаться только одна книга
            assert len(collection.get_books_genre()) == 1
            assert 'Преступление и наказание' in collection.get_books_genre()

    # 2) позитивная проверка на метод add_new_book
    @pytest.mark.parametrize('valid_len_book',
                             ['A' * 2,
                              'A' * 40,
                              'A' * 20
                              ])
    def test_add_new_book_add_book_with_valid_len(self, collection, valid_len_book):
        collection.add_new_book(valid_len_book)

        assert valid_len_book in collection.get_books_genre()

    # 3) негативная проверка на метод set_book_genre

    def test_set_get_book_genre_incorrect_genre_unsuccessful(self, collection):

        collection.add_new_book('Остров сокровищ')
        collection.set_book_genre('Остров сокровищ', 'Приключения')
        assert collection.books_genre['Остров сокровищ'] == ''

    # 4) позитивная проверка на метод set_book_genre

    def test_set_book_genre_correct_genre_successful(self, collection):
        collection.add_new_book('Война миров')
        collection.set_book_genre('Война миров', 'Фантастика')
        assert collection.get_book_genre('Война миров') == 'Фантастика'

    # 5) негативная проверка на метод get_book_genre

    def test_get_book_genre_get_incorrect_genre_unsuccessful(self, collection):
        collection.add_new_book('')
        collection.set_book_genre('', 'Фантастика')
        assert collection.get_book_genre('') is None

    # 6) позитивная проверка на метод set_book_genre

    def test_get_book_genre_correct_genre_by_book_title(self, collection):
        collection.books_genre = {'Горе от ума': 'Комедии'}
        assert collection.get_book_genre('Горе от ума') == 'Комедии'

    # 7) позитивная проверка на метод get_books_with_specific_genre

    def test_get_books_with_specific_genre_get_book_with_correct_genre(self, collection):
        collection.books_genre = {
            'Война миров': 'Фантастика',
            'Человек-амфибия': 'Фантастика',
            'Горе от ума': 'Комедии',
            'Ревизор': 'Комедии'
        }
        assert collection.get_books_with_specific_genre('Комедии') == ['Горе от ума', 'Ревизор']

    # 8) позитивная проверка на метод get_books_genre

    def test_get_books_genre_successful(self, collection):
        collection.add_new_book('Женитьба Бальзаминова')
        collection.set_book_genre('Женитьба Бальзаминова', 'Комедии')
        collection.add_new_book('12 стульев')
        collection.set_book_genre('12 стульев', 'Комедии')
        assert collection.get_books_genre() == {
                'Женитьба Бальзаминова': 'Комедии',
                '12 стульев': 'Комедии'
            }


    # 9) позитивная проверка на метод get_books_for_children

    def test_get_books_for_children_successful(self, collection):
        collection.books_genre = {
            'Ну погоди': 'Мультфильмы',
            'Витя Малеев в школе и дома': 'Комедии',
            'Война миров': 'Ужасы'
        }
        assert collection.get_books_for_children() == ['Ну погоди', 'Витя Малеев в школе и дома']

    # 10) негативная проверка на метод get_books_for_children

    def test_get_books_for_children_when_book_has_no_genre(self, collection):
        # проверяем, что книга без жанра не возвращается
        collection.add_new_book('Шерлок Хомс')
        assert collection.get_books_for_children() == []

    # 11) позитивная проверка на метод add_book_in_favorites

    def test_add_book_in_favorites_added_successful(self, collection):
        collection.add_new_book('Война миров')
        collection.add_book_in_favorites('Война миров')
        assert collection.get_list_of_favorites_books() == ['Война миров']

    # 12) негативная проверка на метод add_book_in_favorites

    def test_add_book_in_favorites_not_added_twice(self, collection):
        collection.add_new_book('Война миров')
        collection.add_book_in_favorites('Война миров')
        collection.add_book_in_favorites('Война миров')
        assert collection.get_list_of_favorites_books() == ['Война миров']

    # 13) позитивная проверка на метод delete_book_from_favorites

    def test_delete_book_from_favorites_successful_deleted(self, collection):
        collection.add_new_book('Горе от ума')
        collection.add_book_in_favorites('Горе от ума')
        collection.delete_book_from_favorites('Горе от ума')
        assert collection.get_list_of_favorites_books() == []

    # 14) негативная проверка на метод delete_book_from_favorites

    def test_delete_book_from_favorites_unsuccessful_when_book_not_in_favorites(self, collection):
        collection.add_new_book('Горе от ума')
        collection.delete_book_from_favorites('Горе от ума')
        assert collection.get_list_of_favorites_books() == []

    # 15) позитивная проверка на метод get_list_of_favorites_books

    def test_get_list_of_favorites_books_successful(self, collection):
        collection.favorites = ['Война миров', 'Горе от ума', 'Остров сокровищ']
        assert collection.get_list_of_favorites_books() == ['Война миров', 'Горе от ума', 'Остров сокровищ']
