from abc import ABC, abstractmethod

class Skill(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Technology(Skill):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class SkillCategory(Skill):
    def __init__(self, name):
        self.name = name
        self.skills = []

    def add(self, skill):
        self.skills.append(skill)

    def remove(self, skill):
        self.skills.remove(skill)

    def get_name(self):
        return {
            "name": self.name,
            "skills": [skill.get_name() for skill in self.skills]
        }

# Usage
if __name__ == "__main__":

    programming = SkillCategory("Programming")
    programming.add(Technology("Python"))
    programming.add(Technology("C"))
    programming.add(Technology("Java"))

    frontend = SkillCategory("Frontend")
    frontend.add(Technology("React"))
    frontend.add(Technology("HTML/CSS"))

    backend = SkillCategory("Backend")
    backend.add(Technology("Flask"))
    backend.add(Technology("Django"))
    backend.add(Technology("SpringBoot"))

    skills = SkillCategory("All Skills")
    skills.add(programming)
    skills.add(frontend)
    skills.add(backend)

    print(programming.get_name())
