# coding:utf-8
import math

class OffsetError(Exception):
    def __str__(self):
        return 'offset should be odd number.'

def paginate(offset,objects,page,per_page=5):
    """
    offset: number of  page links,
    objects: paginate objects

    """
    if offset % 2 == 0:
        raise  OffsetError

    edge =  int(math.floor(offset/2))
    total_page = int(math.ceil(len(objects)/float(per_page)))

    page_start = page -edge

    if page_start < 1:
        page_start = 1

    page_end = page + edge
    if page_end > total_page:
        page_end = total_page

    if page -edge < 1:
        page_end =offset

    if page + edge > total_page:
        page_start =  total_page - offset + 1

    return {
        'page_start':page_start,
        'page_end': page_end,
        'page_idx': page
    }





