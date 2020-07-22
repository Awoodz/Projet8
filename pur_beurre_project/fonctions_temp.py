    def request(url, cat, page=0):
        """This function makes requests to the API."""
        try:
            try:
                # Different parameters can be used for
                # this request, two possibilities
                if page != 0:
                    # Category request
                    user_request = requests.get(
                        url + cat + "/" + str(page) + ".json"
                    )
                else:
                    # Product request
                    user_request = requests.get(url + cat + ".json")
            except TypeError as error:
                print("TypeError" + str(error))
                pass
            return user_request.json()
        except (UnboundLocalError, json.decoder.JSONDecodeError) as error:
            print("Erreur JSON" + str(error))
            pass