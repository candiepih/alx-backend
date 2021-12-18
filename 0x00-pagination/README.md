# Pagination

Aim of this module is to understand the concepts of pagination with the following learning objectives:
 * How to paginate a dataset with simple `page` and `page_size` parameters 
 * How to paginate a dataset with `hypermedia metadata`
 * How to paginate in a `deletion-resilient` manner

# Files

The following task files were used to help understand the concepts:

[0-simple_helper_function.py](./0-simple_helper_function.py)

Contains a function that returns a tuple of size two containing a `start index` and an `end index` corresponding to the range of indexes to return in a list for those particular pagination parameters.

[1-simple_pagination.py](./1-simple_pagination.py)

Contains class with methods to create simple pagination from csv data

Requirements:

* You have to use this [CSV file](./Popular_Baby_Names.csv) (same as the one presented at the top of the project)
* Use `assert` to verify that both arguments are integers greater than 0. 
* Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows). 
* If the input arguments are out of range for the dataset, an empty list should be returned.

[2-hypermedia_pagination.py](./2-hypermedia_pagination.py)

Contains class with methods to create simple pagination from csv data

Requirements:

Returns dictionary with the following keys:
* `page_size`: the length of the returned dataset page
* `page`: the current page number
* `data`: the dataset page (equivalent to return from previous task)
* `next_page`: number of the next page, None if no next page
* `prev_page`: number of the previous page, None if no previous page
* `total_pages`: the total number of pages in the dataset as an integer

[3-hypermedia_del_pagination.py](./3-hypermedia_del_pagination.py)

Deletion-resilient hypermedia pagination

Requirements/Behavior:

The method should return a dictionary with the following key-value pairs:

* `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
* `next_index`: the next index to query with. That should be the index of the first item after the last item on the current page.
* `page_size`: the current page size
* `data`: the actual page of the dataset

* Use `assert` to verify that `index` is in a valid range.
* If the user queries index 0, `page_size` 10, they will get rows indexed 0 to 9 included. 
* If they request the next index (10) with `page_size` 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.