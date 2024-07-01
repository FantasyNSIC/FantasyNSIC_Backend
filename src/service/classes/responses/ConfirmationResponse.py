"""This file contains the ConfirmationResponse class which represent a confirmation on
    the success or failure of a request."""


class ConfirmationResponse:
    """
    ConfirmationResponse class is used to represent a confirmation on the success or failure of a request.
    """
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message

    @property
    def success(self):
        """Getter for the success attribute."""
        return self._success
    
    @success.setter
    def success(self, success: bool):
        """Setter for the success attribute.
        
        Args:
            success (bool): The success value.
        """
        self._success = success

    @property
    def message(self):
        """Getter for the message attribute."""
        return self._message
    
    @message.setter
    def message(self, message: str):
        """Setter for the message attribute.
        
        Args:
            message (str): The message value.
        """
        self._message = message

    def toJson(self):
        return {
            'success': self.success,
            'message': self.message
        }
