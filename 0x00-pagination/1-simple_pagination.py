#!/usr/bin/env python3
""" Module for class Server """
import csv
import math
from typing import List


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
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                print(f"Error: File '{self.DATA_FILE}' not found.")
                return []

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on pagination parameters.

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        start_index = (page - 1) * page_size
        end_index = min(start_index + page_size, len(dataset))
        return dataset[start_index:end_index]
