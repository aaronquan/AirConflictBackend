from rest_framework import pagination

class SmallCustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class LargeCustomPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class SmallPageNumberPaginationWithCount(SmallCustomPagination):
    def get_paginated_response(self, data):
        response = super(SmallCustomPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response


class LargePageNumberPaginationWithCount(LargeCustomPagination):
    def get_paginated_response(self, data):
        response = super(LargeCustomPagination, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response

class PageCountOnly(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages
        })
