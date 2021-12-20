#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

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
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia index for a dataset

        Args:
            index (int, optional): Index of dataset to start from.
            Defaults to None.
            page_size (int, optional): Size of dataset to return.
            Defaults to 10.

        Returns:
            Dict: Hypermedia index
        """
        assert type(index) is int
        assert type(page_size) is int
        assert 0 <= index < len(self.dataset())
        next_index = index + page_size
        try:
            data = [self.indexed_dataset()[k]
                    for k in range(index, next_index)]
        except KeyError:
            data = [self.indexed_dataset()[k]
                    for k in range(index + 1, next_index + 1)]
        info = {
            "index": index,
            "next_index": next_index,
            "page_size": 10 if index == 0 else page_size,
            "data": data
        }
        return info
