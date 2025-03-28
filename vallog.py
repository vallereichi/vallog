class Logger():

    _mode_list = ["Debug", "Release"]
    _category_dict = {
        "Default":  {'color':"white",   'mode':["Release", "Debug"]  },        
        "Info": 	{'color':"green",   'mode':["Release", "Debug"]  },
        "Warning":  {'color':"purple",  'mode':["Release", "Debug"]  },
        "Error":    {'color':"red",     'mode':["Release", "Debug"]  },
        "Debug":    {'color':"blue",    'mode':["Debug"]    },
    }
    _ansi_colors = {
        'white':        "\033[0m",
        'red':          "\033[91m",
        'green':        "\033[92m",
        'yellow':       "\033[93m",
        'blue':         "\033[94m",
        'purple':       "\033[95m",
        'cyan':         "\033[96m",
        'bold':         "\033[1m",
        'underline':    "\033[4m"
    }   

    def __init__(self, mode: str = "Debug"):
        self.mode = mode 
        self._check_mode()
        

    def _check_mode(self) -> None:
        if self.mode not in Logger._mode_list: 
            raise Exception(f"{self.mode} is not a valid mode. Try one of these instead: {Logger._mode_list}")
        
    def _check_category(self, category: str) -> bool:
        return True if category in Logger._category_dict.keys() else False
        

    def log(self, massage: str, category: str = "Default") -> None:
        is_existing_category = self._check_category(category)
        if not is_existing_category:
            print(f"[{category}]    {massage}")
        elif self.mode in Logger._category_dict[category]["mode"]:
            color = Logger._category_dict[category]["color"]
            print(f"[{Logger._ansi_colors[color]}{category}{Logger._ansi_colors["white"]}]    {massage}")
        
    



        

def main():
    logger = Logger()
    logger.log("erste Log Massage!!", "Default")



if __name__ == "__main__":
    main()