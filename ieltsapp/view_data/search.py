
class SearchMixin(object):
    """Base mixin for search views."""
    context_object_name = "search_results"
    query_param = "q"

    def get_query_param(self):
        """Returns the query parameter to use in the request GET dictionary."""
        return self.query_param

    models = ()
    def get_models(self):
        """Returns the models to use in the query."""
        return self.models

    exclude = ()
    def get_exclude(self):
        """Returns the models to exclude from the query."""
        return self.exclude

    def get_queryset(self):
        """Returns the initial queryset."""
        return NaSearch.search(self.query, models=self.get_models(), exclude=self.get_exclude())

    def get_query(self, request):
        """Parses the query from the request."""
        return request.GET.get(self.get_query_param(), "").strip()

    empty_query_redirect = None
    def get_empty_query_redirect(self):
        """Returns the URL to redirect an empty query to, or None."""
        return self.empty_query_redirect

    extra_context = {}
    def get_extra_context(self):
        """
        Returns any extra context variables.
        Required for backwards compatibility with old function-based views.
        """
        return self.extra_context

    def get_context_data(self, **kwargs):
        """Generates context variables."""
        context = super(SearchMixin, self).get_context_data(**kwargs)
        context["query"] = self.query
        # Process extra context.
        for key, value in six.iteritems(self.get_extra_context()):
            if callable(value):
                value = value()
            context[key] = value
        return context

    def get(self, request, *args, **kwargs):
        """Performs a GET request."""
        self.query = self.get_query(request)
        if not self.query:
            empty_query_redirect = self.get_empty_query_redirect()
            if empty_query_redirect:
                return redirect(empty_query_redirect)
        return super(SearchMixin, self).get(request, *args, **kwargs)
