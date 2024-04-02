#!/usr/bin/env python3
'''Simple pagination'''
import csv
import math
from typing import List, Dict

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        Hypermedia pagination
        Returns hypermedia information about a given page(dataset)
        '''

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if len(page_data) == page_size else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
