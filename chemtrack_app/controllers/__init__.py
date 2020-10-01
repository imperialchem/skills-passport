
# For group checks
from .groups import is_student
from .groups import is_teacher

# For record management
from .record import create_record
from .record import has_acces_to
from .record import can_modify
from .record import can_submit

# For admin check template
from .templates import check_template
from .templates import get_template