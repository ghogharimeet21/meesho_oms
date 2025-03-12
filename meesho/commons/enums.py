import enum



class Orders_Reason_for_Credit_Entry(enum.Enum):
    CANCELLED = "CANCELLED"
    DELIVERED = "DELIVERED"
    DOOR_STEP_EXCHANGED = "DOOR_STEP_EXCHANGED"
    RTO_COMPLETE = "RTO_COMPLETE"
    RTO_LOCKED = "RTO_LOCKED"
    RTO_OFD = "RTO_OFD"
    SHIPPED = "SHIPPED"



class Type_of_Return(enum.Enum):
    Courier_Return_RTO = "Courier Return (RTO)"
    Customer_Return = "Customer Return"


class SubType(enum.Enum):
    forward_RTO = "forward_RTO"
    FIRST_RET = "FIRST_RET"

class Expected_Delivery_Date(enum.Enum):
    NA = "NA"