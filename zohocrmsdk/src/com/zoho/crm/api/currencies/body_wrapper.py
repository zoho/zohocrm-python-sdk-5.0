try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.currencies.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class BodyWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""
		super().__init__()

		self.__currencies = None
		self.__key_modified = dict()

	def get_currencies(self):
		"""
		The method to get the currencies

		Returns:
			list: An instance of list
		"""

		return self.__currencies

	def set_currencies(self, currencies):
		"""
		The method to set the value to currencies

		Parameters:
			currencies (list) : An instance of list
		"""

		if currencies is not None and not isinstance(currencies, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currencies EXPECTED TYPE: list', None, None)
		
		self.__currencies = currencies
		self.__key_modified['currencies'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
