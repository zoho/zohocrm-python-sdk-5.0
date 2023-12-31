try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ActionWrapper(object):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""

		self.__hipaa_compliance = None
		self.__key_modified = dict()

	def get_hipaa_compliance(self):
		"""
		The method to get the hipaa_compliance

		Returns:
			ActionHandler: An instance of ActionHandler
		"""

		return self.__hipaa_compliance

	def set_hipaa_compliance(self, hipaa_compliance):
		"""
		The method to set the value to hipaa_compliance

		Parameters:
			hipaa_compliance (ActionHandler) : An instance of ActionHandler
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.hipaa_compliance.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler

		if hipaa_compliance is not None and not isinstance(hipaa_compliance, ActionHandler):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hipaa_compliance EXPECTED TYPE: ActionHandler', None, None)
		
		self.__hipaa_compliance = hipaa_compliance
		self.__key_modified['hipaa_compliance'] = 1

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
