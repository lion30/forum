class PrintParamsMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print(request.GET)
		print(request.POST)
		response = self.get_response(request)
		return response