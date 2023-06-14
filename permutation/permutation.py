import json
import requests
from typing import List


class Permutation:
    def __init__(self, permutation_function_url: str):
        self.function_url = permutation_function_url

    def _function_data(self, data: dict):
        """
        Internal function that sends data to the API
        :param data: data to be processed by the API as a dict
        :type data: dict
        :return: json object with results from the API
        """
        _data = json.dumps(data)
        r = requests.post(self.function_url, data=_data)
        # consider API Errors
        if r.status_code == 200:
            return json.loads(r.content.decode('utf-8'))
        return {'error': r.status_code, 'message': r.content.decode('utf-8')}

    def find(self, n: int, r: int, next_variable: str):
        """
        Generates permutations based on the given parameters. It sends a JSON payload using the provided params
        :param n: The total number of elements available for permutation
        :param r: The number of elements to be selected in each permutation
        :param next_variable: The next variable to be included in the permutation
        :return: response returns the generated permutation in JSON format. The response body contains the following information:
        eventId: An event ID associated with the permutation.
        n: The total number of elements available for permutation.
        r: The number of elements selected in each permutation.
        numberOfPermutations: The total number of possible permutations.
        permutationVariables: An array of arrays, where each inner array represents a permutation with the selected variables.
        inserted_id: The ID of the inserted permutation.
        """
        data = {'inserted_id': None,
                'nextVariable': next_variable,
                "n": n, "r": r,
                "command": "findPermutation"}
        return self._function_data(data)

    def save(self, id: str, selected_permutation: List[str]):
        """
        Saves a selected permutation. It sends a JSON payload with the parameters provided
        :param id: The ID of the permutation to be saved
        :param selected_permutation: An array of variables representing the selected permutation
        :return: The response confirms the successful saving of the permutation. The response body contains a success message.
        """
        data = {"inserted_id": id, "selectedPermutation": [selected_permutation], "command": "savePermutation"}
        return self._function_data(data)

    def retrieve(self, id):
        """
        Retrieves a specific permutation based on its ID
        :param id:
        :return: the requested permutation in JSON format. The response body contains the following information:
        eventId: An event ID associated with the permutation.
        n: The total number of elements available for permutation.
        r: The number of elements selected in each permutation.
        permutationVariables: An array representing the selected permutation.
        inserted_id: The ID of the permutation.
        """
        data = {"inserted_id": id, "command": "showPermutation"}
        return self._function_data(data)