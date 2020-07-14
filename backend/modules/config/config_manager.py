import json

class ConfigManager():
    '''
    Manages system variables to config.json
    '''

    def __init__(self):
        self.config_dict: dict = {} #Empty dictionary
        self.file_name: str = "./modules/config/config.json"
    
    def set_config(self, key: str, value: str) -> None:
        '''
        Set a configuration value with a given key and value

        @key: str -> the key
        @value: str -> value of the key
        @returns: None
        '''

        self.config_dict = json.loads(open(self.file_name, "r").read())
        self.config_dict[key] = value
        with open(self.file_name, "w") as f:
            f.writelines(json.dumps(self.config_dict, indent=4))

    def set_crypto(self, key: bytes) -> None:

        with open("./modules/config/crypto.txt", "w") as f:
            f.write(key.decode("utf-8"))

    def get_crypto(self) -> bytes:

        # with open("./modules/config/crypto.txt", "r") as f:
        #     print(f.read())

            
        with open("./modules/config/crypto.txt", "r") as f:
            return f.readline().encode("utf-8")

    def get_config(self, key: str) -> str:
        '''
        Returns value of config variable based on key
        
        @key: str -> the key to find in .json file
        @returns: str -> the value of environment variable
        '''

        self.config_dict = json.loads(open(self.file_name, "rb").read())
        return self.config_dict[key]