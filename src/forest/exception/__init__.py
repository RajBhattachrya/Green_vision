import os 
import sys

def error_message_detail(error,error_detail):

    try:
        _,_, exc_tb = error_detail.exe_info()

        if exc_tb is None:
            return f"error occurred : {str(error)}"
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error_message = "error occurred python script name [{0}] line number [{1}] error message". format(
            file_name,exc_tb.tb_lineno,str(error)
        )

        return error_message
    except Exception as e:
        return f"error occurrued : {str(error)}. Additionally , error in exception handling:{str(e)}"
    
class ForestException (Exception):
    def __init__(self,error_message,error_detail=sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,error_detail=error_detail
        ) 
    
    def __str__(self):
        return self.error_message


