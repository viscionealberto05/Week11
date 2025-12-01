from dataclasses import dataclass

@dataclass
class Object:
    object_id : int
    object_name : str

    @property
    def id(self):
        return self.object_id
    @property
    def name(self):
        return self.object_name

    def __str__(self):
        return f"{self.object_id}, {self.object_name}"

    def __hash__(self):
        return hash(self.object_id)
