import uuid
import dataclasses

@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float
    
    @classmethod
    def from_dict(cls,myDic: dict):
        #this was my solution
        #return cls(myDic["code"],myDic["size"],myDic["price"],myDic["longitude"],myDic["latitude"])
        #solution from book
        return cls(**myDic) 
    
    def to_dict(self):
        #my solution
        #return {"code": self.code,"size": self.size,"price": self.price,"longitude": self.longitude,"latitude": self.latitude}
        #book solution
        return dataclasses.asdict(self)
    