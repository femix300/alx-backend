#!/usr/bin/env python3
'''Simple pagination'''
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Gets a page using the page number and page size'''

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        filename = 'Popular_Baby_Names.csv'
        result = []

        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)

                next(reader)

                for _ in range(start_index - 1):
                    next(reader)

                for row_no, row in enumerate(reader, start=start_index):
                    result.append(row)

                    if row_no >= (end_index - 1):
                        break

                return result

        except (IndexError, StopIteration):
            return []
