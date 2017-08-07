from django.shortcuts import HttpResponse
import logging
LOGGER = logging.getLogger('forum')


class PrintParamsMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		try:
			response = self.get_response(request)
		except Exception as e:
			LOGGER.exception(e)
			return HttpResponse("wrong")
		return response