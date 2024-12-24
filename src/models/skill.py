class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_skill_details(self):
        return {
            "name": self.name,
            "level": self.level
        }