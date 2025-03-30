import shutil

class Logger():
    
    _terminal_width = shutil.get_terminal_size().columns
    _mode_list: list[str] = ["Debug", "Release"]
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
    class _LogCategory():
       
        def __init__(self, name: str, color: str = "white", mode: list[str] = ["Release", "Debug"]):
            self.name = name
            self.color = color 
            self.mode = mode


    default =    _LogCategory("Default" , _ansi_colors["white"]                 )
    info    =    _LogCategory("Info"    , _ansi_colors["green"]                 )
    warning =    _LogCategory("Warning" , _ansi_colors["purple"]                )
    error   =    _LogCategory("Error"   , _ansi_colors["red"]                   )
    debug   =    _LogCategory("Debug"   , _ansi_colors["blue"],     ["Debug"]   )
 
    _category_list: list[_LogCategory] = [default, info, warning, error, debug]


    def __init__(self, mode: str = "Debug"):
        self.mode = mode 
        self._check_mode()
        

    def _check_mode(self) -> None:
        if self.mode not in Logger._mode_list: 
            raise Exception(f"{self.mode} is not a valid mode. Try one of these instead: {Logger._mode_list}")
        
    def _check_category(self, category: _LogCategory | str) -> bool:
        return True if category in Logger._category_list else False
    
    def _get_indent(self) -> int:
        indent = int(0.1 * Logger._terminal_width) if Logger._terminal_width >= 100 else int(0.3 * Logger._terminal_width)
        return indent
    
    def _break_massage(self, massage: str, indent: int) -> str:
        def _get_break_index(space_inidces: list[int], target_index: int) -> int:
            filtered_indices = [index for index in space_inidces if index <= target_index]
            return filtered_indices[-1]

        if indent + len(massage) <= Logger._terminal_width: return massage
        else:
            for i in range(Logger._terminal_width - indent, len(massage), Logger._terminal_width):
              
                space_indices: list = [index for index, char in enumerate(massage) if char == " "]
                break_index = _get_break_index(space_indices, i)
                massage = massage[:break_index] + f"\n{' '*indent}" + massage[break_index+1:]
               
            return massage

        

    def log(self, massage: str, category: _LogCategory | str = default) -> None:

        is_existing_category = self._check_category(category)
        indent = self._get_indent()
        massage = self._break_massage(massage, indent)

        if not is_existing_category:
            spacing = indent - (len(category) + 2)
            print(f"[{category}]{' '*spacing}{massage}")

        elif self.mode in category.mode:
            spacing = indent - (len(category.name) + 2)
            print(f"[{category.color}{category.name}{Logger._ansi_colors["white"]}]{' '*spacing}{massage}")
            