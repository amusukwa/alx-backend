#!/usr/bin/env python3
""" Module for Deletion-resilient hypermedia pagination """
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return hypermedia metadata for a given start index and page size.

        Args:
            index (int): The start index of the page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: Hypermedia metadata containing page information.
        """
        assert index is None or (isinstance(index, int) and index >= 0), "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.indexed_dataset()
        total_items = len(dataset)

        if index is None:
            index = 0

        if index >= total_items:
            return {
                "index": index,
                "next_index": None,
                "page_size": 0,
                "data": []
            }

        end_index = min(index + page_size, total_items)
        next_index = end_index if end_index < total_items else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": [dataset[i] for i in range(index, end_index)]
        }

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hypermedia metadata for a given page and page size.

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: Hypermedia metadata containing page information.
        """
        index = (page - 1) * page_size
        return self.get_hyper_index(index, page_size)
