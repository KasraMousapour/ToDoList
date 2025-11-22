class ValidationError(Exception):
    """Raised when input data fails validation rules."""
    pass

class LimitExceededError(Exception):
    """Raised when a project exceeds allowed number of tasks."""
    pass

class DeadlineError(Exception):
    """Raised when deadline is invalid or in the past."""
    pass
